#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:35:36 2016

@author: andy
"""

import re
from weatherData import weatherData

def getWeatherData():
 
  weather_categories = []
  with open('../data/weather.csv') as f:
    data = f.readlines()

  print "len data: " , len(data[1:])
  res = {}
  for line in data[1:]:

    clean_line = line.split(',')
    for ii, item in enumerate(clean_line):
      clean_item = re.sub('\s+$', '', item) #Strip trailing whitespace
      clean_line[ii] = clean_item
    
    if clean_line[21] not in weather_categories:
      weather_categories.append( clean_line[21] )
    
    w = weatherData(clean_line)
    res[w.occ_date] = w
  return res, weather_categories
    
   
