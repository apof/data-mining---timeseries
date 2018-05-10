import gmplot

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