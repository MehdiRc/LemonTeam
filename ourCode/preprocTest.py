#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:50:50 2017

@author: pitou
"""
from sys import argv
from sys import path
path.append('../ourCode')
path.append('../sample_code')

import data_manager
import preproc



if __name__ == "__main__":
    
    if len(argv)==1: # Use the default input and output directories if no arguments are provided
          input_dir = "../public_data"
          output_dir = "../res"
    else:
        input_dir = argv[1]
        output_dir = argv[2]
        
        
    basename = 'movierec'
    Data = data_manager.DataManager(basename, input_dir) # Load data
    d1 = Data.data['X_train']
    testPCA = preproc.preprocessingPCA().applyPCA(d1, 54)
    
    print testPCA[:4,:4]