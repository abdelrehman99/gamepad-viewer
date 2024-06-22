import pygame
import logging

class JoystickHandler:
    def __init__(self):
        self.joystick = None
        self.initialize()

    def initialize(self):
        pygame.init()
        pygame.joystick.init()

        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            logging.error("No joystick detected.")
            pygame.quit()
            exit()

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        logging.info(f"Joystick: {self.joystick.get_name()}")

    def process_joystick_input(self):
        pygame.event.pump()
        axes = [self.joystick.get_axis(i) for i in range(self.joystick.get_numaxes())]
        buttons = [self.joystick.get_button(i) for i in range(self.joystick.get_numbuttons())]
        hats = [self.joystick.get_hat(i) for i in range(self.joystick.get_numhats())]
        # print(f"axes are {axes}")
        # print(f"buttons are {buttons}")
        # print(f"hats are {hats}")
        

        return axes, buttons, hats
