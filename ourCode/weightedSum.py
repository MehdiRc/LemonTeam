from sklearn.base import BaseEstimator
from sklearn.tree import DecisionTreeRegressor

import pickle


listUsers []
lsitMovies[]

class User:
userMovies[]
averageRating

class Movie:
rating

string category


class P(User u, Movie m0):
    
    
    weightSim = 0; #sim(i,N)
    
    for i in rannge (len (listMovies)){
    weightSim +=sim(m0,listMovies[i])
    }
    tempNum=weightSIm * u.averageRating #numerateur
    
    return ((tempNum)/math.abs(tempNum))
    
    
    def r(u,i):
    return 0 #renvoie la note du user pour le fim i
    
    def sim(m0,mn):
        
        size = len(listUsers)
        
        U[] #users distincs that have rated i and j.
        
        for x in rang (size){
            for y in rang (size){
                if(x!=y && Users[x].userMovies.contains(m0,mn)
                   && Users[y].userMovies.contains(m0,mn)){
                   U.append(Users[x],Users[y])
                }
            }
        }

      numerateur=0
      denominateur=0
        
        for i in range (len(U)){
        tempRui+=(r(U[i],m0)-U[i].averageRating)
        tempRuj+=(r(U[i],mn)-U[i].averageRating)
        }
        
        numerateur=tempRui*tempRuj;
        
        denominateur=(math.sqrt(tempRui*tempRui))* (math.sqrt(tempRuj*tempRuj))
            return numerateur/denominateur;

