# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:46:08 2022

@author: Alessio
"""

import laspy
import numpy as np
from scipy.spatial import cKDTree


def get_las_file(path):
    return laspy.read(path)

def write_las_file(las_file, points):
    new_las = laspy.LasData(las_file.header)
    new_las.points = points.copy()
    new_las.write(points+'.las')

def scaled_x_dimension(las_file):
    x_dimension = las_file.X
    scale = las_file.header.scales[0]
    offset = las_file.header.offsets[0]
    return (x_dimension * scale) + offset

def get_coords(las_file):
    return np.vstack((las_file.x, las_file.y, las_file.z)).transpose()

def get_classification(las_file):
    return las_file.classification.array

def compute_euclid_distance(coords, point):
    return np.sqrt(np.sum((coords - point) ** 2, axis=1))

def get_nearest_neighbors(dataset):
    tree = cKDTree(dataset)
    tree.query(dataset[100], k=5)
    
def get_ground_points(las_file):
    return las_file.points[las_file.number_of_returns == las_file.return_number]


