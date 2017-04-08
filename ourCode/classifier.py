from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier
import pickle
from sys import path

path.append('../sample_code')
path.append('../ourCode')
path.append('ourCode/')


import preprocAuxFunction as paf

class Classifier(BaseEstimator):
    def __init__(self):
        print("use RandomForestClassifier")

    def fit(self, X, y):
        X2 = paf.preprocAuxFunction()
        X2 = X2.checkData(X)
        self.clf = RandomForestClassifier()
        self.clf.fit(X2, y)

    def predict(self, X):
        X2 = paf.preprocAuxFunction()
        X2 = X2.checkData(X)
        return self.clf.predict(X2)

    def predict_proba(self, X):
        X2 = paf.preprocAuxFunction()
        X2 = X2.checkData(X)
        return self.clf.predict_proba(X2) # The classes are in the order of the labels returned by get_classes

    def get_classes(self):
        return self.clf.classes_

    def save(self, path="./"):
        pickle.dump(self, open(path + '_model.pickle', "w"))

    def load(self, path="./"):
        self = pickle.load(open(path + '_model.pickle'))
        return self
