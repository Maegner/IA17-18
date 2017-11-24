import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn import datasets, tree

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

def numberOfVowels(word):
    vowels = ["a","e","i","o","u","á","à","ã","é","è","í","ì","ú","ó","õ"]
    nber = 0
    for letter in word:
        if letter in vowels:
            nber += 1
    return nber

def numberOfConsonants(word):
    consonants = "bcdfghjklmnpqrstvwyxzç"
    nber = 0
    for letter in word:
        if letter in consonants:
            nber += 1
    return nber

def numberOfAccentedLetters(word):
    acc = ["á","à","ã","é","è","í","ì","ú","ó","õ"]
    nber = 0
    for letter in word:
        if letter in acc:
            nber += 1
    return nber

def features(X):
    
    F = np.zeros((len(X),3))
    for x in range(0,len(X)):
        #F[x,3] = len(X[x])
        F[x,1] = numberOfVowels(X[x])
        F[x,0] = numberOfConsonants(X[x])
        F[x,2] = numberOfAccentedLetters(X[x])

    return F     

def mytraining(f,Y):

    #logreg = LogisticRegression()
    #logreg.fit(f,Y) 
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(f,Y)
   
    return knn
    
"""def mytrainingaux(f,Y,par):
    
    return clf"""

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred

