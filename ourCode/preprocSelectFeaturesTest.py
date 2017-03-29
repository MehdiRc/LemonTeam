#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:16:46 2017

@author: pitou
"""
from sys import argv
from sys import path

path.append('../ourCode')
path.append('../sample_code')

import data_manager
import preprocSelectFeatures






'''test use "explorateur de variable" from spyder'''

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
    
    testFeaturesRemove= preprocSelectFeatures.preprocSelectFeatures().removeFeatures(d1, [0,1]) 
    testFeaturesSelect = preprocSelectFeatures.preprocSelectFeatures().selectFeatures(d1, [0,1])
    testAddData = preprocSelectFeatures.preprocSelectFeatures().addFeatures(d1, d1)
    
    
    
    # Here show something that proves that the preprocessing worked fine
    print("*** Transformed data ***")
    #print d2