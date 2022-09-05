# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:56:03 2022

@author: Alessio
"""

import laspy
import vispy
import vispy.scene
from vispy.scene import visuals
from vispy import app
import numpy as np
import sys



def set_visuals(factor, clas, pos):
    vispy.use('pyqt5')


    canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
    view = canvas.central_widget.add_view()

    # las_file = laspy.read('F:/Anaconda/Projects/Thesis/Datset/5080_54435.las')

    # points = np.vstack((las_file.x, las_file.y, las_file.z)).transpose()
    # factor=100
    pos = pos[::factor]

    
    # clas = las_file.classification.array
    colors=[]
    # col = [unknown, ground, vegetation, cars, trucks, powerlines, fences, poles, buildings]
    available_colors = ['darkblue','blue','darkgreen','pink','yellow','lightgreen','lightblue','orange','red']
    for c in clas:
        colors.append(available_colors[c])

    # intensity = las_file.intensity
    # print(np.amax(intensity))
    colors = colors[::factor]
    # intensity = intensity[::factor]
        
    scatter = visuals.Markers()
    scatter.set_data(pos, edge_color=colors, face_color=colors)
    view.add(scatter)
    view.camera = 'turntable'
    
    if sys.flags.interactive != 1:
        app.run()



# if __name__ == '__main__':
#     import sys
#     if sys.flags.interactive != 1:
#         app.run()


