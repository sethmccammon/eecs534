

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

  precip=0
  for d in data:
    precip+=d.precipitation
  print precip/len(data)
  raw_input()

  #run all of the different types
  bins_list=[20,40,60,100]
  temperatures=[0,1]

  # writer = csv.writer(open("../results/errorDataVaryCrimeType.csv", 'wb'), delimiter='  ', quotechar='"', quoting=csv.QUOTE_ALL)
  # writer.writerow("NumberOfBins,TypeOfCrime,PredictedOctoberError,BaselineOctoberError,SpecificConditionsVsAllCrimesOctoberError")

  ofile  = open('../results/errorDataVaryTemperature.csv', "wb")
  writer = csv.writer(ofile, delimiter=',')
  writer.writerow(["NumberOfBins"]+["Temperature"]+["PredictedOctoberError"]+["BaselineOctoberError"]+["SpecificConditionsVsAllCrimesOctoberError"])
  

  for number_of_bins in bins_list:
    for temp in temperatures:
  
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
      training_set = []
      # print len()
      testing_set = []

      for train in data:
        if(int([train.weather.max_temp>65][0])==temp):
          training_set.append(train)

      for test in data2:
        if(int([test.weather.max_temp>65][0])==temp):
          testing_set.append(test)
      print len(testing_set),"---------------------"

      X, y = preprocessData(data, crime_categories, num_xbins, num_ybins)
      model = GP(X, y)
      params = [temp]
      predict_map = predictBayesMultinomialMap(params, model, num_xbins, num_ybins)

      true_map = buildHeatmap(testing_set, num_xbins, num_ybins)
      average_map = buildHeatmap(training_set, num_xbins, num_ybins)
      all_crimes_map=buildHeatmap(data2,num_xbins,num_ybins)
      # writer.writerow("NumberOfBins,TypeOfCrime,PredictedOctoberError,BaselineOctoberError,SpecificConditionsVsAllCrimesOctoberError")
      writer.writerow([str(number_of_bins)]+[str(temp)]+[str(heatmapError(true_map, predict_map))]+
        [str(heatmapError(true_map, average_map))]+[str(heatmapError(all_crimes_map,predict_map))])

      drawHeatmap(predict_map, "../results/predictPrecip"+str(number_of_bins)+"_"+str(temp)+"_"+".png")
      drawHeatmap(true_map, "../results/truePrecip"+str(number_of_bins)+"_"+str(temp)+"_"+".png")
      drawHeatmap(average_map, "../results/baselinePrecip"+str(number_of_bins)+"_"+str(temp)+"_"+".png")
      drawHeatmap(all_crimes_map, "../results/allcrimesPrecip"+str(number_of_bins)+"_"+str(temp)+"_"+".png")

      print "Prediction error on test (type of crime:  ",str(temp),") (num_bins: ",str(number_of_bins),"): ",heatmapError(true_map, predict_map)
      print "Guessing simply using the average of training: ",heatmapError(true_map, average_map)
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