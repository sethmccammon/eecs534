from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np
from utils import binXY, normalizeHeatmap

def bayesMultinomial(X, y):


  clf = MultinomialNB()
  clf.fit(np.array(X),np.array(y))

  return clf


def neuralNet(X, y):
  clf = MLPRegressor(max_iter = 1000, activation = 'logistic')
  clf.fit(np.array(X),np.array(y))

  return clf

def GP(X, y):
  clf = GaussianProcessRegressor()
  clf.fit(np.array(X),np.array(y))

  return clf


def preprocessData(data, categories, num_xbins, num_ybins):
  data_dict = {}

  print "Len Data:", len(data)
  for ii, d in enumerate(data):
    # print dir(d)
    x_bin, y_bin = binXY(d, num_xbins, num_ybins) 
    key = (x_bin, y_bin)#, categories[d.call_group], d.occ_weekday)#, d.occ_weekday, categories[d.call_group], int([d.weather.max_temp>65][0]))
    try:
      data_dict[key] += 1
    except KeyError:
      data_dict[key] = 1

    
  X = []
  y = []
  for d in data_dict:
    X.append(list(d))
    y.append(data_dict[d])

    #print list(d), data_dict[d]


  # for ii in range(num_xbins):
  #   for jj in range(num_ybins):
  #     print ii, jj, data_dict[ii, jj]
  
  return X, y

def predictBayesMultinomialMap(params, model, num_xbins, num_ybins):


  res = np.zeros((num_xbins, num_ybins))

  for x_bin in range(num_xbins):
    for y_bin in range(num_ybins):
      x = np.asarray([x_bin, y_bin] + params)
      x = x.reshape(1, -1)
      res[x_bin, y_bin] = max(0, model.predict(x))

  return normalizeHeatmap(res)