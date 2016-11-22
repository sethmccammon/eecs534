import re, random, urllib
from crime import crime
from utils import checkCityLimits
from weatherData import weatherData

def readData(filename, crime_categories = {}):
  

  with open(filename) as f:
    data = f.readlines()

  res = []
  for line in data[1:]:
    clean_line = line.split(':')
    for ii, item in enumerate(clean_line):
      clean_item = re.sub('\s+$', '', item) #Strip trailing whitespace
      clean_line[ii] = clean_item
    
    if clean_line[1] not in crime_categories:
      crime_categories[clean_line[1]] = len(crime_categories)
      
    if clean_line[7]:
      new_crime = crime(clean_line)
      if new_crime.x_pixel > 0 and new_crime.y_pixel > 0:
        res.append(new_crime)
  random.shuffle(res)

  # print "***********\n",res[:],"***********"
  return res, crime_categories


def augmentData(filename):
  #Convert X, Y coordinates to Lat Long
  print filename
  with open(filename) as f:
    data = f.readlines()

  outfile_name = filename[:-4]+"_lat_long.csv"
  f = open(outfile_name, 'w')
  for line_id, line in enumerate(data[1:]):
    if line_id%1000 == 0:
      print line_id
    clean_line = line.split(':')
    for ii, item in enumerate(clean_line):
      clean_item = re.sub('\s+$', '', item) #Strip trailing whitespace
      clean_line[ii] = clean_item

    lat, lon = getLatLon(clean_line[6], clean_line[5])
    
    outline = ""
    for item in clean_line:
      outline = outline + item + ":"


    f.write(outline+str(lat)+":"+str(lon)+"\n")


    


def getLatLon(northing, easting):
  url = 'http://beta.ngs.noaa.gov/gtkws/geo?northing={0}&easting={1}&units=ift&zone=3601'.format(northing, easting)
  link = urllib.urlopen(url)
  page = link.read()
  try:
    lon = float(re.findall('\"lon\": ([0-9.-]*)', page)[0])
  except IndexError:
    lon = "Error in Lon"
    print "\nError:"
    print page
  try:
    lat = float(re.findall('\"lat\": ([0-9.-]*)', page)[0])
  except IndexError:
    lat = "Error in Lat"
    print "\nError"
    print page
  return lat, lon





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
    