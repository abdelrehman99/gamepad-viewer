from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import QWidget
from Ui_game import Ui_Game
from joystick_handler import JoystickHandler

class Widget(QWidget, Ui_Game):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")
      
    def capturing(self,lent,hith):
        joystick_handler = JoystickHandler()
        while True:
            axes, buttons, hats = joystick_handler.process_joystick_input()
            button_indices = {
                            "l2_label": 6,
                            "l3_label": 10,
                            "r3_label": 11,
                            "x_label": 2,
                            "squ_label": 3,
                            "o_label": 1,
                            "tri_label": 0,
                            "r2_label": 7,
                            "r1_label": 5,
                            "l1_label": 4,
                            "start_label": 9,
                            "select_label": 8
                             }
    
            for label_name, index in button_indices.items():
                if buttons[index] == 0:
                    getattr(self, label_name).hide()
                else:
                    getattr(self, label_name).show()
            hat = hats[0]
        
            self.r_label.show() if hat[0] == 1 else self.r_label.hide()
            
            self.l_label.show() if hat[0] == -1 else self.l_label.hide()
    
            self.u_label.show() if hat[1] == 1 else self.u_label.hide()
            
            self.d_label.show() if hat[1] == -1 else self.d_label.hide()
            print(axes[0])
            gan=8
            self.l_analog_label.setGeometry(QRect(228+gan*axes[0], 309+gan*axes[1], 94, 94))
            self.r_analog_label.setGeometry(QRect(485+gan*axes[2], 309+gan*axes[3], 94, 94))
            self.l3_label.setGeometry(QRect(228+gan*axes[0], 309+gan*axes[1], 94, 94))
            self.r3_label.setGeometry(QRect(485+gan*axes[2], 309+gan*axes[3], 94, 94))

            

        


