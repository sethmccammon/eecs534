import nltk
import string
from tweet import tweet
import math
from utils import dictionaryLookup

def main():
  file_class = "train"
  tweets, dictionary = parseTweets(file_class)
  probs_donny, probs_hillary, p_hillary,p_donald=BernoulliModel(tweets,dictionary)

  #test on training data
  tweets, dictionary = parseTweets(file_class)
  print BernoulliPredict(tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)


def parseTweets(file_class):
  tweet_filename = "../data/clintontrump.tweets." + file_class
  label_filename = "../data/clintontrump.labels." + file_class

  dictionary = {}
  tweets = []

  with open(tweet_filename) as f:
    text = f.readlines()

  print "Parsing Tweets (counting the frequency of each word)"
  for raw_text in text:
    new_tweet = tweet(raw_text)
    tweets.append(new_tweet)


    for token in new_tweet.tokens:
      if token in dictionary:
        dictionary[token] += 1
      else:
        dictionary[token] = 1

  print "Adding Labels (designating each tweet as Donald or Hillary)"
  with open(label_filename) as f:
    text = f.readlines()

  for ii, label in enumerate(text):
    if 'HillaryClinton' in label:
      tweets[ii].label = 1
    elif 'realDonaldTrump' in label:
      tweets[ii].label = 0
    else:
      print "ERROR: Unknown Label: " + label

    tweets[ii].raw_label = label
  # print len(dictionary)
  return tweets, dictionary

def BernoulliModel(tweets,dictionary):
  #first we need to compute the probability of Hillary
  num_tweets=0.
  count_hillary=0.
  num_clinton=0.
  num_donald=0.
  for i in range(len(tweets)):
    num_tweets+=1.
    if(tweets[i].label==1):
      count_hillary+=1.
      num_clinton+=1.
    else:
      num_donald+=1.

  p_hillary = count_hillary/num_tweets

  #donald=1-hillary
  p_donald=1.-p_hillary
  print p_donald, p_hillary

  #next we need to learn a bernoulli model for each class using the words as features
  dict_hillary={}
  dict_donny={}

  for word in dictionary:#laplace smoothing
    dict_hillary[word]=1.
    dict_donny[word]=1.


  for tweet in tweets:
    for word in tweet.tokens:
      if(word in dict_hillary):
        dict_hillary[word]+=1.

      if(word in dict_donny):
        dict_donny[word]+=1.





  # for i in range(len(tweets)):
#   for token in tweets[1].tokens:
  #     if(tweets[i].label==1):
  #       if token in dict_hillary:
  #         dict_hillary[token] += 1
  #       else:
  #         dict_hillary[token] = 1
  #     else:
  #       if token in dict_donny:
  #         dict_donny[token] += 1
  #       else:
  #         dict_donny[token] = 1

  #compute probabilities of words given the person (and apply laplace smoothing)
  probs_hillary={}
  for word in dictionary:
    probs_hillary[word]=(dict_hillary[word])/(num_clinton)

  probs_donny={}
  for word in dictionary:
    probs_donny[word]=dict_donny[word]/(num_donald)


  return probs_donny, probs_hillary, p_hillary,p_donald

def BernoulliPredict(tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald):
  res=[]
  for count, tweet in enumerate(tweets): 
    if(count%500==0):
      print count
    # print count
    # compute the probably of the tweet given hillary
    keys=dictionary.keys()
    x=[1 if word in tweet.tokens else 0 for word in keys]

    sum_logs_hillary=0
    for ii,word in enumerate(keys):
      # print dictionaryLookup(word,probs_hillary), word
      sum_logs_hillary+=math.log((dictionaryLookup(word,probs_hillary)**x[ii])*(1-dictionaryLookup(word,probs_hillary))**(1-x[ii]))

    sum_logs_donald=0
    for ii,word in enumerate(keys):
      sum_logs_donald+=math.log((dictionaryLookup(word,probs_donny)**x[ii])*(1-dictionaryLookup(word,probs_donny))**(1-x[ii]))

    if((p_hillary*sum_logs_hillary)>(p_donald*sum_logs_donald)):
      res.append(1)
    else:
      res.append(0)
  return res



      



      # sum_probs=0
      # for word in probs_hillary:
      #   sum_probs+=math.log(probs_hillary[word]*(1-probs_hillary[word])**)
  return 0



if __name__ == '__main__':
  main()