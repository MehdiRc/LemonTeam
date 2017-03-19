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


import data_manager
import numpy as np


'''class that take some information about data'''

class info():
    
    '''fonction qui doit retourner la moyenne note/age
    '''
    def moyNoteAge(self, Data):
        pass
    '''fonction qui doit retourner la moyenne note/sev?
    '''
    def moyNoteSev(self, Data):
        pass
    '''fonction qui doit retourner la moyenne note/occupation
    '''
    def moyNoteOccupation(self, data):
        job_other = np.array(data[data["job_other"]==1])
        job_academicOreducator = np.array(data[data["job_academic/educator"]==1])
        job_artist = np.array(data[data["job_artist"]==1])
        job_clericalOradmin = np.array(data[data["job_clerical/admin"]==1])
        job_collegeOrgrad_student = np.array(data[data["job_college/grad student"]==1])
        job_customer_service = np.array(data[data["job_customer_service"]==1])
        job_doctorOrhealth_care = np.array(data[data["job_doctor/health care"]==1])
        job_executiveOrmanagerial = np.array(data[data["job_executive/managerial"]==1])
        job_farmer = np.array(data[data["job_farmer"]==1])
        job_homemaker = np.array(data[data["job_homemaker"]==1])
        job_K12_student = np.array(data[data["job_K-12 student"]==1])
        job_lawyer = np.array(data[data["job_lawyer"]==1])
        job_programmer = np.array(data[data["job_programmer"]==1])
        job_retired = np.array(data[data["job_retired"]==1])
        job_salesOrmarketing = np.array(data[data["job_sales/marketing"]==1])
        job_scientist = np.array(data[data["job_scientist"]==1])
        job_self_employed = np.array(data[data["job_self-employed"]==1])
        job_technicianOrengineer = np.array(data[data["job_technician/engineer"]==1])
        job_tradesmanOrcraftsman = np.array(data[data["job_tradesman/craftsman"]==1])
        job_unemployed = np.array(data[data["job_unemployed"]==1])
        job_writer = np.array(data[data["job_writer"]==1])
        
        
        avergaejob_other=np.mean(job_other[:,-1])
        avergaejob_academicOreducator=np.mean(job_academicOreducator[:,-1])
        avergaejob_artist=np.mean(job_artist[:,-1])
        avergaejob_clericalOradmin=np.mean(job_clericalOradmin[:,-1])
        avergaejob_collegeOrgrad_student=np.mean(job_collegeOrgrad_student[:,-1])
        avergaejob_customer_service=np.mean(job_customer_service[:,-1])
        avergaejob_doctorOrhealth_care=np.mean(job_doctorOrhealth_care[:,-1])
        avergaejob_executiveOrmanagerial=np.mean(job_executiveOrmanagerial[:,-1])
        avergaejob_farmer=np.mean(job_farmer[:,-1])
        avergaejob_homemaker=np.mean(job_homemaker[:,-1])
        avergaejob_K12_student=np.mean(job_K12_student[:,-1])
        avergaejob_lawyer=np.mean(job_lawyer[:,-1])
        avergaejob_programmer=np.mean(job_programmer[:,-1])
        avergaejob_retired=np.mean(job_retired[:,-1])
        avergaejob_salesOrmarketing=np.mean(job_salesOrmarketing[:,-1])
        avergaejob_scientist=np.mean(job_scientist[:,-1])
        avergaejob_self_employed=np.mean(job_self_employed[:,-1])
        avergaejob_technicianOrengineer=np.mean(job_technicianOrengineer[:,-1])
        avergaejob_tradesmanOrcraftsman=np.mean(job_tradesmanOrcraftsman[:,-1])
        avergaejob_unemployed=np.mean(job_unemployed[:,-1])
        avergaejob_writer=np.mean(job_writer[:,-1])
        
        
        averagesByJob=np.array([avergaejob_other,avergaejob_academicOreducator,avergaejob_artist,avergaejob_clericalOradmin,avergaejob_collegeOrgrad_student,avergaejob_customer_service,avergaejob_doctorOrhealth_care,avergaejob_executiveOrmanagerial,avergaejob_farmer,avergaejob_homemaker,avergaejob_K12_student,avergaejob_lawyer,avergaejob_programmer,avergaejob_retired,avergaejob_salesOrmarketing,avergaejob_scientist,avergaejob_self_employed,avergaejob_technicianOrengineer,avergaejob_tradesmanOrcraftsman,avergaejob_unemployed,avergaejob_writer])
        
        return averagesByJob
        
    '''fonction qui doit retourner la moyenne note/genremoovie
    '''
    def moyNoteGenreM(self, Data):
        pass
        
    '''fonction devant retourner je pense sous forme d'un tableau 2d les coeficients de correlations de chaque features
    '''
    def coefcor(self, Data):
        pass
        
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
        if features == []:
            return Data
        newData = np.empty(0)
        c=0
        for i in range(len(Data)):    
            if (not i in features):
                newData = np.append(newData, Data[i][:])
                c = c+1
                print(c)
        return newData







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
    d3 = PreprocessingFeaturesSelec().removeFeatures(d1, [1])
    
    
    # Here show something that proves that the preprocessing worked fine
    print("*** Transformed data ***")
    #print d2
    
    #info().count0(d1)
    