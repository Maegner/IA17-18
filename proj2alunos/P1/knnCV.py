import numpy as np
from sklearn import neighbors, datasets, tree, linear_model
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier
import classsol
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


#load input data
words = []
with open("words.txt",encoding="ISO-8859-9") as file:
    for line in file: 
        line = line.split(' ') #or some other preprocessing
        words.append(line) #storing everything in memory!

X = words[0]

neighbors = [1,2,3,4,5,6,7,8,10]
result = []

for n in neighbors:
    err = 0
    for test in ["wordsclass.npy", "wordsclass2.npy"]:
        
        Y=np.load(test)
        f = classsol.features(X)    
        clf = classsol.mytrainingCV(f,Y,n)
        Ypred = classsol.myprediction(f, clf)
        err += np.sum(Y^Ypred)/len(X)
    result.append(err)

result = np.array(result)
result = result * 50

print(result)

plt.figure()
plt.plot(neighbors,result,'m',label='prediction')
plt.legend( loc = 1 )
plt.show()





