import numpy as np
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import LassoLars
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.ticker import FormatStrFormatter
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR

def mytraining(X,Y,k,deg,g):
    reg = SVR(kernel=k, degree=deg,gamma=g)
    reg.fit(X,Y)
    return reg

def myprediction(X,reg):
    
    Ypred = reg.predict(X)

    return Ypred

cv = [0,0]
degs = [1,2,3,4,5,6,7,8,9,10]
gammas = [10,1,0.1,0.08,0.05,0.04,0.01,0.001]
kernels = ["linear", "poly", "rbf"]
for kernel in kernels:
    for gamma in gammas:
        for deg in degs:
            crosValTot = 0
            for ii,test in enumerate(["regress.npy", "regress2.npy"]):
                X,Y,Xp,Yp = np.load(test)
                reg = mytraining(X,Y,kernel,deg,gamma)
                Ypred = myprediction(Xp,reg)
                crosVal = -cross_val_score( reg, X, Y, cv = 5, scoring = 'neg_mean_squared_error').mean()
                cv[ii] = crosVal
                crosValTot += crosVal
            if(cv[0]<0.3 and cv[1]<800):
                print( "[K: "+kernel+"]GAMMA: "+str(gamma)+"][ALPHA: "+str(deg)+"][T1: " +str(cv[0])+ "][T2: "+str(cv[1])+ "][Tot: "+str(crosValTot)+"]")
            
            
