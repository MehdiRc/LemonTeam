#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:13:44 2017

@author: pitou
"""

from sys import argv
from sys import path

path.append('../ourCode')
path.append('../sample_code')

import data_manager
import preprocDataModif as pdm













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
    
    d1 = D.data['X_train']
    d12 = d1[0:100,:] #100 pour que se soit plus simple, il y a 98 users dedans
    
    
    DataModifiee=pdm.preprocDataModif()
    
    
    DataModifiee.preprocDataModif(d12) # application de la modification
    
    print "vérification si les films sont bien ajouter dasn l'user"
    DataModifiee.checkM()
    print "fin de vérification"
    
    Listefilm=DataModifiee.auxMovieList
    listeUser=DataModifiee.auxUserList
    print "les 2 premiers film de la liste movie"
    print DataModifiee.movieList[0].id_movie
    print DataModifiee.movieList[1].id_movie
    
    # Here show something that proves that the preprocessing worked fine
    print("*** Transformed data ***")