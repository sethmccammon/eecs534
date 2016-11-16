import datetime
from weatherData import weatherData
from utils import binXY

class crime(object):
  """docstring for crime"""
  def __init__(self, arg):



    self.category = arg[0]
    self.call_group = arg[1]
    self.final_case_type = arg[2]
    self.case_desc = arg[3]

    date = arg[4].split('/')
    self.occ_date = datetime.date(int(date[2]), int(date[0]), int(date[1]))
    self.occ_weekday = self.occ_date.weekday()
    self.x_coordinate = int(arg[5])
    self.y_coordinate = int(arg[6])
    if arg[7]:
      self.census_tract = int(arg[7])
    else:
      self.census_tract = -1
    self.xbin,self.ybin=binXY(int(arg[5]),int(arg[6]))



      
    
  def printCrime(self):
    print "Category:", self.category
    print "Call Group:" , self.call_group
    print "Final Case Type:", self.final_case_type
    print "Case Decision:", self.case_desc
    print "Occurance Date:", self.occ_date
    print "Occurrance Weekday:", self.occ_weekday
    print "X Coordinate:", self.x_coordinate
    print "Y Coordinate:", self.y_coordinate
    print "Census Tract", self.census_tract

  def loadWeather(self, w):
    self.weather=w
    # print w
    # self.max_temp = w.max_temp
    # self.min_temp = w.min_temp
    # self.mean_humidity = w.mean_humidity
    # self.mean_visibility = w.mean_visibility
    # self.mean_wind_speed = w.mean_wind_speed
    # self.max_gust_speed = w.max_gust_speed
    # self.precipitation = w.precipitation
    # self.cloud_cover = w.cloud_cover
    # self.events = w.events
    # if(w.maxtemp)
    
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