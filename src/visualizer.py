import pandas as pd
import gmplot
from ast import literal_eval

trainSet = pd.read_csv( '../datasets/train_set.csv', converters={"Trajectory": literal_eval}, index_col='tripId')
trainSetMatrix = trainSet.as_matrix()

visited = []
counter = 0
print trainSetMatrix[0][1][0][1]
for i in trainSetMatrix:
	if(i[0] not in visited):
		visited.append(i[0])
		counter += 1;
		print i[0]
		lats = []
		longs = []
		for j in i[1]:
			lats.append(j[2])
			longs.append(j[1])
		gmap = gmplot.GoogleMapPlotter(lats[0], longs[0], 16)
		gmap.plot(lats, longs, 'cornflowerblue', edge_width=10)
		gmap.scatter(lats, longs, '#3B0B39', size=40, marker=False)
		gmap.draw("mymap"+str(counter)+".html")
	if(counter == 5):
		break