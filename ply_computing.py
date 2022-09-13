# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:24:16 2022

@author: aleal
"""
from plyfile import PlyData
import numpy as np


def get_file(path):
    return PlyData.read(path)

def get_coord(file):
    return np.vstack((file.elements[0].data['x'],
                     file.elements[0].data['y'],
                     file.elements[0].data['z'])).transpose()

def get_attribute(file, attribute):
    return file.elements[0].data[attribute]