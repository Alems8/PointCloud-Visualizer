# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:51:31 2022

@author: aleal
"""

import las_computing as las
import ply_computing as ply
import visualization as vis



def run(path, factor):
    coords = None
    file = None
    colors = None
    if (path.endswith(('.las','.laz'))):
        file = las.get_las_file(path)
        coords = las.get_coords(file)
        colors = las.get_classification(file)
    elif(path.endswith('.ply')):
        file = ply.get_file(path)
        coords = ply.get_coord(file)
        colors = ply.get_attribute(file, 'sem_class')
    else:
        print('Wrong file extension')
    
    vis_points = factor*coords.shape[0]
    factor = coords.shape[0] / (coords.shape[0]*factor)
    return int(factor), colors, coords
    # canvas, vis_points  = vis.set_visuals(int(factor), colors, coords)
    
    # return vis_points, coords.shape[0], canvas
    
    
def main():
    path = 'F:/Anaconda/Projects/Thesis/Datset/5080_54435.las'
    factor = 100
    run(path, factor)
    
if __name__ == '__main__':
    main()
