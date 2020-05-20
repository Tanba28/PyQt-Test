import sys
from PyQt5 import QtWidgets, QtCore, QtSerialPort
from ui_terminal import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.menuBarSetup()
        self.monitorTextBoxSetup()

        self.serialPortSetup()

        self.settingsBoxSetup()

    def menuBarSetup(self):
        self.ui.actionQuit.triggered.connect(QtWidgets.qApp.quit)
    
    def monitorTextBoxSetup(self):
        self.ui.monitor.setReadOnly(True)

    def settingsBoxSetup(self):
        self.ui.applyPushButton.clicked.connect(self.serialPortSetting)

        self.serialPortComboBoxSetup()
        self.baudRateComboBoxSetup()

    def serialPortComboBoxSetup(self):
        self.ui.serialPortComboBox.clear()
        self.portInfos = QtSerialPort.QSerialPortInfo.availablePorts()

        for portInfo in self.portInfos:
            self.ui.serialPortComboBox.addItem(portInfo.portName())

    def baudRateComboBoxSetup(self):
        self.ui.baudRateComboBox.clear()
        self.ui.baudRateComboBox.addItem("9600")
        self.ui.baudRateComboBox.addItem("19200")
        self.ui.baudRateComboBox.addItem("38400")
        self.ui.baudRateComboBox.addItem("57600")
        self.ui.baudRateComboBox.addItem("115200")

    def serialPortSetup(self):
        self.serial = QtSerialPort.QSerialPort(self)
        self.serial.readyRead.connect(self.readData)
    
    def serialPortSetting(self):
        self.serial.setPortName(self.ui.serialPortComboBox.currentText())
        if self.serial.open(QtCore.QIODevice.ReadWrite):
            self.serial.setBaudRate(int(self.ui.baudRateComboBox.currentText()))
        else:
            print("Not Connected")            

    def readData(self):
        data = bytes(self.serial.readAll())
        self.ui.monitor.append(data.decode('utf-8'))
    




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())