import pandas as pd
import gmplot
from haversine import haversine
from ast import literal_eval
import plotter as plotter
import time
from operator import itemgetter

def backtrack(matrix, list1, list2, i, j, result):
	if(i == 0 or j == 0):
		return result
	if(distance_matching((list1[i-1][2],list1[i-1][1]),(list2[j-1][2],list2[j-1][1]))):
		result.insert(0, (list2[j-1][1],list2[j-1][2]))
		return backtrack(matrix, list1, list2, i-1, j-1, result)
	if(matrix[i][j-1] > matrix[i-1][j]):
		return backtrack(matrix, list1, list2, i, j-1, result)
	return backtrack(matrix, list1, list2, i-1, j, result)

def distance_matching(x, y):
	if(haversine(x,y) > 0.2):
		return False
	else:
		return True 

def find_LCSS(list1, list2):
	n = len(list1)+1
	m = len(list2)+1
	matrix = [[0 for x in range(m)] for y in range(n)]
	for i in range(n):
		matrix[i][0] = 0
	for i in range(m):
		matrix[0][i] = 0
	for i in range(1,n):
		for j in range(1,m):
			if(distance_matching((list1[i-1][2],list1[i-1][1]),(list2[j-1][2],list2[j-1][1]))):
				matrix[i][j] = matrix[i-1][j-1]+1
			else:
				matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
	#find the common subsequence
	if(matrix[n-1][m-1] > 0):
		result = (matrix[n-1][m-1], backtrack(matrix, list1, list2, n-1, m-1, []) )
	else:
		result = (matrix[n-1][m-1], [])
	return result

def main():
	trainSet = pd.read_csv( '../datasets/train_set.csv', converters={"Trajectory": literal_eval}, index_col='tripId')
	trainSetMatrix = trainSet.as_matrix()
	testSet = pd.read_csv( '../datasets/test_set_a2.csv',sep="\t", converters={"Trajectory": literal_eval})
	testSetMatrix = testSet.as_matrix()
	file = open("./LCSS_results.csv",'w')
	file.write("Id"+","+"JourneyId"+","+"Matching points"+"\n")

	counter = 0
	start = time.time()
	for test in testSetMatrix:
		counter += 1
		distances = []
		for train in trainSetMatrix:
			lcss_similarity = find_LCSS(test[0],train[1])
			if(lcss_similarity[0] > 0):
				distances.append((lcss_similarity[0], train[1], lcss_similarity[1], train[0]))
			#print lcss_similarity
		sorted_distances = sorted(distances,key=itemgetter(0),reverse=True)

		plotter.plot(test[0],"route_"+str(counter)+".html")
		for p in range(5):
			plotter.plot2(sorted_distances[p][1],sorted_distances[p][2],"route_"+str(counter)+"-neighbor_"+str(p+1)+".html")
			file.write("route_"+str(counter)+"-neighbor_"+str(p+1))
			file.write(",")
			file.write(str(sorted_distances[p][3]))
			file.write(",")
			file.write(str(sorted_distances[p][0]))
			file.write("\n")

	end = time.time()
	print("elapsed time = "+str(end - start))

	#file.close()


if __name__ == "__main__":
	main()