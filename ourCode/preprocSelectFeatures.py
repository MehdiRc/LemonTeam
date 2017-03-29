#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:02:00 2017

@author: pitou
"""

from sys import argv
from sys import path

path.append('../ourCode')
path.append('../sample_code')

import numpy as np

from sklearn.base import BaseEstimator

import data_manager



'''class to select the most determinant features'''

class preprocSelectFeatures(BaseEstimator):
    
    '''function to remove features
    use Data our data
    features: an array composed by numbers of column to remove'''
    def removeFeatures(self, Data, features):
        newData = np.delete(Data, features, axis = 1)
        return newData
    
    
    ''' function to select features
    use Data our data
    features: an array composed by the numbers of column to select
    '''
    def selectFeatures(self, Data, features):
        newData = Data[:,features]
        return newData

    '''function to concatenate 2 Data
    data1 first Data
    data2 second Data  
    '''
    def addFeatures(self, Data1, Data2):
        newData = np.column_stack((Data1, Data2))
        return newData
    


if __name__ == "__main__":
    
    if len(argv)==1: # Use the default input and output directories if no arguments are provided
          input_dir = "../public_data"
          output_dir = "../res"
    else:
        input_dir = argv[1]
        output_dir = argv[2]
    
    basename = 'movierec'
    D = data_manager.DataManager(basename, input_dir) # Load data
    print("*** Original data ***")
    print D
    
    d1 = D.data['X_train']
    
    # Here show something that proves that the preprocessing worked fine
    print("*** Transformed data ***")
    #print d2
    
    