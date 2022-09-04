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



vispy.use('pyqt5')


canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()

las_file = laspy.read('F:/Anaconda/Projects/Thesis/Datset/5080_54435.las')

points = np.vstack((las_file.x, las_file.y, las_file.z)).transpose()
factor=100
pos = points[::factor]

    
clas = las_file.classification.array
colors=[]
# col = [white, ground, vegetation, cars, trucks, powerlines, fences, poles, buildings]
col = ['white','grey','green','red','blue','yellow','brown','pink','purple']
for c in clas:
    colors.append(col[c])

colors = colors[::factor]
scatter = visuals.Markers()
scatter.set_data(pos, edge_color=colors, face_color=colors )
view.add(scatter)
view.camera = 'turntable'

axis = visuals.XYZAxis(parent=view.scene)


if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1:
        app.run()


