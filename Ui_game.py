from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)
import resource_rc

class Ui_Game(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(993, 757)

        self.gamepad_widget = QWidget(Form)
        self.gamepad_widget.setObjectName(u"gamepad_widget")
        self.gamepad_widget.setGeometry(QRect(80, 50, 807, 600))
        self.gamepad_widget.setMinimumSize(QSize(807, 600))
        self.gamepad_widget.setMaximumSize(QSize(807, 600))

        self.gp_label = QLabel(self.gamepad_widget)
        self.gp_label.setObjectName(u"gp_label")
        self.gp_label.setGeometry(QRect(1, 1, 805, 598))
        self.gp_label.setMinimumSize(QSize(805, 598))
        self.gp_label.setMaximumSize(QSize(805, 598))
        self.gp_label.setPixmap(QPixmap(u":/base.png"))
        self.gp_label.setScaledContents(False)
        self.gp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.l2_label = QLabel(self.gamepad_widget)
        self.l2_label.setObjectName(u"l2_label")
        self.l2_label.setGeometry(QRect(109, 0, 100, 91))
        self.l2_label.setMinimumSize(QSize(100, 91))
        self.l2_label.setMaximumSize(QSize(100, 91))
        self.l2_label.setPixmap(QPixmap(u":/l2.png"))
        self.l2_label.setScaledContents(True)

        self.r_analog_label = QLabel(self.gamepad_widget)
        self.r_analog_label.setObjectName(u"r_analog_label")
        self.r_analog_label.setGeometry(QRect(485, 309, 94, 94))
        self.r_analog_label.setMinimumSize(QSize(94, 94))
        self.r_analog_label.setMaximumSize(QSize(94, 94))
        self.r_analog_label.setSizeIncrement(QSize(0, 0))
        self.r_analog_label.setPixmap(QPixmap(u":/analog.png"))
        self.r_analog_label.setScaledContents(True)

        self.l_analog_label = QLabel(self.gamepad_widget)
        self.l_analog_label.setObjectName(u"l_analog_label")
        self.l_analog_label.setGeometry(QRect(228, 309, 94, 94))
        self.l_analog_label.setMinimumSize(QSize(94, 94))
        self.l_analog_label.setMaximumSize(QSize(94, 94))
        self.l_analog_label.setSizeIncrement(QSize(0, 0))
        self.l_analog_label.setPixmap(QPixmap(u":/analog.png"))
        self.l_analog_label.setScaledContents(True)

        self.l3_label = QLabel(self.gamepad_widget)
        self.l3_label.setObjectName(u"l3_label")
        self.l3_label.setGeometry(QRect(228, 309, 94, 94))
        self.l3_label.setMinimumSize(QSize(94, 94))
        self.l3_label.setMaximumSize(QSize(94, 94))
        self.l3_label.setSizeIncrement(QSize(0, 0))
        self.l3_label.setPixmap(QPixmap(u":/l3.png"))
        self.l3_label.setScaledContents(True)

        self.r3_label = QLabel(self.gamepad_widget)
        self.r3_label.setObjectName(u"r3_label")
        self.r3_label.setGeometry(QRect(485, 309, 94, 94))
        self.r3_label.setMinimumSize(QSize(94, 94))
        self.r3_label.setMaximumSize(QSize(94, 94))
        self.r3_label.setSizeIncrement(QSize(0, 0))
        self.r3_label.setPixmap(QPixmap(u":/r3.png"))
        self.r3_label.setScaledContents(True)

        self.x_label = QLabel(self.gamepad_widget)
        self.x_label.setObjectName(u"x_label")
        self.x_label.setGeometry(QRect(625, 276, 54, 54))
        self.x_label.setMinimumSize(QSize(54, 54))
        self.x_label.setMaximumSize(QSize(54, 54))
        self.x_label.setPixmap(QPixmap(u":/x.png"))
        self.x_label.setScaledContents(True)

        self.squ_label = QLabel(self.gamepad_widget)
        self.squ_label.setObjectName(u"squ_label")
        self.squ_label.setGeometry(QRect(569, 219, 54, 54))
        self.squ_label.setMinimumSize(QSize(54, 54))
        self.squ_label.setMaximumSize(QSize(54, 54))
        self.squ_label.setPixmap(QPixmap(u":/square.png"))
        self.squ_label.setScaledContents(True)

        self.o_label = QLabel(self.gamepad_widget)
        self.o_label.setObjectName(u"o_label")
        self.o_label.setGeometry(QRect(682, 219, 54, 54))
        self.o_label.setMinimumSize(QSize(54, 54))
        self.o_label.setMaximumSize(QSize(54, 54))
        self.o_label.setPixmap(QPixmap(u":/o.png"))
        self.o_label.setScaledContents(True)

        self.tri_label = QLabel(self.gamepad_widget)
        self.tri_label.setObjectName(u"tri_label")
        self.tri_label.setGeometry(QRect(625, 160, 54, 54))
        self.tri_label.setMinimumSize(QSize(54, 54))
        self.tri_label.setMaximumSize(QSize(54, 54))
        self.tri_label.setPixmap(QPixmap(u":/triangle.png"))
        self.tri_label.setScaledContents(True)

        self.u_label = QLabel(self.gamepad_widget)
        self.u_label.setObjectName(u"u_label")
        self.u_label.setGeometry(QRect(134, 182, 37, 53))
        self.u_label.setMinimumSize(QSize(37, 53))
        self.u_label.setSizeIncrement(QSize(37, 53))
        self.u_label.setPixmap(QPixmap(u":/pad_u.png"))
        self.u_label.setScaledContents(True)

        self.d_label = QLabel(self.gamepad_widget)
        self.d_label.setObjectName(u"d_label")
        self.d_label.setGeometry(QRect(136, 254, 37, 53))
        self.d_label.setMinimumSize(QSize(37, 53))
        self.d_label.setSizeIncrement(QSize(37, 53))
        self.d_label.setPixmap(QPixmap(u":/pad_d.png"))
        self.d_label.setScaledContents(True)

        self.r_label = QLabel(self.gamepad_widget)
        self.r_label.setObjectName(u"r_label")
        self.r_label.setGeometry(QRect(163, 225, 53, 37))
        self.r_label.setMinimumSize(QSize(53, 37))
        self.r_label.setMaximumSize(QSize(53, 37))
        self.r_label.setPixmap(QPixmap(u":/pad_r.png"))

        self.l_label = QLabel(self.gamepad_widget)
        self.l_label.setObjectName(u"l_label")
        self.l_label.setGeometry(QRect(91, 227, 53, 37))
        self.l_label.setMinimumSize(QSize(53, 37))
        self.l_label.setMaximumSize(QSize(53, 37))
        self.l_label.setPixmap(QPixmap(u":/pad_l.png"))

        self.r2_label = QLabel(self.gamepad_widget)
        self.r2_label.setObjectName(u"r2_label")
        self.r2_label.setGeometry(QRect(597, 0, 100, 91))
        self.r2_label.setMinimumSize(QSize(100, 91))
        self.r2_label.setMaximumSize(QSize(100, 91))
        self.r2_label.setPixmap(QPixmap(u":/r2.png"))

        self.r1_label = QLabel(self.gamepad_widget)
        self.r1_label.setObjectName(u"r1_label")
        self.r1_label.setGeometry(QRect(598, 94, 99, 22))
        self.r1_label.setMinimumSize(QSize(99, 22))
        self.r1_label.setMaximumSize(QSize(99, 22))
        self.r1_label.setPixmap(QPixmap(u":/r1.png"))
        self.r1_label.setScaledContents(True)

        self.l1_label = QLabel(self.gamepad_widget)
        self.l1_label.setObjectName(u"l1_label")
        self.l1_label.setGeometry(QRect(109, 94, 99, 22))
        self.l1_label.setMinimumSize(QSize(99, 22))
        self.l1_label.setMaximumSize(QSize(99, 22))
        self.l1_label.setPixmap(QPixmap(u":/l1.png"))
        self.l1_label.setScaledContents(True)

        self.start_label = QLabel(self.gamepad_widget)
        self.start_label.setObjectName(u"start_label")
        self.start_label.setGeometry(QRect(551, 141, 28, 47))
        self.start_label.setMinimumSize(QSize(28, 47))
        self.start_label.setMaximumSize(QSize(28, 47))
        self.start_label.setPixmap(QPixmap(u":/strat.png"))
        self.start_label.setScaledContents(True)
        
        self.select_label = QLabel(self.gamepad_widget)
        self.select_label.setObjectName(u"select_label")
        self.select_label.setGeometry(QRect(227, 141, 28, 47))
        self.select_label.setMinimumSize(QSize(28, 47))
        self.select_label.setMaximumSize(QSize(28, 47))
        self.select_label.setPixmap(QPixmap(u":/strat.png"))
        self.select_label.setScaledContents(True)

        self.retranslateUi(Form)
        self.hide_all_labels()

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gp_label.setText("")
        self.l2_label.setText("")
        self.r_analog_label.setText("")
        self.l_analog_label.setText("")
        self.l3_label.setText("")
        self.r3_label.setText("")
        self.x_label.setText("")
        self.squ_label.setText("")
        self.o_label.setText("")
        self.tri_label.setText("")
        self.u_label.setText("")
        self.d_label.setText("")
        self.r_label.setText("")
        self.l_label.setText("")
        self.r2_label.setText("")
        self.r1_label.setText("")
        self.l1_label.setText("")
        self.start_label.setText("")
        self.select_label.setText("")
    # retranslateUi
    def hide_all_labels(self):
        labels = [
            self.l2_label,
            self.l3_label,
            self.r3_label,
            self.x_label,
            self.squ_label,
            self.o_label,
            self.tri_label,
            self.u_label,
            self.d_label,
            self.r_label,
            self.l_label,
            self.r2_label,
            self.r1_label,
            self.l1_label,
            self.start_label,
            self.select_label
        ]
    
        for label in labels:
            label.hide()

