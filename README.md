# data-mining---timeseries

In this assignment we have performed 3 tasks on timeseries (bus routes).
The first task is to find the closest neighbor route of several bus routes, while the second is to find the closest sub-routes of several bus routes.
We have also visualized the dataset, using the gmplot library of Python and we have performed a classification task for timeseries.

For the first task, we find the 5 closest neighbors using Dynamic Time Warping (DTW) technique.
For the second task, given several timeseries, we use the Longest Common Subsequence (LCS) technique in order to find other routes that have common parts.
For the classification of routes we use a KNN classifier and the geographical distances between 2 GPS points are calculated with Harversine distance.
