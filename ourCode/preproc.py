#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:56:50 2017

@author: pitou
"""

from sys import argv

from sklearn import decomposition
from sklearn.base import BaseEstimator

from sys import path

path.append('../ourCode')
path.append('../sample_code')

import data_manager

import numpy as np
import preprocAuxFunction as paf

class preprocessingPCA(BaseEstimator):
    
    '''def __init__(self, Data ,nfeatures):
        self.transformer = decomposition.PCA(n_components = nfeatures).fit_transform(self.checkData(Data))
    '''
    
    def checkData(self,Data):
        return paf.preprocAuxFunction().checkData(Data)
    
    def applyPCA(self, Data, nfeatures):
        return decomposition.PCA(n_components = nfeatures).fit_transform(self.checkData(Data))

    
    '''code to make some test about transformation inspirate by Isabelle Guyons code'''
if __name__ == "__main__":
    
    if len(argv)==1: # Use the default input and output directories if no arguments are provided
          input_dir = "../public_data"
          output_dir = "../res"
    else:
        input_dir = argv[1]
        output_dir = argv[2]
    
    basename = 'movierec'
    D = data_manager.DataManager(basename, input_dir) # Load data
    #D2 = D.loadData("/home/pitou/mini_projet2/starting_kit_project/public_data/movierec_train.data")
    print("*** Original data ***")
    print D
    
    d1 = D.data['X_train']
    
    # Here show something that proves that the preprocessing worked fine
    print("*** Transformed data ***")
    #print d2
    
    
    
    #regarder np.histogramme pour faire du binage des id, et MPA pour les boolean
