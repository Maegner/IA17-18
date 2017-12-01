import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import timeit

def mytraining(X,Y):
    #reg = KernelRidge(kernel='rbf', gamma=0.1, alpha = 0.001)
    reg = Pipeline([('poly', PolynomialFeatures(degree=8)),  ('linear', linear_model.LassoLars(alpha=1/10000))])
    reg.fit(X,Y)
    return reg
    

def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred
