# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:47:02 2022

@author: aleal
"""
import main
import vispy
from PyQt5.QtWidgets import QApplication, QHBoxLayout,QVBoxLayout,QMainWindow, QLabel, QWidget, QPushButton, QComboBox, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.Vlayout = QVBoxLayout()
        self.hlayout = QHBoxLayout()
        self.container = QWidget()
        self.setWindowTitle('PointCloud')
        
        self.Url = QLabel()
        self.inputLabel = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.Url.setText)
        self.inputLabel.setText("Inserisci l'URL")
        self.renderButton = QPushButton()
        self.pointLabel = QLabel()
        self.pointLabel.setText('Seleziona il fattore di scala')
        self.pointsSelector = QComboBox()
        self.nPoints = 100
        self.canvas = vispy.app.Canvas()
        
        
        self.pointsSelector.addItems(['100','1','10','1000'])
        self.pointsSelector.currentIndexChanged.connect(self.selectionChange)
        
        self.renderButton.setText('Visualizza il file')
        self.renderButton.clicked.connect(self.buttonClick)
        
        
        
        
        self.hlayout.addWidget(self.inputLabel)
        self.hlayout.addWidget(self.pointLabel)
        self.Vlayout.addLayout(self.hlayout)
        
        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.input)
        self.hlayout.addWidget(self.pointsSelector)
        self.hlayout.addWidget(self.renderButton)
        self.Vlayout.addLayout(self.hlayout)
        
        self.Vlayout.addWidget(self.canvas.native)

        
        self.container.setLayout(self.Vlayout)

        self.setCentralWidget(self.container)
        
    def selectionChange(self):
        self.nPoints = int(self.pointsSelector.currentText())
    
    def buttonClick(self):
        self.Vlayout.removeWidget(self.canvas.native)
        self.canvas = main.run(self.Url.text(), self.nPoints)
        self.Vlayout.addWidget(self.canvas.native)
        self.container.setLayout(self.Vlayout)


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
