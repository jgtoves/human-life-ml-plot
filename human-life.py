import matplotlib.pyplot as plt
import numpy
import pandas as pd

from sklearn import linear_model
df = pd.read_csv('/kaggle/input/timespent/time-spent-with-relationships-by-age-us.csv')
X = df["Time spent with partner, by age of respondent (United States)"]
y = df["Year"]
##myMean = numpy.mean(column)
##print(myMean)
plt.scatter(X , y)
##plt.hist(x, 10)
plt.show()

##regr = linear_model.LinearRegression()
##regr.fit(X, y)
#Insert x and y
##myPrediction = regr.predict([[10, 15]])
##print(myPrediction)
