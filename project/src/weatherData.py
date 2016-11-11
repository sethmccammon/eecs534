#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:35:36 2016

@author: andy
"""

import datetime

class weatherData(object):
  def __init__(self, arg):
    date = arg[0].split('-')
    self.occ_date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    self.max_temp = arg[1]
    self.min_temp = arg[2]
    self.mean_humidity = arg[8]
    self.mean_visibility = arg[14]
    self.mean_wind_speed = arg[17]
    self.max_gust_speed = arg[18]
    self.precipitation = arg[19]
    self.cloud_cover = arg[20]
    self.events = arg[21]
    
    
    
  def printWeather( self ):
    print "Max Temperature: " , self.max_temp # F
    print "Min Temperature:" , self.min_temp # F
    print "Mean Humidity:", self.mean_humidity  
    print "Mean Visibility:", self.mean_visibility # miles
    print "Mean Wind Speed:", self.mean_wind_speed # mph
    print "Max Gust Speed:", self.max_gust_speed # mph
    print "Precipitation:", self.precipitation # in
    print "Cloud Cover:", self.cloud_cover
    print "Events: ", self.events
