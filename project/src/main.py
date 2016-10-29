

#Read Data
#I was thinking use a neural net to try and learn
#we also can think about how to learn most informative features

from data import readData
from bayes import bayesMultinomial, preprocessData
import math

def main():
  print "Reading Data"
  data, crime_categories = readData('../data/NIJ2015_JAN01_DEC31.csv')



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
    train_set = chunky_data[:ii] + chunky_data[ii+1:]
    train_set = [j for i in train_set for j in i]
    train_x, train_y = preprocessData(train_set, crime_categories)
    eval_x, eval_y = preprocessData(eval_set, crime_categories)
    model = bayesMultinomial(train_x, train_y)


    correct = 0
    wrong = 0
    for jj, item in enumerate(eval_x):
      #print model.predict_proba(eval_x[jj:jj+1])
      #print model.predict(eval_x[jj:jj+1])
      if model.predict(eval_x[jj:jj+1])[0] == eval_y[jj]:
        correct += 1
      else: 
        wrong += 1

    print "Fold:", ii, "Accuracy:", correct/float(correct+wrong)





if __name__ == '__main__':
  main()