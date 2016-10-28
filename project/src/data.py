import re
from crime import crime

def readData(filename):
  with open(filename) as f:
    data = f.readlines()

  res = []
  for line in data[1:]:
    clean_line = line.split(',')
    for ii, item in enumerate(clean_line):
      clean_item = re.sub('\s+$', '', item) #Strip trailing whitespace
      clean_line[ii] = clean_item
  
    res.append(crime(clean_line))

  return res
