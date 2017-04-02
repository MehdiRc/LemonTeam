#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:22:13 2017

@author: handypedrovalery
"""

from sklearn.base import BaseEstimator
from sklearn import Linear_Model

class Movie(object):
    
    def __init__(self, i, M, g):
        self.id_movie = i
        self.MAR = M
        self.genre = g


class User(object):
    
    def __init__(self, i, gen, a, j, A):
        self.id_user = i;
        self.gender = gen;
        self.age = a;
        self.job = j;
        self.UAR = A;
        self.movies = [];


    def addMovie(self, m):
        self.listMovie.append(m)

        
        
        
        
        
        
        
        
        
        
        
        
class Regressor(BaseEstimator):
    
       
    def __init__(self):
            
        #initialisation and load
        
        self.userList = [];
        self.movieList = [];
        self.auxUserList = [];
        self.auxMovieList = [];

        listJob = ["job_other","job_academic/educator","job_artist","job_clerical/admin",
        "job_college/grad student","job_customer service","job_doctor/health care",
        "job_executive/managerial","job_farmer","job_homemaker","job_K-12 student",
        "job_lawyer","job_programmer","job_retired","job_sales/marketing","job_scientist",
        "job_self-employed","job_technician/engineer","job_tradesman/craftsman",
        "job_unemployed","job_writer"];
        
        listAge = [0,18,25,35,45,50,56];
        
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
    

    def fit(self, X, y):
    
     #X : numpy array or sparse matrix of shape [n_samples,n_features]
     #y : numpy array of shape [n_samples, n_targets]
     #sample_weight : numpy array of shape [n_samples]
     
            self.clf = Linear_model.LinearRegression();
            self.clf.fit(X, y);

    #Similarity beteen two users a and b 
    def similarity(a,b):
        
        self.Data=[];

        fr = open(fileName);
        numFeat = 54;

    for line in fr.readlines():
        curLine = line.strip().split('\t');
        for i in range(numFeat) :
             self.Data.append(curLine[i]);
    return 0;
           
    
    def predict(self,u,m):
        
        numpredict=0;
        sum=0;
        
        for usr in [self.userList]:
            s=similarity(u,usr);
            if u!=usr and m in usr.movies and s>0:
                sum+=s*usr.UAR;
                
            numpredict = sum*i.UAR;
        
    return numpredict/math.abs(sum);

    def preprocDataModif(self, Data):
        
        
          
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
                
            
            

	def predict_proba(self, X):
		return self.clf.predict_proba(X) # The classes are in the order of the labels returned by get_classes

	def get_classes(self):
		return self.clf.classes_

	def save(self, path="./"):
		pickle.dump(self, open(path + '_model.pickle', "w"))

	def load(self, path="./"):
		self = pickle.load(open(path + '_model.pickle'))
		return self

  
  
  
            
    
  
  
  if __name__ == '__main__':
    
    data = loadData('movierec_train.data')
    target = loadSolution('movierec_train.solution')
    test = loadData('movierec_test.data')

    rf = RandomForestRegressor(
                               n_estimators=1)
    rf.fit(data, target)
    
    #rint rf.predict(test)
    print rf.score(data, target)