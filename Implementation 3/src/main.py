from utils import readData
from decisionTree import buildTree, printTree, predictTree
from randomForest import buildForest, predictForest
import matplotlib.pyplot as plt
import numpy as np

def main():
  train_data = readData('../data/iris_train-1.csv')
  test_data = readData('../data/iris_test-1.csv')

  step_size = 5
  #Part 1
  print "Single Tree"
  x = range(1, len(train_data)+step_size, step_size)
  y = []
  for k in x:
    tree = buildTree(train_data, k)
    accuracy = computeAccuracy(test_data, tree, predictTree)
    y.append(accuracy)

  plt.figure()
  plt.plot(x, y)
  title = "Single Tree K value"
  plt.title(title)
  plt.xlabel("K")
  plt.ylabel("% Accuracy")
  plt.savefig("../results/"+title.replace(" ", "_")+".png")
  print "X:", x
  print "Y:", y
  #plt.show()

  #Part 2

  for l in [5, 10, 15, 20, 25, 30]:
    print "Forest L", l
    x = range(1, len(train_data)+step_size, step_size)
    y = []
    stdev = []
    for k in x:
      print "Tree K:", k
      res = []
      for trial in range(20):
        print "Trial:", trial
        forest = buildForest(train_data, l, k)
        accuracy = computeAccuracy(test_data, forest, predictForest)
        res.append(accuracy)
      y.append(np.mean(res))
      stdev.append(np.std(res))
    print "X:", x
    print "Y:", y
    print "STDEV:", stdev
    plt.figure()
    plt.errorbar(x, y, stdev)
    title = "Forest K value - L = " + str(l)
    plt.title(title)
    plt.xlabel("K")
    plt.ylabel("% Accuracy")
    plt.savefig("../results/"+title.replace(" ", "_")+".png")
  #   # plt.show()
  # plt.show()

def computeAccuracy(test_data, test_item, predictionFunction):
  correct = 0.0
  incorrect = 0.0

  for item in test_data:
    y_hat = predictionFunction(test_item, item)
    if y_hat == item[-1]:
      correct += 1
    else:
      incorrect += 1

  return correct/(correct+incorrect)


if __name__ == '__main__':
  main()