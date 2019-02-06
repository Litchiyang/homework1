import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
x = load_iris().data
y = load_iris().target

y_0 = x[0:50, :]
y_1 = x[51:100, :]
y_2 = x[101:150, :]

fig, axes = plt.subplots(4, 4, figsize=(15, 15))
fig.text(0.5, 0.9, "Pair plot of the Iris dataset, colored by class label", ha="center", fontsize=20)
fig.subplots_adjust(hspace=0, wspace=0)

for i in [0,1,2,3]:
    for j in [1,2,3]:
        axes[i,j].yaxis.set_visible(False)
        
axes[0,0].set_ylabel('sepal length (cm)', fontsize = 14)
axes[0,0].set_yticklabels(np.arange(4, 8, step=0.5))
axes[1,0].set_ylabel('sepal width (cm)', fontsize = 14)
axes[1,0].set_yticklabels(np.arange(1.5, 4.5, step=0.5))
axes[2,0].set_ylabel('petal length (cm)', fontsize = 14)
axes[3,0].set_ylabel('petal width (cm)', fontsize = 14)

axes[3,0].set_xlabel('sepal length (cm)', fontsize = 14)
axes[3,1].set_xlabel('sepal width (cm)', fontsize = 14)
axes[3,2].set_xlabel('petal length (cm)', fontsize = 14)
axes[3,3].set_xlabel('petal width (cm)', fontsize = 14)

#histograms
for i in np.arange(0, 4):
    axes[i,i].hist(x[:,i], bins = 20, edgecolor = 'k') 

#Scatter plots
for i in [1,2,3]:
    axes[0, i].scatter(y_0[:,i], y_0[:,0], c = 'blue', label = 'setosa', alpha = .8, edgecolor = 'k')
    axes[0, i].scatter(y_1[:,i], y_1[:,0], c = 'red', label = 'versicolor', alpha = .8, edgecolor = 'k')
    axes[0, i].scatter(y_2[:,i], y_2[:,0], c = 'green', label = 'virginica', alpha = .8, edgecolor = 'k')
    
for i in [0,2,3]:
    axes[1, i].scatter(y_0[:,i], y_0[:,1], c = 'blue', label = 'setosa', alpha = .8, edgecolor = 'k')
    axes[1, i].scatter(y_1[:,i], y_1[:,1], c = 'red', label = 'versicolor', alpha = .8, edgecolor = 'k')
    axes[1, i].scatter(y_2[:,i], y_2[:,1], c = 'green', label = 'virginica', alpha = .8, edgecolor = 'k')
    
for i in [0,1,3]:
    axes[2, i].scatter(y_0[:,i], y_0[:,2], c = 'blue', label = 'setosa', alpha = .8, edgecolor = 'k')
    axes[2, i].scatter(y_1[:,i], y_1[:,2], c = 'red', label = 'versicolor', alpha = .8, edgecolor = 'k')
    axes[2, i].scatter(y_2[:,i], y_2[:,2], c = 'green', label = 'virginica', alpha = .8, edgecolor = 'k')
    
for i in [0,1,2]:
    axes[3, i].scatter(y_0[:,i], y_0[:,3], c = 'blue',label = 'setosa', alpha = .8, edgecolor = 'k')
    axes[3, i].scatter(y_1[:,i], y_1[:,3], c = 'red', label = 'versicolor', alpha = .8, edgecolor = 'k')
    axes[3, i].scatter(y_2[:,i], y_2[:,3], c = 'green', label = 'virginica', alpha = .8, edgecolor = 'k')

axes[0,3].legend(bbox_to_anchor=(0.9, 1), fontsize = 13)
plt.savefig('task22.png')