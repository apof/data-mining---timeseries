import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.neighbors import NearestNeighbors
import sys
from haversine import haversine


def DTW_distance(list1, list2):
	n = len(list1)+1
	m = len(list2)+1
	print list1
	print list2
	DTW = [[0 for x in range(m)] for y in range(n)]
	for i in range(n):
		DTW[i][0] = sys.maxint
	for i in range(m):
		DTW[0][i] = sys.maxint
	DTW[0][0] = 0

	for i in range(1,n):
		for j in range(1,m):
			cost = haversine((list1[i-1][2], list1[i-1][1]),(list2[j-1][2], list2[j-1][1]))
			DTW[i][j] = cost + min(DTW[i-1][j], DTW[i][j-1], DTW[i-1][j-1])

	#DTW distance is on the right bottom cell
	distance = DTW[n-1][m-1]

	return distance

trainSet = pd.read_csv( '../datasets/small_train.csv', converters={"Trajectory": literal_eval}, index_col='tripId')
trainSetMatrix = trainSet.as_matrix()
# print np.array(trainSet["journeyPatternId"])
# print np.array(trainSet["Trajectory"])

# testSet = pd.read_csv( '../datasets/test_set_a1.csv',sep="\t", converters={"Trajectory": literal_eval})
# testSetMatrix = testSet.as_matrix()

nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree', metric=DTW_distance)
nbrs.fit([ np.array([[10, 1], [6, 1]]),np.array([[1,2],[3,4]]) ],["a","a"])

# for test in testSetMatrix:
# 	x = np.array(test[0])
# 	