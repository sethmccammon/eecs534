import numpy as np
import operator, math, random

def main():
  filename = '../data/train p1-16.csv'
  thresh = 0.05
  learn_rate = 0.5
  x, y = readData(filename)
  w = [(random.random()-.5)*2 for ii in x[0]]

  gradient_mag = float('inf')

  iteration = 0
  while gradient_mag > thresh:
    print "Iter:", iteration
    iteration += 1
    gradient = computeGradient(x, w, y)
    # print gradient
    w = [w[ii] - gradient[ii]*learn_rate for ii in range(len(w))]
    # print w
    gradient_mag = l2norm(gradient)
    print gradient_mag



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

    # print output_features
  for ii in range(len(input_features)):
    output_features[ii] = output_features[ii]/(max_val)
    input_features[ii] = [x/(max_val) for x in input_features[ii]]

  # print input_features
  return input_features, output_features


def SSE(x, w, y):
  learn_rate = 1.0
  total_err = 0
  for ii in range(len(x)):
    total_err += (y[ii]- sum(map(operator.mul, x[ii], w)))**2 + learn_rate*l2norm(w)
  return total_err


def computeGradient(x, w, y):
  res = [0 for ii in x[0]]
  d1=np.asarray(w)*np.asarray(x)
  d15=np.transpose(d1)-np.asarray(y)
  d2=np.transpose(d15)*np.asarray(x)
  res=sum(d2)
  print res
  # deltaE=sum((np.asarray(w)*np.asarray(x)-np.asarray(y))*np.asarray(x))
  # diff = SSE(x, w, y)
  # for ii in range(len(x)):
  #   delt1=y[ii]-np.asarray(w)*x[ii]
  #   delt1=delt1**2
  #   # delt2=delt1*x[ii]
  #   # delt3=delt1+1.*l2norm(w)
  #   res=res+delt1
  #   # vec = [element * diff for element in x[ii]] 
  #   # res = map(operator.add, res, vec)[xi * w for xi in x[ii]]
  #   # print type(x[ii])
  #   # print res
   
  # res=res+5.*l2norm(w)
  return res


def l2norm(vec):
  res = [x**2 for x in vec]
  return math.sqrt(sum(res))
# [xi * w for xi in x[ii]]

def normalize(vec):
  vec_len = sum([x**2 for x in vec])
  return [x/vec_len for x in vec]


if __name__ == '__main__':
  main()