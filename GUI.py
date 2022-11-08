from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import pointcloud_visualizer

class MainWindow(QtWidgets.QMainWindow,pointcloud_visualizer.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

            

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()