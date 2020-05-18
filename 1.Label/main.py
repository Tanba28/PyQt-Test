# - * - coding: utf8 - * -

import sys

from PyQt5 import QtWidgets, QtGui, QtCore

class MyWindow(QtWidgets.QWidget): # QWidgetクラスを使用します。

    def __init__(self):
        super().__init__()
        self.title = 'Hello World'
        self.width = 300
        self.height = 200
        self.word = "Hello World!"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(500, 500, self.width, self.height)

        label = QtWidgets.QLabel(self)

        label.setText(self.word)
    
        label.setGeometry(75,50,150,100)

        label.setAlignment(QtCore.Qt.AlignCenter)
        
        label.setStyleSheet("QLabel { background-color : black; color : white;}")

        label.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MyWindow()



    sys.exit(app.exec_())


if __name__ == "__main__":
    main()