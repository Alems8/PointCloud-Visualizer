# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:47:02 2022

@author: aleal
"""

from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel('Hello World!')
label.show()
app.exec()
