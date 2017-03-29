#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:02:32 2017

@author: pitou
"""

import numpy as np





'''class that take some information about data'''

class preprocAuxFunction(object):
    
    
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
       
        lineToRemove = []     #an array made for save position of error and remove them at the end
        
        for i in range(len(Data)):
            #print i
            if (np.nan in Data[i,:]): #if we have missing data
                if (not i in lineToRemove): lineToRemove.append(i)
                print("ERROR MISSING DATA")
            
            c=0
            for j in range(7): #check age
                #print j
                c = c + Data[i,j+2]
                #print c
            
            if (c!=1):
                if (not i in lineToRemove): lineToRemove.append(i)
                print("ERROR DEUX AGES")
            
            c=0
            for j in range(21): #check job
                c = c + Data[i,j+9]
            if (c!=1):
                if (not i in lineToRemove): lineToRemove.append(i)
                print("ERROR JOB")
            
            c=0
            for j in range(2): #check gender
                c = c + Data[i, j+30]
            if (c!=1):
                if (not i in lineToRemove): lineToRemove.append(i)
                print("ERROR GENDER")
                
            c=0
            for j in range(18): #check movie
                c = c + Data[i, j+32]
            if (c==0):
                if (not i in lineToRemove): lineToRemove.append(i)
                print("ERROR NO MOVIE GENDER")
                    
        newData = np.delete(Data, lineToRemove, axis=0)
        if len(lineToRemove)!=0:
            print lineToRemove
        return newData
                
    
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