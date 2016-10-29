from sklearn.naive_bayes import MultinomialNB
import numpy as np

def bayesMultinomial(X, y):


  clf = MultinomialNB()
  clf.fit(np.array(X),np.array(y))

  return clf

def preprocessData(data, categories):
  X = []
  y = []
  for d in data:
    #print d
    X.append([d.occ_weekday, d.census_tract])
    y.append(categories[d.call_group])

  return X, y


