import sys

import argparse
import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,widget):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("Eartquakes information")
        self.setCentralWidget(widget)

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        exit_action = QtWidgets.QAction("Exit",self)
        exit_action.setShortcut(QtGui.QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")

        geometry = QtWidgets.qApp.desktop().availableGeometry(self)
        self.setFixedSize(int(geometry.width() * 0.5),int(geometry.height() * 0.5))

class CustomTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=None):
        QtCore.QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self,data):
        self.input_dates = data[0].values
        self.input_magnitudes = data[1].values

        self.column_count = 2
        self.row_count = len(self.input_magnitudes)

    def rowCount(self,parent=QtCore.QModelIndex()):
        return self.row_count

    def columnCount(self,parent=QtCore.QModelIndex()):
        return self.column_count

    def headerData(self,section,orientation,role):
        if role != QtCore.Qt.DisplayRole:
            return None
        if orientation == QtCore.Qt.Horizontal:
            return ("Data", "Magnituide")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                raw_date = self.input_dates[row]
                date = "{}".format(raw_date.toPyDateTime())
                return date[:-3]
            elif column == 1:
                return "{:.2f}".format(self.input_magnitudes[row])
        elif role == QtCore.Qt.BackgroundRole:
            return QtGui.QColor(QtCore.Qt.white)
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignRight

        return None


class Widget(QtWidgets.QWidget):
    def __init__(self,data):
        QtWidgets.QWidget.__init__(self)

        self.model = CustomTableModel(data)

        self.table_view = QtWidgets.QTableView()
        self.table_view.setModel(self.model)

        self.horizontal_header = self.table_view.horizontalHeader()
        self.vertical_header = self.table_view.verticalHeader()
        self.vertical_header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setStretchLastSection(True)

        self.main_layout = QtWidgets.QHBoxLayout()
        size = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        size.setHorizontalStretch(1)
        self.table_view.setSizePolicy(size)
        self.main_layout.addWidget(self.table_view)

        self.setLayout(self.main_layout)

def transform_date(utc,timezone=None):
    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QtCore.QDateTime().fromString(utc,utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date

def read_data(frame):
    df = pd.read_csv(frame)

    df = df.drop(df[df.mag < 0].index)
    magnitudes = df["mag"]

    timezone = QtCore.QTimeZone(b"Europe/Berlin")

    times = df["time"].apply(lambda x: transform_date(x,timezone))

    return times,magnitudes

if __name__ == '__main__':
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)

    app = QtWidgets.QApplication(sys.argv)

    widget = Widget(data)
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec_())