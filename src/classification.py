import pandas as pd
import numpy as np
from ast import literal_eval
#from sklearn.neighbors import NearestNeighbors
import sys
from haversine import haversine
import KNN_classifier as knn
#import DTW as dtw




trainSet = pd.read_csv( '../datasets/train_set.csv', converters={"Trajectory": literal_eval})
trainSet = trainSet[0:500]
#trainSetMatrix = trainSet.as_matrix()

# X = [[] for i in range(len(trainSetMatrix))]

# for i in range(len(trainSetMatrix)):
# 	for j in trainSetMatrix[i][2]:
# 		X[i].append(j[1])
# 		X[i].append(j[2])	
# #X = np.array(X)
# #print X
testSet = pd.read_csv( '../datasets/test_set_a1.csv',sep="\t", converters={"Trajectory": literal_eval})
# #print trainSet['Trajectory']
# nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree', metric=dtw.DTW_distance)
# #X = np.array(trainSet['Trajectory'])

# nbrs.fit(X)


knn.KNN_CrossValidation(10,trainSet)
#knn.KNN(trainSet['Trajectory'], trainSet['journeyPatternId'], testSet['Trajectory'])

# for test in testSetMatrix:
# 	x = np.array(test[0])
# 	