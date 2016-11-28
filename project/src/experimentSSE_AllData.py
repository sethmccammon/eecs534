

#Read Data
#I was thinking use a neural net to try and learn
#we also can think about how to learn most informative features

from data import readData, augmentData, getWeatherData
from predictor import GP, bayesMultinomial, preprocessData, predictBayesMultinomialMap, neuralNet
from utils import dictCombine,binXY, heatmapError, averageError
from plotData import plotData, drawHeatmap, buildHeatmap
import math, random
import numpy as np
import time
import csv

def main():
    
  print "Reading Crime Data"
  num_folds = 5  
  weatherLog, weather_categories = getWeatherData()
  #print weather_categories
  #print "length weatherLog: " , len(weatherLog)

  file_names = [ '../data/NIJ2012_MAR01_DEC31.csv', '../data/NIJ2013_JAN01_DEC31.csv', '../data/NIJ2014_JAN01_DEC31.csv', '../data/NIJ2015_JAN01_DEC31.csv', 
  '../data/NIJ2016_JAN01_JUL31.csv','../data/NIJ2016_AUG01_AUG31.csv', '../data/NIJ2016_SEP01_SEP30.csv']
  # file_names = ['../data/NIJ2016_SEP01_SEP30.csv']
  crime_categories = {}
  data = []
  chunked_data = []

  for filename in file_names:
    print filename
    new_data, crime_categories = readData(filename, crime_categories)
    data = data + new_data
    print len(data)
  random.shuffle(data)

  print crime_categories
  # print "Done Reading Crime Data"
  # print "Adding Weather Data"
  for d in data:
    d.loadWeather(weatherLog[d.occ_date]) 
  # print "Done Adding Weather Data"

  #create some test data
  train_d=data[:len(data)*4/5]
  test_d=data[len(data)*4/5:]

  print "len train: ",len(train_d)
  print "len test: ",len(test_d)



  #run all of the different types
  bins_list=[20,40,60,100]

  ofile  = open('../results/errorSSE_AllData.csv', "wb")
  writer = csv.writer(ofile, delimiter=',')
  writer.writerow(["NumberOfBins"]+["PredictedOctoberError"]+["PredictedTestError"]+["PredictedUniformError"]+["UniformOctoberError"]+["UniformTestError"])
  

  for number_of_bins in bins_list:
  
    num_xbins = number_of_bins
    num_ybins = number_of_bins

  # #*******************************************************************************************
  # #*******************************************************************************************
    file_names = ['../data/NIJ2016_OCT01_OCT31.csv']
    crime_categories = {}
    data2 = []
    chunked_data = []

    for filename in file_names:
      print filename
      new_data, crime_categories = readData(filename, crime_categories)
      data2 = data2 + new_data
      print len(data2)
    random.shuffle(data2)

    print crime_categories
    # print "Done Reading Crime Data"
    # print "Adding Weather Data"
    for d in data2:
      d.loadWeather(weatherLog[d.occ_date]) 
    # print "Done Adding Weather Data"

    # for ii in range(num_folds):
    # training_set = []
    # # print len()
    # testing_set = []

    # for train in data:
    #   if(crime_categories[train.call_group]==type_of_crime):
    #     training_set.append(train)

    # for test in data2:
    #   if(crime_categories[test.call_group]==type_of_crime):
    #     testing_set.append(test)

    X, y = preprocessData(train_d, crime_categories, num_xbins, num_ybins)
    model = GP(X, y)
    params = []
    predict_map = predictBayesMultinomialMap(params, model, num_xbins, num_ybins)

    october_map = buildHeatmap(data2, num_xbins, num_ybins)
    test_map = buildHeatmap(test_d,num_xbins,num_ybins)

    #uniform map
    uniform = np.ones((num_xbins,num_ybins))
    uniform = uniform/(num_xbins*num_ybins)
    uniform_map=uniform
    # print "sum should be one: ",sum(uniform)
    print uniform


    # average_map = buildHeatmap(training_set, num_xbins, num_ybins)
    # all_crimes_map=buildHeatmap(data2,num_xbins,num_ybins)
    # writer.writerow(["NumberOfBins"]+["PredictedOctoberError"]+["PredictedTestError"]+["PredictedUniformError"]+["UniformOctoberError"]+["UniformTestError"])
    writer.writerow([str(number_of_bins)]+[str(heatmapError(october_map, predict_map))]+
      [str(heatmapError(test_map, predict_map))]+[str(heatmapError(predict_map,uniform_map))]+[str(heatmapError(october_map,uniform_map))]+
      [str(heatmapError(test_map,uniform_map))])

    drawHeatmap(predict_map, "../results/SSE_AllData_predict"+str(number_of_bins)+".png")
    drawHeatmap(october_map, "../results/SSE_AllData_october"+str(number_of_bins)+".png")
    drawHeatmap(test_map, "../results/SSE_AllData_test"+str(number_of_bins)+"_"+".png")
    drawHeatmap(uniform_map, "../results/SSE_AllData_uniform"+str(number_of_bins)+".png")

    print "Prediction error october  (num_bins: ",str(number_of_bins),"): ",heatmapError(october_map, predict_map)
    print "Guessing simply using the average of training: ",heatmapError(october_map,uniform_map)
    # print "Error on all types: "
    print "*********************************"
    print "*********************************"
    print "*********************************"
  ofile.close()












  # params = [1]
  # predict_map = predictBayesMultinomialMap(params, model, num_xbins, num_ybins)
  # prediction2heatmap(predict_map)

  print "STOP RIGHT THERE CRIMINAL SCUM!"






if __name__ == '__main__':
  main()