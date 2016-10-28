

#Read Data
#I was thinking use a neural net to try and learn
#we also can think about how to learn most informative features

from data import readData

def main():
  
  data = readData('../data/NIJ2016_AUG01_AUG31_USE.csv')
  #data = readData('../data/NIJ2016_SEP01_SEP30.csv')


  data[0].printCrime()
if __name__ == '__main__':
  main()