
import matplotlib.pyplot as plt
import cv2, math, operator
import numpy as np

def plotData(crimes, categories):
  hist = []
  for cat in categories:
    for day in range(0,7):
      hist.append(0)
      x = []
      y = []
      h = 0            
      for c in crimes:
        if( cat == c.call_group and c.occ_weekday == day):
          x.append( c.x_coordinate )
          y.append( c.y_coordinate )
          h = h+1
      print day, h
      hist.append(h)
      print cat, day, len(x)
      plt.plot(x,y,'r.', alpha = 0.05)
      plt.axis([7610000, 7700000, 650000, 730000])
      plt.show(block = True)
    plt.hist(hist)
    plt.show( block=True )
    raw_input()
        


def plotHeatmap(data, num_xbins = 100, num_ybins = 100):
  base_img = cv2.imread('../data/portland.png')
  heatmap = np.ones(base_img.shape, dtype="uint8")
  hist2d = np.zeros((num_xbins, num_ybins))

  x_bin_size = int(math.ceil(845.0/num_xbins))
  y_bin_size = int(math.ceil(697.0/num_ybins))

  for d in data:
    xbin_id = d.x_pixel/x_bin_size
    ybin_id = d.y_pixel/y_bin_size

    hist2d[xbin_id, ybin_id] += 1

  max_val = np.max(hist2d)
  hist2d = hist2d/max_val 
  for x in range(0, 845):
    for y in range(0, 697):
      xbin_id = x/x_bin_size
      ybin_id = y/y_bin_size
      color = (0, 0, 255*hist2d[xbin_id, ybin_id])
      heatmap[y, x] = color
  alpha = .8
  heatmap = cv2.addWeighted(base_img, 1-alpha, heatmap, alpha, 0)  
  cv2.imshow("asdas", heatmap)
  cv2.waitKey(0)
  #2 miles = 85 pixels
  #1 foot = 0.00804924242 pixels

  #NW Corner AKA 0, 0
  #730304.55
  #7610837.17

  #SE CORNER
  #647920.61
  #7687990.08



def getPixelLoc(x, y):
  y = abs(y - 734285.42)
  x = x - 7599189.49

  x_offset = 5
  y_offset = -10
  return (int(x*0.00804924242)+x_offset, int(y*0.00804924242)+y_offset)



  # 646331.8
  # 7702241.86
