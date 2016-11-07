import math

class decisionNode(object):
  """docstring for decisionNode"""
  def __init__(self, thresh, parameter, rhs_data, lhs_data, k):

    print "Splitting on Paramter", parameter, "thresh =", thresh
    self.type = 'decision'

    self.thresh = thresh 
    self.parameter = parameter

    #rhs: val > thresh
    #lhs: val <= thresh

    self.rhs_data = rhs_data
    self.lhs_data = lhs_data

    self.lhs = buildTree(lhs_data, k)
    self.rhs = buildTree(rhs_data, k)

class leafNode(object):
  def __init__(self, val):
    print "Leaf:", val
    self.type = 'leaf'
    self.value = val


def buildTree(data, k):
  labels = {}
  for d in data:
    try:
      labels[d[-1]] += 1
    except KeyError:
      labels[d[-1]] = 1
  
  if len(data) < k:
    max_count = 0
    max_key = 0
    for key in labels.keys():
      if labels[key] > max_count:
        max_count = labels[key]
        max_key = key

    return leafNode(key)
  elif len(labels) == 1:
    return leafNode(labels.keys()[0])
  else:
    parameter, thresh = computeMaximalThresh(data)
    lhs_data, rhs_data = splitData(data, parameter, thresh)
    return decisionNode(thresh, parameter, rhs_data, lhs_data, k)


def computeMaximalThresh(data):

  best_parameter = -1
  best_thresh = -1
  max_info_gain = -float('inf')

  for parameter in range(len(data[0])-1):
    for item in data:
      thresh = item[parameter]

      lhs_data, rhs_data = splitData(data, parameter, thresh)
      info_gain = computeInfoGain(data, lhs_data, rhs_data)
      #print parameter, thresh, info_gain
      if info_gain > max_info_gain:
        best_thresh = thresh
        best_parameter = parameter
        max_info_gain = info_gain


  #print "Best:", best_parameter, best_thresh, max_info_gain
  #raw_input()
  return best_parameter, best_thresh


def computeInfoGain(data, lhs_data, rhs_data):
  return entropy(data) - len(lhs_data)*entropy(lhs_data)/len(data) - len(rhs_data)*entropy(rhs_data)/len(data)



def splitData(data, parameter, thresh):
  rhs_data = []
  lhs_data = []


  for item in data:
    if item[parameter] > thresh:
      rhs_data.append(item)
    else: #item[parameter] <= thresh
      lhs_data.append(item)

  return lhs_data, rhs_data


def entropy(data):
  res = 0

  labels = {}
  for d in data:
    try:
      labels[d[-1]] += 1.0
    except KeyError:
      labels[d[-1]] = 1.0


  #print len(labels)
  for label in labels.keys():
    #sprint labels[label]/len(data)
    res += math.log(labels[label]/len(data), 2)*(labels[label]/len(data))

  return -1 * res


def predict(node, query):
  if node.type is not 'leaf':
    if query[node.parameter] > node.thresh:
      return predict(node.rhs, query)
    else:
      return predict(node.lhs, query)
  else:
    return node.value


def printTree(node, level=0):
  if node.type is 'leaf':
    outstr = ("  "*level) + "Class: " + str(node.value)
    print outstr
  else:
    outstr = ("  "*level) + "If X[" + str(node.parameter) + "] <= " + str(node.thresh)
    print outstr
    printTree(node.lhs, level+1)
    print ("  "*level) + "Else"
    printTree(node.rhs, level+1)


