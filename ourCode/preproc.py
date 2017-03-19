#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:56:50 2017

@author: pitou
"""

from sys import argv


from sklearn import decomposition
from sklearn.base import BaseEstimator

import numpy as np

PYTHONPATH="../sample_code"
import data_manager

'''class that take some information about data'''

class info():
        
    '''a fonction to count the number of 0'''
    def count0(self, Data):
        c = 0
        for i in range(len(Data)):
            for j in range(len(Data[i])):
                if Data[i][j]==0.0:
                    c = c+1
        print ("number of 0 =")
        print c
    



'''class to select the most determinant features'''

class PreprocessingFeaturesSelec(BaseEstimator):
    
    '''function to remove a features
    use Data our data
    features: an array composed by nombre of column to remove'''
    def removeFeatures(self, Data, features):
        '''
        if the column of the data is in features's array, remove it
        return data without the columns in features
        '''
        
        
        '''buged code'''
        '''if features == []:
            return Data
        newData = np.empty(0)
        c=0
        for i in range(len(Data)):    
            if (not i in features):
                newData = np.append(newData, Data[i][:])
                c = c+1
                print(c)
        return newData'''
        pass

'''
class to transform data using PCA presently inspirate by Isabelle Guyon's code 
'''
class PreprocessingPCA(BaseEstimator):
    
    def __init__(self):
        self.transformer = decomposition.PCA(n_components=52)
    

    def fit(self, X, y=None):
        return self.transformer.fit(X, y)

    def fit_transform(self, X, y=None):
        return self.transformer.fit_transform(X)

    def transform(self, X, y=None):
        return self.transformer.transform(X)
        
'''
a new preprocessing class using also pca but with a different system
'''
class PreprocessingPCA2(BaseEstimator):

    def usePCA(self, Data, nfeatures):
        pca = decomposition.PCA(n_components= nfeatures).fit_transform(Data) 
        return pca
    
    '''
    second fonction for test
    '''
    def usePCAb(self, Data):
        pca = decomposition.PCA().fit_transform(Data) 
        return pca

    
    '''code to make some test about transformation inspirate by Isabelle Guyons code'''
    '''it is use to make some test about the data transformation, the same way will be use
    on a different files when the code were finished, but now it's more useful to do it here
    with the variable explorator of spyder
    '''
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
    
    #Prepro = PreprocessingPCA()
 
    # Preprocess on the data and load it back into D
    #D.data['X_train'] = Prepro.fit_transform(D.data['X_train'], D.data['Y_train'])
    #D.data['X_valid'] = Prepro.transform(D.data['X_valid'])
    #D.data['X_test'] = Prepro.transform(D.data['X_test'])
    #D.data['X_train']  = Prepro.cleanData(D.data['X_train'])
    
    
    
    d2 = PreprocessingPCA2().usePCAb(d1)
    d3 = PreprocessingFeaturesSelec().removeFeatures(d1, [1])
    
    
    # Here show something that proves that the preprocessing worked fine
    print("*** Transformed data ***")
    print d2
    
    info().count0(d1)
    