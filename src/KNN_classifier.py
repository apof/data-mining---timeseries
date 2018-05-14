from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from numpy import linalg as LA
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import math
from operator import itemgetter
import DTW as dtw
import numpy as np
from sklearn.model_selection import KFold
from sklearn import metrics

def KNN_CrossValidation(folds, data):
	k_fold = KFold(n_splits=folds)
	accuracy = 0
	count = 1
	for train_indices, test_indices in k_fold.split(data['tripId']):
		#text_clf.fit(data['Content'][train_indices], data['Category'][train_indices])
		predicted = KNN(data['Trajectory'][train_indices], data['journeyPatternId'][train_indices], data['Trajectory'][test_indices])
		predicted = np.asarray(predicted)
		accuracy += metrics.accuracy_score(data['journeyPatternId'][test_indices], predicted) 
		
		print str(count) + "st fold completed"
		print str(metrics.accuracy_score(data['journeyPatternId'][test_indices], predicted) )
		count += 1

	print "Accuracy = " + str(accuracy/folds)

	results = []
	results.append(str(accuracy/folds))
	return results

def KNN(train_data, target, predict_data):
	out = []
	predict_data = np.array(predict_data)
	for i in range(len(predict_data)):
		distances = calculate_distances(predict_data[i], train_data, target)
		#print distances
		hashmap = {}
		for i in range(5):
			hashmap[distances[i][1]] = 0
		for i in range(5):
			hashmap[distances[i][1]] += 1
		sorted_hashmap = sorted(hashmap.items(), key=itemgetter(1),reverse=True)
		#print sorted_hashmap
		#print "\n"
		out.append(sorted_hashmap[0][0])

	return out


def calculate_distances(X_predict, X, target):

	distances = []
	X = np.array(X)
	X_predict = np.array(X_predict)
	target = np.array(target)
	#print X[0]
	for i in range(len(X)):
		distance = dtw.DTW_distance(X_predict,X[i])
		distances.append((distance, target[i]))
	sorted_distances = sorted(distances,key=itemgetter(0))

	return sorted_distances