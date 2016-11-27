

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
  '../data/NIJ2016_JAN01_JUL31.csv','../data/NIJ2016_AUG01_AUG31.csv', '../data/NIJ2016_SEP01_SEP30.csv','../data/NIJ2016_OCT01_OCT31.csv']
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


  #run all of the different types
  bins_list=[20,40,60,100]
  # days=[0,1,2,3,4,5,6]

  # writer = csv.writer(open("../results/errorDataVaryCrimeType.csv", 'wb'), delimiter='  ', quotechar='"', quoting=csv.QUOTE_ALL)
  # writer.writerow("NumberOfBins,TypeOfCrime,PredictedOctoberError,BaselineOctoberError,SpecificConditionsVsAllCrimesOctoberError")

  # ofile  = open('../results/errorDataVaryDay.csv', "wb")
  # writer = csv.writer(ofile, delimiter=',')
  # writer.writerow(["NumberOfBins"]+["Day"]+["PredictedOctoberError"]+["BaselineOctoberError"]+["SpecificConditionsVsAllCrimesOctoberError"])
  

  for number_of_bins in bins_list:
    # for day in days:
  
    num_xbins = number_of_bins
    num_ybins = number_of_bins

    

    X, y = preprocessData(data, crime_categories, num_xbins, num_ybins)
    model = GP(X, y)
    params = []
    predict_map = predictBayesMultinomialMap(params, model, num_xbins, num_ybins)

    true_map = buildHeatmap(data, num_xbins, num_ybins)

    drawHeatmap(predict_map, "../results/predictAllData"+str(number_of_bins)+".png")
    drawHeatmap(true_map, "../results/trueAllData"+str(number_of_bins)+".png")

    print "Prediction error on test (num_bins: ",str(number_of_bins),"): ",heatmapError(true_map, predict_map)
    # print "Error on all types: "
    print "*********************************"
    print "*********************************"
    print "*********************************"
  # ofile.close()












  # params = [1]
  # predict_map = predictBayesMultinomialMap(params, model, num_xbins, num_ybins)
  # prediction2heatmap(predict_map)

  print "STOP RIGHT THERE CRIMINAL SCUM!"






if __name__ == '__main__':
  main()