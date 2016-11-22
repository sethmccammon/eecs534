

#Read Data
#I was thinking use a neural net to try and learn
#we also can think about how to learn most informative features

from data import readData, augmentData, getWeatherData
from predictor import GP, bayesMultinomial, preprocessData, predictBayesMultinomialMap, neuralNet
from utils import dictCombine,binXY
from plotData import plotData, plotHeatmap, prediction2heatmap
import math
import numpy as np

def main():
    
  print "Reading Crime Data"
  
  weatherLog, weather_categories = getWeatherData()
  #print weather_categories
  #print "length weatherLog: " , len(weatherLog)

  file_names = [ '../data/NIJ2012_MAR01_DEC31.csv', '../data/NIJ2013_JAN01_DEC31.csv', '../data/NIJ2014_JAN01_DEC31.csv', '../data/NIJ2015_JAN01_DEC31.csv', '../data/NIJ2016_JAN01_JUL31.csv', '../data/NIJ2016_AUG01_AUG31.csv', '../data/NIJ2016_SEP01_SEP30.csv']
  #file_names = ['../data/NIJ2016_SEP01_SEP30.csv']
  crime_categories = {}
  data = []

  for filename in file_names:
    print filename
    new_data, crime_categories = readData(filename, crime_categories)
    data = data + new_data
    print len(data)

  print "Done Reading Crime Data"
  print "Adding Weather Data"
  for d in data:
    d.loadWeather(weatherLog[d.occ_date]) 
  print "Done Adding Weather Data"
  
  num_xbins = 20
  num_ybins = 20

  X, y = preprocessData(data, crime_categories, num_xbins, num_ybins)

  # print X
  # print y

  model = GP(X, y)
  params = [1]
  predict_map = predictBayesMultinomialMap(params, model, num_xbins, num_ybins)
  prediction2heatmap(predict_map)

  # params = [1]
  # predict_map = predictBayesMultinomialMap(params, model, num_xbins, num_ybins)
  # prediction2heatmap(predict_map)

  print "STOP RIGHT THERE CRIMINAL SCUM!"






if __name__ == '__main__':
  main()