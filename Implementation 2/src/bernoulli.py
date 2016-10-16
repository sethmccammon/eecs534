from utils import dictionaryLookup
import math

def BernoulliModel(tweets, dictionary):
  #first we need to compute the probability of Hillary
  num_tweets=0.
  num_clinton=0.
  num_donald=0.
  for i in range(len(tweets)):
    num_tweets+=1.
    if(tweets[i].label==1):
      num_clinton+=1.
    else:
      num_donald+=1.

  p_hillary = num_clinton/num_tweets

  #donald=1-hillary
  p_donald=1.-p_hillary
  print p_donald, p_hillary
  #next we need to learn a bernoulli model for each class using the words as features
  dict_hillary={}
  dict_donny={}

  for word in dictionary: #initialize dictionary
    dict_hillary[word]=1.
    dict_donny[word]=1.


  for tweet in tweets:
    for word in tweet.tokens:
      if(word in dict_hillary):
        dict_hillary[word]+=1.
      if(word in dict_donny):
        dict_donny[word]+=1.


  probs_hillary={}
  for word in dictionary:
    probs_hillary[word] = dict_hillary[word]/num_clinton
  

  probs_donny={}
  for word in dictionary:
    probs_donny[word] = dict_donny[word]/num_donald




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
      print word, dictionaryLookup(word, probs_donny), x[ii]



      sum_logs_donald+=math.log((dictionaryLookup(word,probs_donny)**x[ii])*(1-dictionaryLookup(word,probs_donny))**(1-x[ii]))

    if((p_hillary*sum_logs_hillary)>(p_donald*sum_logs_donald)):
      res.append(1)
    else:
      res.append(0)
  return res