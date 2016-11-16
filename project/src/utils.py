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

def binXY(x_coor,y_coor):
    #********************
    #Max x and y coordinate, to be used for binning:
    #Max => 7728636 787862 
    #Min => 7547902 602723 
    #********************

    num_bins=400
    # print "***************"
    # print x_coor,y_coor
    # print math.sqrt(num_bins)
    xedges=np.linspace(7547901,7728637,int(math.sqrt(num_bins)))
    yedges=np.linspace(602723,787863,int(math.sqrt(num_bins)))
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



