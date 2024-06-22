import sys
import socket
import pickle
import time
import pygame
import numpy as np
import logging
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QTextBrowser, QLabel, QHBoxLayout)
from PySide6.QtCore import QTimer, QTime, Qt, QThread, Signal, QMutex

RETRY_INTERVAL = 5
DEAD_MAN_SWITCH_TIMEOUT = 5
SURGE_STEP = ROLL_STEP = 0.0005

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Worker(QThread):
    log_signal = Signal(str)
    update_indicator = Signal(bool)
    stop_signal = Signal()

    def __init__(self):
        super().__init__()
        self.running = False
        self.joystick = None
        self.s = None
        self.LAST_JOYSTICK_UPDATE_TIME = time.time()
        self.Cf = 0.6
        self.activation_delay = 0.5
        self.last_activation_time = 0
        self.flip = 0
        self.prev = 0
        self.mutex = QMutex()

    def initialize(self):
        pygame.init()
        pygame.joystick.init()

        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            self.log_signal.emit("No joystick detected.")
            pygame.quit()
            return None

        try:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            self.log_signal.emit(f"Joystick: {joystick.get_name()}")
            self.update_indicator.emit(True)
            return joystick
        except pygame.error as e:
            self.log_signal.emit(f"Joystick initialization error: {e}")
            pygame.quit()
            return None

    def connect_to_pi(self):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(RETRY_INTERVAL)
                s.connect(("192.168.0.2", 6161))  # Raspberry Pi's IP and port
                self.log_signal.emit("Connected to Raspberry Pi.")
                return s
            except (ConnectionRefusedError, socket.timeout, TimeoutError):
                self.log_signal.emit(f"Connection to Raspberry Pi failed. Retrying in {RETRY_INTERVAL} seconds...")
                time.sleep(RETRY_INTERVAL)

    def process_joystick_input(self, joystick):
        pygame.event.pump()
        axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
        buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
        hats = [joystick.get_hat(i) for i in range(joystick.get_numhats())]
        return axes, buttons, hats

    def dead_man_switch(self, axes, buttons):
        if any(axes) or any(buttons):
            self.LAST_JOYSTICK_UPDATE_TIME = time.time()

        if time.time() - self.LAST_JOYSTICK_UPDATE_TIME > DEAD_MAN_SWITCH_TIMEOUT:
            return True
        return False

    def run(self):
        self.log_signal.emit("Ground station started.")
        self.joystick = self.initialize()
        if self.joystick is None:
            return

        self.running = True

        while self.running:
            if self.s is None or self.s.fileno() == -1:
                self.s = self.connect_to_pi()

            if self.s is not None and self.s.fileno() != -1:
                axes, buttons, hats = self.process_joystick_input(self.joystick)
                dead_man_triggered = self.dead_man_switch(axes, buttons)

                if hats == [(0, 1)]:
                    if time.time() - self.last_activation_time > self.activation_delay:
                        self.Cf = min(self.Cf + 0.1, 1)
                        self.last_activation_time = time.time()
                elif hats == [(0, -1)]:
                    if time.time() - self.last_activation_time > self.activation_delay:
                        self.Cf = max(self.Cf - 0.1, 0.1)
                        self.last_activation_time = time.time()

                if buttons[2] == 1 and self.prev == 0:
                    self.flip = 1 - self.flip
                self.prev = buttons[2]

                if dead_man_triggered:
                    self.log_signal.emit("Dead Man's Switch triggered. Stopping ROV.")
                    Vsurge, Vsway, Vheave, Vroll, Vpitch, Vyaw = 0, 0, 0, 0, 0, 0
                else:
                    Vsway = axes[2] * self.Cf
                    Vroll = axes[3] * self.Cf
                    Vpitch = axes[1] * self.Cf
                    Vyaw = axes[0] * self.Cf

                    if buttons[4]:
                        Vheave = self.Cf
                    elif buttons[6]:
                        Vheave = -self.Cf
                    else:
                        Vheave = 0

                    if buttons[5]:
                        Vsurge = self.Cf
                    elif buttons[7]:
                        Vsurge = -self.Cf
                    else:
                        Vsurge = 0

                    if buttons[0]:
                        Vsurge = Vsway = Vheave = Vroll = Vpitch = Vyaw = 0

                Vm = np.array([Vsurge, Vsway, Vheave, Vroll, Vpitch, Vyaw, self.flip])

                try:
                    self.s.sendall(pickle.dumps(Vm))
                except (BrokenPipeError, ConnectionResetError):
                    self.log_signal.emit("Connection to Raspberry Pi lost. Attempting to reconnect...")
                    self.s.close()
                    self.s = None

            time.sleep(0.1)

        self.cleanup()

    def cleanup(self):
        if self.s is not None:
            self.s.close()
        pygame.quit()
        self.update_indicator.emit(False)
        self.log_signal.emit("Worker stopped.")
        self.stop_signal.emit()

    def stop(self):
        self.running = False
        self.log_signal.emit("Stopping...")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ROV Controller")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.log_browser = QTextBrowser(self)
        self.layout.addWidget(self.log_browser)

        self.timer = QTimer(self)
        self.time = QTime(0, 0, 0, 0)
        self.timer.timeout.connect(self.update_time)

        self.time_display = QLabel(self.time.toString("hh:mm:ss.zzz")[:-1], self)
        self.time_display.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.time_display)

        self.button_layout = QHBoxLayout()
        self.run_button = QPushButton("Run", self)
        self.stop_run_button = QPushButton("Stop Run", self)
        self.start_button = QPushButton("Start Timer", self)
        self.stop_button = QPushButton("Stop Timer", self)
        self.reset_button = QPushButton("Reset Timer", self)

        self.button_layout.addWidget(self.run_button)
        self.button_layout.addWidget(self.stop_run_button)
        self.button_layout.addWidget(self.start_button)
        self.button_layout.addWidget(self.stop_button)
        self.button_layout.addWidget(self.reset_button)
        self.layout.addLayout(self.button_layout)

        self.indicator = QLabel(self)
        self.indicator.setAlignment(Qt.AlignCenter)
        self.indicator.setFixedSize(20, 20)
        self.indicator.setStyleSheet("background-color: red")
        self.layout.addWidget(self.indicator)

        self.setLayout(self.layout)

        self.run_button.clicked.connect(self.run_action)
        self.stop_run_button.clicked.connect(self.stop_run_action)
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.reset_button.clicked.connect(self.reset_timer)

        self.worker = Worker()
        self.worker.log_signal.connect(self.log_message)
        self.worker.update_indicator.connect(self.update_joystick_indicator)
        self.worker.stop_signal.connect(self.on_worker_stopped)

    def log_message(self, message):
        self.log_browser.append(message)

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_display.setText(self.time.toString("hh:mm:ss.zzz")[:-1])  # Drop the last digit to get 1/100 seconds

    def start_timer(self):
        self.timer.start(10)  # update every 10 milliseconds

    def stop_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_display.setText(self.time.toString("hh:mm:ss.zzz")[:-1])

    def run_action(self):
        if not self.worker.isRunning():
            self.worker.running = True
            self.run_button.setEnabled(False)
            self.stop_run_button.setEnabled(True)
            self.worker.start()

    def stop_run_action(self):
        self.worker.stop()
        self.run_button.setEnabled(False)
        self.stop_run_button.setEnabled(False)

    def on_worker_stopped(self):
        self.run_button.setEnabled(True)
        self.stop_run_button.setEnabled(False)

    def update_joystick_indicator(self, connected):
        if connected:
            self.indicator.setStyleSheet("background-color: green")
        else:
            self.indicator.setStyleSheet("background-color: red")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
