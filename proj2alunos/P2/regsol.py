import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Perceptron
import timeit

def mytraining(X,Y):
    reg = KernelRidge(kernel='rbf', gamma=0.05, alpha = 1e-05)
    #reg = Pipeline([('poly', PolynomialFeatures(degree=10)),  ('linear', HuberRegressor(alpha=0.1))])
    reg.fit(X,Y)
    return reg
    

def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred
