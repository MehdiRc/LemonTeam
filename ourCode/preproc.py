#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:56:50 2017

@author: pitou
"""

from sys import argv

#import numpy as np
from sklearn import decomposition
from sklearn.base import BaseEstimator

import pandas as pd

import data_manager
import numpy as np

from sklearn.ensemble import RandomForestRegressor



'''class that take some information about data'''

class info(object):
    
    
    '''a fonction to count the number of 0
    made for bonus table
    '''
    def count0(self, Data):
        c = 0
        for i in range(len(Data)):
            for j in range(len(Data[i])):
                if Data[i][j]==0.0:
                    c = c+1
        print ("number of 0 =")
        print c
    
    
    '''
    a fonction to check if data don't have error
    if data contain error, it should remove them
    now it don't remove bad data
    '''
    def checkData(self, Data):
       
        for i in range(len(Data)):
            if (np.nan in Data[i,:]): #if we have missing data
                print("ERROR MISSING DATA")
            
            c=0
            for j in range(7): #check age
                c = c + Data[i,j+2]
            
            if (c!=1):
                print("ERROR 2 AGE")
            
            c=0
            for j in range(21): #check job
                c = c + Data[i,j+9]
            if (c!=1):
                print("ERROR JOB")
            
            c=0
            for j in range(2): #check gender
                c = c + Data[i, j+30]
            if (c!=1):
                print("ERROR GENDER")
                
            c=0
            for j in range(18): #check movie
                c = c + Data[i, j+32]
            if (c==0):
                print("ERROR NO MOVIE GENDER")
                
    
    '''
    a fonction to return the accuracyCoef of the result 
    predict, the array of result return by the prediction
    Solution the array of the solution that the prediction must find
    predict and solution must have the same size
    made just to add information
    '''
    def accuracyCoefV1(self, predict, solution):
        count=0
        
        for i in range(len(predict)):
            if (predict[i]==solution[i]):
                count = count + 1                
        
        return count/len(predict)
    
    '''
    same as V1 but more flexible
    '''    
    def accuracyCoefV2(self, predict, solution):
        count=0
        
        for i in range(len(predict)):
            if (predict[i]==solution[i] or predict[i]==solution[i]+1 or predict[i]== solution[i]-1):
                count= count + 1
        return count/len(predict)
    
    '''
    fonction that should returnthe "precision" of the algo
    made to add information
    '''
    def precisionAlgo(self, predict, solution):
        countError=0
        
        for i in range(len(predict)):
            countError = countError + abs(predict[i]-solution[i])
            
        return countError/len(predict)
    
    
'''class to select the most determinant features'''

class PreprocessingFeaturesSelec(BaseEstimator):
    
    '''function to remove a features
    use Data our data
    features: an array composed by nombre of column to remove'''
    def removeFeatures(self, Data, features):
        '''creation of a new array
        add array if he is not in features
        return new array
        it should have in the futurs test in an other function, but we use main tu make test now
        '''
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
but we must change it
'''
class PreprocessingPCA2(BaseEstimator):

    def usePCA(self, Data, nfeatures):
        pca = decomposition.PCA(n_components= nfeatures).fit_transform(Data) 
        return pca
    
    '''
    second fonction for test don't use a number of features
    '''
    def usePCAb(self, Data):
        pca = decomposition.PCA().fit_transform(Data) 
        return pca

    
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
    
    #Prepro = PreprocessingPCA()
 
    # Preprocess on the data and load it back into D
    #D.data['X_train'] = Prepro.fit_transform(D.data['X_train'], D.data['Y_train'])
    #D.data['X_valid'] = Prepro.transform(D.data['X_valid'])
    #D.data['X_test'] = Prepro.transform(D.data['X_test'])
    
    #D.data['X_train']  = Prepro.cleanData(D.data['X_train'])
    
    
    
    #d2 = PreprocessingPCA2().usePCAb(d1)
    #d3 = PreprocessingFeaturesSelec().removeFeatures(d1, [1])
    
    '''D3 = D.loadData("/home/pitou/mini_projet2/starting_kit_project/public_data/movierec_train.solution")
    Y = D3
    dtest = pd.DataFrame(d1)
    dtest.columns=["job_other","job_academic/educator","job_artist","job_clerical/admin","job_college/grad student","job_customer service","job_doctor/health care","job_executive/managerial","job_farmer","job_homemaker","job_K-12 student","job_lawyer","job_programmer","job_retired","job_sales/marketing","job_scientist","job_self-employed","job_technician/engineer","job_tradesman/craftsman","job_unemployed", "job_writer",]
    dtest['class']=Y
    correlations = dtest.corr(method='pearson')'''
    
                             
    d12 = d1[0:100,:]                         
                             
    info().checkData(d12)
                             
    data = d12
    
    t2 = D.loadData("/home/pitou/mini_projet2/starting_kit_project/public_data/movierec_train.solution")
    t= t2[:,0]
    
    
    target = t[0:100] # new array to make test faster
    
    rf = RandomForestRegressor()
    rf.fit(d1, t)
    
    
    test = rf.predict(d1)
    #print rf.predict(data)
    tant = rf.predict(data)
    
    #print (info().accuracyCoefV2(test, t))
    #print (info().precisionAlgo(test, t))


    #print(info().accuracyCoefV2(tant, data))
    #print(info().precisionAlgo(tant, data))                    
    
    r1=info().accuracyCoefV2(test, t)
    r2=info().precisionAlgo(test, t)
    
    # Here show something that proves that the preprocessing worked fine
    print("*** Transformed data ***")
    #print d2
    
    #fusion = info().fusionFeatures(d1)
    
    #info().count0(d1)
    #info().count0(D.data['X_valid'])
    #info().count0(D.data['X_test'])
