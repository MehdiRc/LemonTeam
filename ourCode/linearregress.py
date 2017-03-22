# -*- coding: utf-8 -*-
"""

Created on Sun Mar 12 12:36:48 2017

@author: Zeyu YANG


This is the model of regression part of our program, in this part I realise 2 methods:
    1. OLS(Ordinary Least Square)
    2. Ridge regression

"""

import json
import inspect 
from numpy import *
from copy import *

class linearRegress(object):
    
    def __init__(self,LRDict = None,  **args):
        #currently support OLS, ridge           
        
        obj_list = inspect.stack()[1][-1]
        
        if not LRDict:
            self.LRDict = {}

        else:
            self.LRDict = LRDict
            
        #to Numpy matrix
        if 'OLS' in self.LRDict:
            self.LRDict['OLS'] = mat(self.LRDict['OLS'])
            
        if 'ridge' in self.LRDict:
            self.LRDict['ridge'][0] = mat(self.LRDict['ridge'][0])
            self.LRDict['ridge'][2] = mat(self.LRDict['ridge'][2])
            self.LRDict['ridge'][3] = mat(self.LRDict['ridge'][3])
            self.LRDict['ridge'][4] = mat(self.LRDict['ridge'][4])
        
                
    def object2dict(obj):   
        #convert object to a dict   
        
        d = {'__class__':obj.__class__.__name__, '__module__':obj.__module__}   
        d.update(obj.__dict__)   
        return d
    
        
    def objectDumps2File(obj, jsonfile):
        objDict = object2dict(obj)
        with open(jsonfile, 'w') as f:
            f.write(json.dumps(objDict))
        
            
    def dict2object(d):   
        #convert dict to object, the dict will be changed
        
        if'__class__' in d:   
            class_name = d.pop('__class__')   
            module_name = d.pop('__module__')   
            module = __import__(module_name)   
            class_ = getattr(module,class_name)   
            args = dict((key.encode('ascii'), value) for key, value in d.items()) 
            inst = class_(**args) #create new instance   
            
        else:   
            inst = d   
            
        return inst
    
        
    def objectLoadFromFile(jsonFile):
        #load json file and generate a new object instance whose __name__ filed will be 'inst' 
        
        with open(jsonFile) as f:
            objectDict =json.load(f)
            obj = dict2object(objectDict)
        
        return obj           
                
                
    def solver_OLS(self, xMat, yMat):
        #the method of OLS
        
        x0Mat = mat(ones((xMat.shape[0],1)))
        xMat = hstack((x0Mat, xMat)) #extend x0=1 for each sample
        xTx = xMat.T*xMat
        
        if linalg.det(xTx) == 0.0:
            print "This matrix is singular, cannot do inverse"
            
        else:
            self.LRDict['OLS'] = xTx.I * (xMat.T*yMat)
    
    
    def solver_ridge(self, xMat, yMat, **args):
        #the method of ridge
        
        lam = args['lam']

        yMean = mean(yMat,0)
        yMat = yMat - yMean     #to eliminate X0 take mean off of Y
        
        #regularize X's
        xMeans = mean(xMat,0)   #calc mean then subtract it off
        xVar = var(xMat,0)      #calc variance of X
        xMat = (xMat - xMeans)/xVar

        x0Mat = mat(ones((xMat.shape[0],1)))
        xMat = hstack((x0Mat, xMat))#extend x0=1 for each sample
        xTx = xMat.T*xMat
        
        I = eye(shape(xMat)[1])  #to get the diagonal matrix
        I[0][0] = 0;             #w0 has no punish factor
        denom = xTx + lam*I
        
        if linalg.det(denom) == 0.0:
            print "This matrix is singular, can't do inverse"
           
        else:
            paraList = []
            ws = denom.I * (xMat.T*yMat)
            paraList.append(ws)
            paraList.append(lam)
            paraList.append(xMeans)
            paraList.append(xVar)
            paraList.append(yMean)
            self.LRDict['ridge'] = paraList
        
    def regress(self, xInMat, yInMat, solver = 'OLS', **args):
        ''' create regression model according to solver
            parameters:
              xMat: (m,n) matrix or list, m represents sample count, n represents feature count
              yMat: (m,1) matrix or list, m represents sample count
              **args represents additional parameters of solver, such as lambda of ridge slover
        '''
        
        xMat = mat(xInMat)
        yMat = mat(yInMat).T

        if solver == 'OLS':
            self.solver_OLS(xMat, yMat)
            
        elif solver == 'ridge':
            self.solver_ridge(xMat, yMat, **args)
            
        else:
            print '%s solver not support'%solver

            
    def __predict(self, x2predict, ws):
        #the matrix calculation part of prediction
        
        tmpX = mat(x2predict)
        x0Mat = mat(ones((tmpX.shape[0],1)))
        xMat =  hstack((x0Mat, tmpX))#extend x0=1 for each testvector
        return (mat(xMat)*ws).T.getA()[0]#return predict array
     

    def predict(self, x2predict, solver = 'OLS'):
        #the calculation part of prediction
        
        x2predict = mat(x2predict)
        
        if solver == 'OLS':
            ws = self.LRDict['OLS']
            return self.__predict(x2predict, ws)
            
        elif solver == 'ridge':
            ws = self.LRDict['ridge'][0]
            xMean = self.LRDict['ridge'][2]
            xVar = self.LRDict['ridge'][3]
            x2predict = (x2predict - xMean)/xVar
            yMean = self.LRDict['ridge'][4]
            return self.__predict(x2predict, ws)+yMean.getA()[0].tolist()[0]
        
        else:
            print '%s solver not support'%solver
            return None
          

if __name__ == "__main__":
    pass
 
    
