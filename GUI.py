# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:47:02 2022

@author: aleal
"""
import main
import PyQt5
import vispy
from PyQt5.QtWidgets import (QApplication, QHBoxLayout,QVBoxLayout,QMainWindow, 
                    QLabel, QWidget, QPushButton, QComboBox, QLineEdit,QFileDialog,
                    QMessageBox, QGridLayout, QProgressBar, QSlider)
StyleSheet = '''
#ProgressBar {
    min-height: 12px;
    max-height: 12px;
    border-radius: 6px;
}
'''

# class Worker(QRunnable):
#     def __init__(self):
#         super().__init__()
        
#         self.threadpool = QThreadPool()
        
#         def run(self):
            


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.Vlayout = QVBoxLayout()
        self.hlayout = QHBoxLayout()
        self.grid = QGridLayout()
        self.container = QWidget()
        self.setWindowTitle('PointCloud')
        
        self.Url = ''
        self.fileButton = QPushButton()

        self.renderButton = QPushButton()
        
        self.pointLabel = QLabel()
        self.pointLabel.setText('Seleziona la percentuale dei punti da visualizzare')
        self.pointLabel.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Maximum, PyQt5.QtWidgets.QSizePolicy.Fixed)
        self.pointsSelector = QSlider(PyQt5.QtCore.Qt.Horizontal)
        self.nPoints = 0.08
        self.totalPoints = None
        self.vis_points = None
        
        self.canvas = vispy.app.Canvas()
        self.canvas.native.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Expanding, PyQt5.QtWidgets.QSizePolicy.Expanding)

        
        self.fileButton.setText('Seleziona il file da visualizzare')
        self.fileButton.clicked.connect(self.fileOpening)
        self.fileButton.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Maximum, PyQt5.QtWidgets.QSizePolicy.Fixed)
        
        # self.pointsSelector.addItems(['100','1','10','1000'])
        self.pointsSelector.setRange(0,100)
        self.pointsSelector.setValue(80)
        self.pointsSelector.setTickPosition(QSlider.TicksAbove)
        self.pointsSelector.setTickInterval(10)
        self.pointsSelector.setSingleStep(1)
        self.pointsSelector.valueChanged[int].connect(self.selectionChange)
        self.pointsSelector.setStyleSheet('''
                                          QSlider::groove:horizontal {
                                              border: 1px solid #999999;
                                              height: 8px; 
                                              background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
                                              margin: 2px 0;
                                             }

                                         QSlider::handle:horizontal {
                                             background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
                                             border: 1px solid #5c5c5c;
                                             width: 18px;
                                             margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
                                             border-radius: 3px;
                                        }
                                        ''')
        # self.pointsSelector.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Maximum, PyQt5.QtWidgets.QSizePolicy.Fixed)

        
        self.renderButton.setText('Visualizza il file')
        self.renderButton.clicked.connect(self.setStatus)
        self.renderButton.clicked.connect(self.setCanvas)

        self.renderButton.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Maximum, PyQt5.QtWidgets.QSizePolicy.Fixed)
        self.pLabel = ''
        self.statusbar = self.statusBar()

        
        
        
        self.hlayout.addWidget(self.fileButton)
        
        self.hlayout.addWidget(self.pointLabel)
        
        self.hlayout.addWidget(self.renderButton)

        self.Vlayout.addLayout(self.hlayout)

        
        self.hlayout = QHBoxLayout()

        self.hlayout.addWidget(self.pointsSelector)

        
        self.Vlayout.addLayout(self.hlayout)
        
        
        
        self.Vlayout.addWidget(self.canvas.native)


        
        self.container.setLayout(self.Vlayout)

        self.setCentralWidget(self.container)
        
        self.showMaximized()

    def fileOpening(self):
        self.Url, _filter = QFileDialog.getOpenFileName(self,'Seleziona il file', None,'Point Cloud files (*.las *.laz *.ply)')
        
    def selectionChange(self, value):
        self.nPoints = value/1000
        if(self.nPoints < 0.05):
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setText('Stai selezionando un valore inferirore al 50%, la rappresentazione non sarà accurata')
            msg.setIcon(QMessageBox().Warning)
            msg.exec_()    
    
    def setCanvas(self):
        if self.Url != '':
            self.Vlayout.removeWidget(self.canvas.native)
            self.vis_points, self.totalPoints, self.canvas = main.run(self.Url, self.nPoints)
            self.Vlayout.addWidget(self.canvas.native)
            self.container.setLayout(self.Vlayout)
            
            self.statusbar.removeWidget(self.progressBar)
            self.pLabel = QLabel(f'Sono visibili {self.vis_points} / {self.totalPoints} punti')
            self.statusbar.addPermanentWidget(self.pLabel)
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Errore')
            msg.setText('Nessun file è stato selezionato!')
            msg.setIcon(QMessageBox().Critical)
            msg.exec_()
    
    def setStatus(self):
        if(self.pLabel != ''):
            self.statusbar.removeWidget(self.pLabel)
        else:
            self.statusbar.addPermanentWidget
        self.progressBar = QProgressBar()
        self.progressBar.setObjectName('ProgressBar')
        self.progressBar.setStyleSheet(StyleSheet)
        self.progressBar.setMaximum(0)
        self.progressBar.setMinimum(0)
        self.statusbar.addPermanentWidget(self.progressBar)
        self.update()


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
