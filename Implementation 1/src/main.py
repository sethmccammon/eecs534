import numpy as np
import operator, math, random

def main():
  filename = '../data/train p1-16.csv'
  thresh = .05
  learn_rate = .1
  x, y = readData(filename)
  w = [(random.random()-.5)*2 for ii in x[0]]

  gradient_mag = float('inf')

  iteration = 0
  while gradient_mag > thresh:
    print "Iter:", iteration
    iteration += 1
    gradient = computeGradient(x, w, y)
    print gradient
    w = [w[ii] - gradient[ii]*learn_rate for ii in range(len(w))]
    gradient_mag = l2norm(gradient)
    #print w



def readData(filename):
  input_features = []
  output_features = []
  max_val = 0
  f = open(filename)
  for line in f:
    tokens = map(float, line.split(','))
    v1 = max(tokens)
    v2 = min(tokens)

    max_val = max(max(abs(v1), abs(v2)), max_val)

    input_features.append(tokens[:-1])
    output_features.append(tokens[-1])


  for ii in range(len(input_features)):
    output_features[ii] = output_features[ii]/max_val
    input_features[ii] = [x/max_val for x in input_features[ii]]


  return input_features, output_features


def SSE(x, w, y):
  learn_rate = 1.0
  total_err = 0
  for ii in range(len(x)):
    total_err += (y[ii]- sum(map(operator.mul, x[ii], w)))**2 + learn_rate*l2norm(w)
  return total_err


def computeGradient(x, w, y):
  res = [0 for ii in x[0]]
  
  diff = SSE(x, w, y)
  for ii in range(len(x)):

    vec = [element * diff for element in x[ii]] 
    res = map(operator.add, res, vec)
  return res


def l2norm(vec):
  res = [x**2 for x in vec]
  return math.sqrt(sum(res))


def normalize(vec):
  vec_len = sum([x**2 for x in vec])
  return [x/vec_len for x in vec]


if __name__ == '__main__':
  main()