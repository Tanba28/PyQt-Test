# https://doc.qt.io/qtforpython/tutorials/basictutorial/dialog.html

import sys
from PyQt5 import QtWidgets, QtCore

class Form(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(Form,self).__init__(parent)
        self.setWindowTitle("My Form")

        self.edit = QtWidgets.QLineEdit("Write My Name Here")
        self.button = QtWidgets.QPushButton("Show Greetings")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print("Hello %s" % self.edit.text())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec_())