# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:56:03 2022

@author: Alessio
"""

import vispy
import vispy.scene
from vispy.scene import visuals




def set_visuals(factor, clas, pos):
    vispy.use('pyqt5')


    canvas = vispy.scene.SceneCanvas(keys='interactive')
    view = canvas.central_widget.add_view()

    pos = pos[::factor]

    colors=[]
    # col = [unknown, ground, vegetation, cars, trucks, powerlines, fences, poles, buildings]
    available_colors = ['darkblue','blue','darkgreen','pink','yellow','lightgreen','lightblue','orange','red']
    for c in clas:
        colors.append(available_colors[c])

    colors = colors[::factor]
        
    scatter = visuals.Markers(alpha = 0.5)
    
    scatter.set_data(pos, edge_color=colors, face_color=colors, size = 5, scaling=True)
    
    view.add(scatter)
    view.camera = 'turntable'
    
    return canvas, pos.shape[0]




