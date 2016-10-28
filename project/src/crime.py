class crime(object):
  """docstring for crime"""
  def __init__(self, arg):
    self.category = arg[0]
    self.call_group = arg[1]
    self.final_case_type = arg[2]
    self.case_desc = arg[3]
    self.occ_date = arg[4]
    self.x_coordinate = arg[5]
    self.y_coordinate = arg[6]
    self.census_tract = arg[7]
    
  def printCrime(self):
    print "Category:", self.category
    print "Call Group:" , self.call_group
    print "Final Case Type:", self.final_case_type
    print "Case Decision:", self.case_desc
    print "Occurance Date:", self.occ_date
    print "X Coordinate:", self.x_coordinate
    print "Y Coordinate:", self.y_coordinate
    print "Census Tract", self.census_tract

