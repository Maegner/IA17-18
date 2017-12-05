import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn import datasets, tree

from sklearn.tree import DecisionTreeClassifier

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

def letterSum(word):
    result = 0
    for letter in word:
        result += ord(letter)
    return result

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

def palindrome(word):
    if(word == word[::-1]):
        return 1
    else:
        return 0

def features(X):
    
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = letterSum(X[x])   # IMPORTANT !!
        F[x,1] = numberOfVowels(X[x])
        F[x,2] = numberOfConsonants(X[x])
        F[x,3] = len(X[x])
        F[x,4] = numberOfAccentedLetters(X[x])

    return F     

def mytraining(f,Y):

    #logreg = LogisticRegression()
    #logreg.fit(f,Y)
    knn = DecisionTreeClassifier()
    #knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(f,Y)
   
    return knn

def mytrainingCV(f,Y,n):

    knn = KNeighborsClassifier(n_neighbors=n)
    knn.fit(f,Y)
   
    return knn
    
"""def mytrainingaux(f,Y,par):
    
    return clf"""

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred

