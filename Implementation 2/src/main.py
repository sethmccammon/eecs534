import nltk, math, string
from tweet import tweet, parseTweets
from utils import dictionaryLookup, topTen
from bernoulli import BernoulliModel, BernoulliPredict, BernoulliTest
from multinomial import MultinomialModel, MultinomialPredict, MultinomialTest
from plotVaryingPrior import plotPriors
from reduceFeatures import reduceFeatures

def main():
  file_class = "train"
  tweets, dictionary = parseTweets(file_class)
  probs_donny, probs_hillary, p_hillary,p_donald=BernoulliModel(tweets,dictionary)

  #test on training data
  tweets, dictionary = parseTweets(file_class)
  prediction = BernoulliPredict(tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
  print "Training accuracy: ", BernoulliTest(prediction,tweets)
  # print "Prediction for training:", float(sum(prediction))/len(prediction)

  #test on test data
  file_class="dev"
  test_tweets,test_dictionary=parseTweets(file_class)
  test_prediction = BernoulliPredict(test_tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
  print "Overall testing accuracy (bernoulli): ", BernoulliTest(test_prediction,test_tweets)

  #multiomial
  file_class="train"
  tweets, dictionary = parseTweets(file_class)
  probs_donny, probs_hillary, p_hillary,p_donald=MultinomialModel(tweets,dictionary)

  # predict multinomial
  prediction = MultinomialPredict(tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
  print "Training accuracy: ", MultinomialTest(prediction,tweets)

  #test multinomial
  file_class="dev"
  test_tweets,test_dictionary=parseTweets(file_class)
  test_prediction = MultinomialPredict(test_tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
  print "Overall testing accuracy (multinomial) ", MultinomialTest(test_prediction,test_tweets)

  topTen(probs_hillary, probs_donny)

  plotPriors()
  
  reduceFeatures()

#TODO: Bsic implementation part 3
#THIS IS OK Do counts have to be with respect to each candidate?












if __name__ == '__main__':
  main()