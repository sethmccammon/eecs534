import random
from decisionTree import buildTree, predictTree

def buildForest(data, num_trees, k):
  num_samples = 2


  forest = []

  for tree_id in range(num_trees):
    random_data = [random.sample(data, 1)[0] for x in range(len(data))]
    forest.append(buildTree(random_data, k, num_samples))
  return forest

def predictForest(forest, query):
  predictions = []
  for tree in forest:
    predictions.append(predictTree(tree, query))

  #print predictions
  return max(set(predictions), key=predictions.count)
