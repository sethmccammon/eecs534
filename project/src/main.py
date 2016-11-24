

#Read Data
#I was thinking use a neural net to try and learn
#we also can think about how to learn most informative features

from data import readData, augmentData, getWeatherData
from predictor import GP, bayesMultinomial, preprocessData, predictBayesMultinomialMap, neuralNet
from utils import dictCombine,binXY, heatmapError
from plotData import plotData, drawHeatmap, buildHeatmap
import math
import numpy as np

def main():
    
  print "Reading Crime Data"
  num_folds = 5  
  weatherLog, weather_categories = getWeatherData()
  #print weather_categories
  #print "length weatherLog: " , len(weatherLog)

  file_names = [ '../data/NIJ2012_MAR01_DEC31.csv', '../data/NIJ2013_JAN01_DEC31.csv', '../data/NIJ2014_JAN01_DEC31.csv', '../data/NIJ2015_JAN01_DEC31.csv', '../data/NIJ2016_JAN01_JUL31.csv', '../data/NIJ2016_AUG01_AUG31.csv', '../data/NIJ2016_SEP01_SEP30.csv']
  #file_names = ['../data/NIJ2016_SEP01_SEP30.csv']
  crime_categories = {}
  data = []
  chunked_data = []

  for filename in file_names:
    print filename
    new_data, crime_categories = readData(filename, crime_categories)
    data = data + new_data
    print len(data)

  print crime_categories
  print "Done Reading Crime Data"
  print "Adding Weather Data"
  for d in data:
    d.loadWeather(weatherLog[d.occ_date]) 
  print "Done Adding Weather Data"
  
  num_xbins = 20
  num_ybins = 20


  chunk_size = int(math.ceil(float(len(data))/num_folds))
  print "Chunk Size:", chunk_size
  for ii in range(num_folds):
    chunk = data[chunk_size*ii:min(chunk_size*(ii+1), len(data))]
    #print "\n", ii
    #chunk[0].printCrime()

    chunked_data.append(chunk)

  for ii in range(num_folds):
    training_set = [j for i in chunked_data[:ii]+chunked_data[ii+1:] for j in i]
    testing_set = chunked_data[ii]
    #print len(testing_set), len(training_set)
    X, y = preprocessData(training_set, crime_categories, num_xbins, num_ybins)
    model = GP(X, y)
    params = []#[0, 0]
    predict_map = predictBayesMultinomialMap(params, model, num_xbins, num_ybins)
    #prediction2heatmap(predict_map)
    drawHeatmap(predict_map, "../results/predict"+str(ii)+".png")
    true_map = buildHeatmap(testing_set, num_xbins, num_ybins)
    drawHeatmap(true_map, "../results/true"+str(ii)+".png")
    print heatmapError(true_map, predict_map)









  # params = [1]
  # predict_map = predictBayesMultinomialMap(params, model, num_xbins, num_ybins)
  # prediction2heatmap(predict_map)

  print "STOP RIGHT THERE CRIMINAL SCUM!"






if __name__ == '__main__':
  main()