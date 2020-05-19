# https://doc.qt.io/qtforpython/tutorials/basictutorial/clickablebutton.html
import sys
from PyQt5 import QtWidgets, QtCore

def say_hello():
    print("Button clicked, Hello!")

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("click me")

button.clicked.connect(say_hello)

button.show()
app.exec_()