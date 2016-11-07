def readData(filename):
  with open(filename) as f:
    data = f.readlines()


  res = []
  for line in data:
    res.append([float(x.strip()) for x in line.split(';')])

  return res