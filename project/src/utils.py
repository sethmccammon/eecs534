import numpy as np
import math


def dictCombine(d1, d2):
  res = {}
  for item in d1:
    if item in res:
      res[item] += d1[item]
    else:
      res[item] = d1[item]

  for item in d2:
    if item in res:
      res[item] += d2[item]
    else:
      res[item] = d2[item]

  return res

def binXY(d, num_xbins, num_ybins):
  x_bin_size = int(math.ceil(845.0/num_xbins))
  y_bin_size = int(math.ceil(697.0/num_ybins))

  xbin_id = d.x_pixel/x_bin_size
  ybin_id = d.y_pixel/y_bin_size

  return xbin_id, ybin_id



def checkCityLimits(x, y):
  #print x, y
  #raw_input()
  if x < 734285.42 and x > 646331.8:
    if y > 7599189.49 and y < 7702241.86:
      return 1
 
  return 0


def heatmapError(h1, h2):
  error = 0
  num_xbins, num_ybins = h1.shape
  for x_bin in range(num_xbins):
    for y_bin in range(num_ybins):
      error += (h1[x_bin, y_bin] - h2[x_bin, y_bin])**2

  return error

def normalizeHeatmap(h):
  total = sum(sum(h))
  return h/total
