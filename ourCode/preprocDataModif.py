#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:27:06 2017

@author: pitou
"""
from sys import argv

from sklearn.base import BaseEstimator

import numpy as np
import data_manager




class Movie(object):
    
    '''
    constructor of movie
    @param i, id's film
    @param M, the Movie_average_rating
    @param g, an array corresponding of boolean data of the movie
    '''
    
    def __init__(self, i, M, g):
        self.id_movie = i
        self.MAR = M
        self.genre = g


class User(object):
    
    '''
    user's constructor
    @param i user id
    @param gen a char corresponding to the gender of the user
    @param a the low level age of the user
    @param j a String corresponding to the user's job
    @param A a float corresponding to user_average_rating
    '''
    def __init__(self, i, gen, a, j, A):
        self.id_user = i
        self.gender = gen
        self.age = a
        self.job = j
        self.UAR = A
        self.listMovie = []

    '''
    method to add a moovie in user list
    @param m un movie
    '''
    def addMovie(self, m):
        self.listMovie.append(m)
   

     
class preprocDataModif(BaseEstimator):
    
    
    '''
    constructor of DataModif
    '''
    def __init__(self):
        self.userList = []
        self.movieList = []
        self.auxUserList = []
        self.auxMovieList = []
    
        
    '''method to change data's form
    @param Data, the data
    this method create the different data in this object
    '''    
    def preprocDataModif(self, Data):
        
        listJob = ["job_other","job_academic/educator","job_artist","job_clerical/admin","job_college/grad student","job_customer service","job_doctor/health care","job_executive/managerial","job_farmer","job_homemaker","job_K-12 student","job_lawyer","job_programmer","job_retired","job_sales/marketing","job_scientist","job_self-employed","job_technician/engineer","job_tradesman/craftsman","job_unemployed", "job_writer",]
        listAge = [0,18,25,35,45,50,56]
        
        
        for i in range(len(Data)):
            if (not Data[i][0] in self.auxUserList):
                self.auxUserList.append(Data[i,0]) #auxilary list with user id
                
                if (Data[i,30]==1):
                    gen='M'
                else:
                    gen='F'
                
                for j in range(7):
                    
                    if (Data[i,j+2]==1):
                        age=listAge[j]
                        break
                    if j==6:
                        print("ERROR AGE")
                
                
                for j in range(21):
                    if (Data[i,j+9]==1):
                        job=listJob[j]
                        break
                    if j==20:
                        print("ERROR JOB")
                
                uar=Data[i,51]
                id_per = Data[i,0]
                id_film = Data[i,1]
                mar=Data[i,52]
                          
                genrefilm = Data[i, 32:49]
                
                leFilm=Movie(id_film, mar, genrefilm)
                leUser=User(id_per, gen, age, job, uar)
                leUser.addMovie(leFilm)
                self.userList.append(leUser)
                
                
            else:
                ind = self.auxUserList.index(Data[i][0])
                
                genrefilm = Data[i, 32:49]
                mar=Data[i,52]
                genrefilm = Data[i, 32:49]
                leFilm=Movie(id_film, mar, genrefilm)
                
                self.userList[ind].addMovie(leFilm)
            
            if  (not Data[i][1] in self.auxMovieList):
                self.auxMovieList.append(Data[i,1]) #auxilary list with movie id
            
                id_film = Data[i,1]
                mar = Data[i,52]
                genrefilm = Data[i, 32:49]
                leFilm = Movie(id_film, mar, genrefilm)
                self.movieList.append(leFilm)
            '''print(self.userList[0].id_user) #test
            print(self.userList[0].gender)
            print(self.userList[0].age)
            print(self.userList[0].job)
            print(self.userList[0].UAR)
            
            print(self.userList[0].listMovie[0].id_movie)
            print(self.userList[0].listMovie[0].MAR)
            print(self.userList[0].listMovie[0].genre)'''
        '''print(len(self.userList))
        print(self.userList[1].id_user)
        print(self.userList[2].id_user)
        print(self.userList[3].id_user)
        print(self.userList[4].id_user)'''
                
    def checkM(self): #fonction de test
        c=0
        m=0
        for i in range(len(self.auxUserList)):
            if len(self.userList[i].listMovie)>1:
                c=1
                m=i
        if c==0:
            print("PROB AJOUT MOOVIE")
        else:
            print("no prob")
        for i in range(len(self.userList[m].listMovie)):
            print (self.userList[m].listMovie[i].id_movie)
                
            
    
        
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
    

    
