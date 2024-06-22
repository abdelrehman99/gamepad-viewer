import sys

from PySide6 import QtWidgets
from widget import Widget

app = QtWidgets.QApplication(sys.argv)

window = Widget()
window.show()

window.capturing(0,0)

app.exec()