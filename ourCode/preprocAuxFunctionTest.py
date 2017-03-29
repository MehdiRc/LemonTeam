#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:31:57 2017

@author: pitou
"""

import numpy as np

from sys import argv
from sys import path

path.append('../ourCode')
path.append('../sample_code')

import data_manager
import preprocAuxFunction as paf


''' test use "explorateur de variable" from spyder'''

if __name__ == "__main__":
    
    if len(argv)==1: # Use the default input and output directories if no arguments are provided
          input_dir = "../public_data"
          output_dir = "../res"
    else:
        input_dir = argv[1]
        output_dir = argv[2]
    
    basename = 'movierec'
    D = data_manager.DataManager(basename, input_dir) # Load data
    
    print "debut test 0"
    modele0 = np.array([[0,0,0],[1,0,0],[0,1,1]])
    
    paf.preprocAuxFunction().count0(modele0)
    
    print "fin test 0"
    
    d1 = D.data['X_train']
    
    
    print "test goodDataCheck"
    goodData = d1[:5,:]
    goodDataCheck =  paf.preprocAuxFunction().checkData(goodData)
    print "test badDataCheck in 2 line"
    badData = goodData
    badData[1,4]=1
    badData[2,18]=1
    badDataCheck = paf.preprocAuxFunction().checkData(badData)
    print "fin testCheckData"
    
    print "test accuracyCoefV1"
    tabToFind = np.array([[1],[2],[3]])
    tabFind1 = np.array([[2],[2],[3]])
    
    print paf.preprocAuxFunction().accuracyCoefV1(tabFind1,tabToFind)
    
    print "test accuracyCoefV2"
    print paf.preprocAuxFunction().accuracyCoefV2(tabFind1,tabToFind)
    
    tabFind2 = np.array([[1.5],[2.5],[3.5]])
    print "test precisinoAlgo"
    print paf.preprocAuxFunction().precisionAlgo(tabFind2,tabToFind)
    
    print "fin test"
    
    
