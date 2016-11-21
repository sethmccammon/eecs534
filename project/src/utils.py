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

def binXY(x_coor,y_coor, num_xbins = 1, num_ybins = 1):
    #********************
    #Max x and y coordinate, to be used for binning:
    #Max => 7728636 787862 
    #Min => 7547902 602723 
    #********************

    # print "***************"
    # print x_coor,y_coor
    # print math.sqrt(num_bins)
    xedges=np.linspace(0,845,int(num_xbins))
    yedges=np.linspace(0,697,int(num_ybins))
    # print xedges 
    # print yedges
    x=[x_coor]
    y=[y_coor]
    H, xedges, yedges = np.histogram2d(x,y, bins=(xedges, yedges))
    # print H
    xbin=np.where(H==1)[0][0]
    ybin=np.where(H==1)[1][0]
    # print np.argmax(H)
    # return np.argmax(H)
    return xbin,ybin



def checkCityLimits(x, y):
  #print x, y
  #raw_input()
  if x < 734285.42 and x > 646331.8:
    if y > 7599189.49 and y < 7702241.86:
      return 1
 
  return 0