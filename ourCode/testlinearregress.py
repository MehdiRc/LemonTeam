# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:37:34 2017

@author: Zeyu YANG


This is the test of my methods.

"""

from numpy import *
import pdb
from linearregress import *
import matplotlib.pyplot as plt
from pylab import *
    

def loadDataSet(fileName):      
    #general function to parse tab -delimited floats
    
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields 
    dataMat = []; labelMat = []
    dataList = []
    fr = open(fileName)
    
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
            
        dataMat.append(lineArr[1:])
        dataList.extend(lineArr[1:])
        labelMat.append(float(curLine[-1]))
        
    return dataMat,labelMat,dataList

    
def loadDataSet_mul(fileName):      
    #general function to parse tab -delimited floats
    
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields 
    print '\nnumFeat=\n',numFeat
    dataMat = []; labelMat = []
    fr = open(fileName)
    
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        #print '\ncurLine:',line
        #print '\n',curLine
        for i in range(numFeat):
            print i
            lineArr.append(float(curLine[i]))
            #print 'lineArr:\n',lineArr
        
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
        
    return dataMat,labelMat

    
def test_singleFeature():
    
    xArray, yArray,xList = loadDataSet('train0.txt')
    testLR = linearRegress()
    
    testLR.regress(xArray, yArray, solver = 'OLS')
    predicted = testLR.predict(xArray,solver = 'OLS')
    predicted_r =  predicted

    testLR.regress(xArray, yArray, solver = 'ridge', **{'lam':0.1})
    predicted_r = testLR.predict(xArray,solver = 'ridge')

    cor = corrcoef(mat(predicted),mat(yArray))

    print 'corrcoef: \n',cor

    figure(1)
    
    subplot(211)  
    plt.scatter(array(yArray), predicted)
    plt.plot([min(yArray),max(yArray)],[min(predicted),max(predicted)],'--k')
    plt.axis('tight')
    plt.xlabel('True value')
    plt.ylabel('Predicted value')

    subplot(212)  
    plt.scatter(array(yArray), predicted_r)
    plt.plot([min(yArray),max(yArray)],[min(yArray),max(yArray)],'--k')
    plt.axis('tight')
    plt.xlabel('True value')
    plt.ylabel('Predicted value')
    
    plt.show()

    figure(2)
    
    subplot(211)  
    plt.scatter(array(xList), array(yArray))
    plt.plot([min(xList),max(xList)],[min(yArray),max(yArray)],'--k')
    plt.axis('tight')
    plt.xlabel('Feature value')
    plt.ylabel('True value')

    subplot(212)  
    plt.scatter(array(xList), array(predicted_r))
    plt.plot([min(xList),max(xList)],[min(predicted_r),max(predicted_r)],'--k')
    plt.axis('tight')
    plt.xlabel('Feature value')
    plt.ylabel('Predicted value')

    plt.show()

    
def rssError(yArr,yHatArr): 
    #yArr and yHatArr both need to be arrays
    
    return ((yArr-yHatArr)**2).sum()

    
def test_multipleFeature():
    xArray, yArray = loadDataSet_mul('train1.txt')
    testLR = linearRegress()
    
    testLR.regress(xArray[0:99], yArray[0:99], solver = 'OLS')
    predicted = testLR.predict(xArray[100:199],solver = 'OLS')
    error_OLS = rssError(array(yArray[100:199]), predicted)
    cor = corrcoef(mat(predicted),mat(yArray[100:199]))
    print 'rss error with OLS', error_OLS
    print 'correlated with OLS', cor
    numTestPts = 30
    
    for i in range(numTestPts):
        testLR.regress(xArray[0:99], yArray[0:99], solver = 'ridge', **{'lam':exp(i-10)})
        predicted_r = testLR.predict(xArray[100:199],solver = 'ridge')
        error_OLS = rssError(array(yArray[100:199]), predicted_r)
        #print 'lam=', i,'\nrss error with ridge: ', error_OLS
        #if i==17:
            #print '\nws\n', testLR.LRDict['ridge'][0]
       # print '\n'
        cor = corrcoef(mat(predicted_r),mat(yArray[100:199]))
        #print 'correlated with ridge: \n',cor
        #print '\n'

    testLR.regress(xArray[0:99], yArray[0:99], solver = 'ridge', **{'lam':1096.63315843})
    predicted_r = testLR.predict(xArray[100:199],solver = 'ridge')

    figure(1)
    
    subplot(211)  
    plt.scatter(array(yArray[100:199]), predicted)
    plt.plot([min(yArray[100:199]),max(yArray[100:199])],[min(predicted),max(predicted)],'--k')
    plt.axis('tight')
    plt.xlabel('True value')
    plt.ylabel('value with OLS')
    
    subplot(212)  
    plt.scatter(array(yArray[100:199]), predicted_r)
    plt.plot([min(yArray[100:199]),max(yArray[100:199])],[min(yArray[100:199]),max(yArray[100:199])],'--k')
    plt.axis('tight')
    plt.xlabel('True value')
    plt.ylabel('value with ridge ')
    
    plt.show()
    

if __name__ == '__main__':
    print '\n---------------'
    print 'Single Feature:'
    print '---------------\n'
    #test_singleFeature()
    print '\n-------------------------'
    print 'End of the Single Feature'
    print '-------------------------\n'
    print '-----------------'
    print 'Multiple Feature:'
    print '-----------------\n'
    test_multipleFeature() 
    print '\n-------------------------'
    print 'End of the Multiple Feature'
    print '-------------------------'