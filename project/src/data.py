import re

def readData(filename):
  with open(filename) as f:
    data = f.readlines()

  clean_data = []
  for line in data:
    clean_line = line.split(',')
    for ii, item in enumerate(clean_line):
      clean_item = re.sub('\s+$', '', item) #Strip trailing whitespace
      clean_line[ii] = clean_item

    clean_data.append(clean_line)


  return clean_data
