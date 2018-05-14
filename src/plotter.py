import gmplot

def plot2(list1_with_coordinates, list2_with_coordinates, file_name):

	visited = []
	counter = 0
	lats = []
	longs = []
	for j in list1_with_coordinates:
		lats.append(j[2])
		longs.append(j[1])
	lats2 = []
	longs2 = []
	for j in list2_with_coordinates:
		lats2.append(j[1])
		longs2.append(j[0])
	gmap = gmplot.GoogleMapPlotter(lats[0], longs[0], 16)	
	gmap.plot(lats, longs, 'cornflowerblue', edge_width=10)
	gmap.plot(lats2, longs2, 'red', edge_width=10)
	#gmap.scatter(lats, longs, 'blue', size=40, marker=False)
	#gmap.scatter(lats2, longs2, 'red', size=40, marker=False)
	gmap.draw(file_name)

def plot(list_with_coordinates, file_name):

	visited = []
	counter = 0
	lats = []
	longs = []
	for j in list_with_coordinates:
		lats.append(j[2])
		longs.append(j[1])
	gmap = gmplot.GoogleMapPlotter(lats[0], longs[0], 16)	
	gmap.plot(lats, longs, 'cornflowerblue', edge_width=10)
	gmap.scatter(lats, longs, '#3B0B39', size=40, marker=False)
	gmap.draw(file_name)