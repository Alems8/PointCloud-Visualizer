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
    #This class contains all the methods needed to interact with the DataFrame and create or update the canvas to be rendered.
    def __init__(self):
        self.df = None
        self.density = 0.4
        self.alpha = 0.5
        self.size = 5
        self.available_colors = ['darkblue','blue','darkgreen','pink','yellow','lightgreen','lightblue','orange','red']
        self.classes = None
        self.hiddenClasses = []
    
    def getDf(self):
        #Return the full dataframe
        return self.df
    def setDf(self,dfp):
        #Get the new DataFrame from the file loaded and change its columns to have the colors associated with the classes and the class predicted per row.
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
        #Return the name of the classes of the point cloud
        return self.classes
    def getColor(self,i):
        #Return the list of the colors 
        return self.available_colors[i]
    def getAccuracy(self, i):
        #Return the accuracy score computed for the class i
        return round(accuracy_score(self.df[self.df['index']==i]['GT'],self.df[self.df['index']==i]['index']),2)
    def getPoints(self, i):
        #Return the number of points for the class i
        return self.reducedDf['index'].value_counts()[i] if self.reducedDf['index'].value_counts().__contains__(i) > 0 else 0
    def setDensity(self,dens):
        #Set the value of the density
        self.density = dens/100
    def setAlpha(self,a):
        #Set the value of alpha
        self.alpha = a/100
    def setSize(self,s):
        #Set the value of the size of the points
        self.size = s/10
    def setData(self):
        #Create a new scatter based on a reduced version of the original DataFrame
        vispy.use('pyqt5')
        self.reducedDf = self.df.sample(frac = self.density)
            
        self.scatter = visuals.Markers()
        self.scatter.alpha = self.alpha
        self.scatter.set_data(self.reducedDf.iloc[:,0:3].values, edge_color=self.reducedDf['colors'].values.tolist(), face_color=self.reducedDf['colors'].values.tolist(), size = self.size, scaling=True)
    
        return self.scatter
    
    def updateD(self,scatter):
        #Update the scatter and check if the list of hidden classes has been updated
        self.reducedDf = self.df.sample(frac = self.density)
        if (len(self.hiddenClasses) > 0):
            for hc in self.hiddenClasses:
                self.reducedDf = self.reducedDf.loc[self.df['index'] != hc]
        scatter.set_data(self.reducedDf.iloc[:,0:3].values, edge_color=self.reducedDf['colors'].values.tolist(), face_color=self.reducedDf['colors'].values.tolist(), size = self.size, scaling=True)
    
    def updateA(self,scatter):
        #Update the value of alpha for the scatter
        scatter.alpha = self.alpha
    def setClass(self,className):
        #Update the list of hidden classes adding the class if it's not in the list or removing if it's already in the list
        if(self.hiddenClasses.count(self.classes.index(className)) > 0):
            self.hiddenClasses.remove(self.classes.index(className))
        else:
            self.hiddenClasses.append(self.classes.index(className))







