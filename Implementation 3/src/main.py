from utils import readData
from decisionTree import *


def main():
  train_data = readData('../data/iris_train-1.csv')
  test_data = readData('../data/iris_test-1.csv')
  k = 5

  

  # d = [[0] for x in range(7)] + [[1] for x in range(26)]
  
  # d1 = [[0] for x in range(3)] + [[1] for x in range(21)]
  # d2 = [[0] for x in range(4)] + [[1] for x in range(5)]

  # print computeInfoGain(d, d1, d2)
  tree = buildTree(train_data, k)
  printTree(tree)
  # print "Tree Constructed\n"

  # correct = 0.0
  # incorrect = 0.0

  # for item in test_data:
  #   y_hat = predict(tree, item)
  #   if y_hat == item[-1]:
  #     correct += 1
  #   else:
  #     incorrect += 1

  # print correct/(correct+incorrect)

if __name__ == '__main__':
  main()