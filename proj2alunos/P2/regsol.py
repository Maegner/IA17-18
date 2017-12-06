import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.ensemble import GradientBoostingRegressor
import timeit

def mytraining(X,Y):
    #reg = KernelRidge(kernel='rbf', gamma=0.1, alpha = 0.001)
    reg = svm.SVR(gamma=0.1, epsilon=0.01, C=1000)
    reg.fit(X,Y)
    return reg
    

def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred
