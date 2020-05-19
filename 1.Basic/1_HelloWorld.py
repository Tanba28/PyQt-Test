# PyQt Tutorial https://doc.qt.io/qtforpython/tutorials/index.html
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello World")
label.show()
app.exec_()