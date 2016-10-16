# import matplotlib.pyplot as plt
from bernoulli import BernoulliModel, BernoulliPredict, BernoulliTest
from multinomial import MultinomialModel, MultinomialPredict, MultinomialTest
from tweet import tweet,parseTweets
import copy
import matplotlib.pyplot as plt


def reduceFeatures():
  file_class = "train"
  tweets, dictionary = parseTweets(file_class)
  probs_donny, probs_hillary, p_hillary,p_donald=BernoulliModel(tweets,dictionary)
  #probs_donny,probs_hillary,dictionary=reduceModel(probs_hillary,probs_donny,dictionary)

  # probs_donny, probs_hillary, p_hillary,p_donald=BernoulliModel(tweets,dictionary,alpha)

  #test on test data
  file_class="dev"
  test_tweets,test_dictionary=parseTweets(file_class)
  # probs_donny, probs_hillary, p_hillary,p_donald=BernoulliModel(tweets,dictionary,alpha)
  #test_prediction = BernoulliPredict(test_tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
  # bernoulli_accuracies.append(BernoulliTest(test_prediction,test_tweets))
  #print "accuracy: ",BernoulliTest(test_prediction,test_tweets)

  #now plot varying thresholds
  accuracies=[]
  num_words=[]

  for thresh in range(0,16):
    reduced_probs_donny, reduced_probs_hillary, reduced_dictionary=reduceModel(copy.deepcopy(probs_hillary), copy.deepcopy(probs_donny), copy.deepcopy(dictionary), thresh)
    test_prediction = BernoulliPredict(test_tweets,reduced_dictionary, reduced_probs_donny, reduced_probs_hillary, p_hillary,p_donald)
    # bernoulli_accuracies.append(BernoulliTest(test_prediction,test_tweets))
    accuracies.append(BernoulliTest(test_prediction,test_tweets))
    num_words.append(len(reduced_dictionary))
  plt.plot(range(0,16),accuracies)
  plt.show()
  plt.plot(range(0,16),num_words)
  plt.show()



def reduceModel(probs_hillary,probs_donny,dictionary,thresh=0.):
  print len(probs_hillary)
  delete_words=[]
  # thresh=15.
  for word in probs_donny:
    if not(probs_donny[word]*(1.+thresh)<probs_hillary[word]) and not(probs_hillary[word]*(1.+thresh)<probs_donny[word]):
      delete_words.append(word)
    # elif(probs_hillary[word]<probs_donny[word]*(1.+thresh)):
    #   delete_words.append(word)

  for word in delete_words:
    probs_donny.pop(word,None)
    probs_hillary.pop(word,None)
    dictionary.pop(word,None)
  print "Afterwards: ",len(probs_hillary)
  # print probs_donny.keys()
  return probs_donny,probs_hillary,dictionary