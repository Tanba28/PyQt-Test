# https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html

import sys
from PyQt5 import QtWidgets, QtCore
from ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.statusBarSetup()

    def statusBarSetup(self):
        self.ui.actionQuit.triggered.connect.(QtWidgets.qApp.quit)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())