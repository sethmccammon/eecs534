from sklearn.naive_bayes import MultinomialNB
import numpy as np

def bayesMultinomial(X, y):


  clf = MultinomialNB()
  clf.fit(np.array(X),np.array(y))

  return clf

def preprocessData(data, categories):
  data_dict = {}





  print "Len Data:", len(data)
  for ii, d in enumerate(data):
    # print dir(d)

    try:
      data_dict[d.occ_weekday, d.xbin, d.ybin, categories[d.call_group], [d.weather.max_temp>65][0]] += 1
    except KeyError:
      data_dict[d.occ_weekday, d.xbin, d.ybin, categories[d.call_group], [d.weather.max_temp>65][0]] = 1

    

    # if [d.occ_weekday, d.census_tract, categories[d.call_group]] in data_dict.keys():
    #   data_dict[d.occ_weekday, d.census_tract, categories[d.call_group]] += 1
    # else:
    #   data_dict[d.occ_weekday, d.census_tract,categories[d.call_group]] = 1




  X = []
  y = []
  for d in data_dict:

    X.append(list(d))
    y.append(data_dict[d])

  return X, y


