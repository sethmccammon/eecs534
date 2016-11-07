

#Read Data
#I was thinking use a neural net to try and learn
#we also can think about how to learn most informative features

from data import readData
from bayes import bayesMultinomial, preprocessData
from utils import dictCombine
import math

def main():
  print "Reading Data"

  file_names = ['../data/NIJ2012_MAR01_DEC31.csv', '../data/NIJ2013_JAN01_DEC31.csv', '../data/NIJ2014_JAN01_DEC31.csv', '../data/NIJ2015_JAN01_DEC31.csv', '../data/NIJ2016_JAN01_JUL31.csv', '../data/NIJ2016_AUG01_AUG31.csv', '../data/NIJ2016_SEP01_SEP30.csv']
  crime_categories = {}
  data = []


  for filename in file_names:
    print filename
    new_data, crime_categories = readData(filename, crime_categories)
    print crime_categories
    data = data + new_data
    # crime_categories = dictCombine(crime_categories, new_crime_categories)
    #print crime_categories
  

  counts = {}
  for d in data:
    if d.call_group not in counts.keys():
      counts[d.call_group] = 1
    else:
      counts[d.call_group] += 1

  print counts
  print crime_categories

  #data, crime_categories = readData('../data/NIJ2016_AUG01_AUG31.csv')
  #data = readData('../data/NIJ2016_SEP01_SEP30.csv')
  # X, y = preprocessData(data, crime_categories)
  # model = bayesMultinomial(X, y)

  print len(crime_categories)




  num_folds = 6.0
  chunk_size = int(math.ceil(len(data)/num_folds))
  folds = []

  chunky_data = []



  print len(data)
  for ii in range(int(num_folds)):
    chunk = data[ii*chunk_size:min((ii+1)*chunk_size, len(data))]
    chunky_data.append(chunk)

  for ii, eval_set in enumerate(chunky_data):
    print "Fold:", ii
    train_set = chunky_data[:ii] + chunky_data[ii+1:]
    train_set = [j for i in train_set for j in i]
    train_x, train_y = preprocessData(train_set, crime_categories)
    eval_x, eval_y = preprocessData(eval_set, crime_categories)
    model = bayesMultinomial(train_x, train_y)


    total_accuracy = 0
    for jj, item in enumerate(eval_x):
      if jj%1000 == 0:
        print "Predict", model.predict(eval_x[jj:jj+1])[0], "Actual", eval_y[jj]
      #print model.predict_proba(eval_x[jj:jj+1])
      #print model.predict(eval_x[jj:jj+1])

      total_accuracy += (model.predict(eval_x[jj:jj+1])[0] - eval_y[jj])**2

      # if model.predict(eval_x[jj:jj+1])[0] == eval_y[jj]:
      #   correct += 1
      # else: 
      #   wrong += 1

    print "Fold:", ii, "Accuracy:", total_accuracy/float(jj)





if __name__ == '__main__':
  main()