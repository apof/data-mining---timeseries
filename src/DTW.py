import pandas as pd
import gmplot
import sys
from haversine import haversine
from ast import literal_eval
from operator import itemgetter
import plotter as plotter
import time


def DTW_distance(list1, list2):
	n = len(list1)+1
	m = len(list2)+1
	DTW = [[0 for x in range(m)] for y in range(n)]
	for i in range(n):
		DTW[i][0] = sys.maxint
	for i in range(m):
		DTW[0][i] = sys.maxint
	DTW[0][0] = 0

	for i in range(1,n):
		for j in range(1,m):
			#print list2[0][2]
			cost = haversine((list1[i-1][2], list1[i-1][1]),(list2[j-1][2], list2[j-1][1]))
			DTW[i][j] = cost + min(DTW[i-1][j], DTW[i][j-1], DTW[i-1][j-1])

	#calculate distance
	distance = DTW[n-1][m-1]
	i = n-1
	j = m-1
	while(i != 1 and j != 1):
		min_neigh = min(DTW[i-1][j], DTW[i][j-1], DTW[i-1][j-1])
		distance = min_neigh
		if(min_neigh == DTW[i-1][j]):
			i = i-1
		elif(min_neigh == DTW[i][j-1]):
			j = j-1
		else:
			i = i-1
			j = j-1

	return distance



trainSet = pd.read_csv( '../datasets/train_set.csv', converters={"Trajectory": literal_eval}, index_col='tripId')
trainSetMatrix = trainSet.as_matrix()
#testSet = pd.read_csv( '../datasets/test_set_a1.csv',sep="\t", converters={"Trajectory": literal_eval})
testSet = pd.read_csv( '../datasets/test_set_a1.csv',sep="\t", converters={"Trajectory": literal_eval})
testSetMatrix = testSet.as_matrix()
file = open("./DTW_results.csv",'w')
file.write("Id"+","+"JourneyId"+","+"Distance"+"\n")


counter = 0
start = time.time()
for test in testSetMatrix:
	counter += 1
	distances = []
	for train in trainSetMatrix:
		distance = DTW_distance(test[0],train[1])
		distances.append((distance, train[1], train[0]))
	sorted_distances = sorted(distances,key=itemgetter(0))

	plotter.plot(test[0],"root_"+str(counter)+".html")
	for p in range(5):
		plotter.plot(sorted_distances[p][1],"root_"+str(counter)+"-neighbor_"+str(p+1)+".html")
		file.write("root_"+str(counter)+"-neighbor_"+str(p+1))
		file.write(",")
		file.write(str(sorted_distances[p][2]))
		file.write(",")
		file.write(str(sorted_distances[p][0]))
		file.write("\n")

end = time.time()
print("elapsed time = "+str(end - start))

file.close()