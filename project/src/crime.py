import datetime

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

