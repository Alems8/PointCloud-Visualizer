# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:10:10 2022

@author: aleal
"""


import pandas as pd
import numpy as np
import vispy
import vispy.scene
from vispy.scene import visuals
from sklearn.metrics import accuracy_score



class DataFrame():
    def __init__(self):
        self.df = None
        self.density = 0.4
        self.alpha = 0.5
        self.size = 5
        self.available_colors = ['darkblue','blue','darkgreen','pink','yellow','lightgreen','lightblue','orange','red']
        self.classes = None
        self.hiddenClasses = []
    
    def getDf(self):
        return self.df
    def setDf(self,dfp):
        self.df = pd.read_pickle(dfp)
        self.classes = list(self.df.iloc[0:0,3:-1].columns.values)
        indexes = []
        colors = []
        mask = [row>0.5 for row in self.df[self.classes].to_numpy()]
        for i in range(len(mask)):
            index, = np.where(mask[i] == True)
            colors.append(self.available_colors[index[0]])
            indexes.append(index[0])
        self.df.drop(self.classes, axis=1,inplace=True)
        self.df['colors'] = colors
        self.df['index'] = indexes
    def getClasses(self):
        return self.classes
    def getColor(self,i):
        return self.available_colors[i]
    def getAccuracy(self, i):
        return round(accuracy_score(self.df[self.df['index']==i]['GT'],self.df[self.df['index']==i]['index']),2)
    def getPoints(self, i):
        return self.reducedDf['index'].value_counts()[i] if self.reducedDf['index'].value_counts().__contains__(i) > 0 else 0
    def setDensity(self,dens):
        self.density = dens/100
    def setAlpha(self,a):
        self.alpha = a/100
    def setSize(self,s):
        self.size = s/10
    def setData(self):
        vispy.use('pyqt5')
        self.reducedDf = self.df.sample(frac = self.density)
            
        self.scatter = visuals.Markers()
        self.scatter.alpha = self.alpha
        self.scatter.set_data(self.reducedDf.iloc[:,0:3].values, edge_color=self.reducedDf['colors'].values.tolist(), face_color=self.reducedDf['colors'].values.tolist(), size = self.size, scaling=True)
    
        return self.scatter
    
    def updateD(self,scatter):
        self.reducedDf = self.df.sample(frac = self.density)
        if (len(self.hiddenClasses) > 0):
            for hc in self.hiddenClasses:
                self.reducedDf = self.reducedDf.loc[self.df['index'] != hc]
        scatter.set_data(self.reducedDf.iloc[:,0:3].values, edge_color=self.reducedDf['colors'].values.tolist(), face_color=self.reducedDf['colors'].values.tolist(), size = self.size, scaling=True)
    
    def updateA(self,scatter):
        scatter.alpha = self.alpha
    def setClass(self,className):
        if(self.hiddenClasses.count(self.classes.index(className)) > 0):
            self.hiddenClasses.remove(self.classes.index(className))
        else:
            self.hiddenClasses.append(self.classes.index(className))







