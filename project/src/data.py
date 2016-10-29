import re, random
from crime import crime

def readData(filename):
  
  crime_categories = {}
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
      res.append(crime(clean_line))
  random.shuffle(res)
  return res, crime_categories
