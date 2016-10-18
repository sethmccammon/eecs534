from utils import dictionaryLookup
import math

def BernoulliModel(tweets, dictionary,alpha=1.):
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
  # print p_donald, p_hillary
  #next we need to learn a bernoulli model for each class using the words as features
  dict_hillary={}
  dict_donny={}

  for word in dictionary: #initialize dictionary with prior
    dict_hillary[word]=alpha
    dict_donny[word]=alpha


  for tweet in tweets:
    for word in list(set(tweet.tokens)):
      if tweet.label == 1:
        dict_hillary[word]+=1.
      else:
        dict_donny[word]+=1.


  probs_hillary={}
  # print sorted(dict_hillary.values(),reverse=True)[:15]
  for word in dictionary:
    probs_hillary[word] = dict_hillary[word]/num_clinton
  

  probs_donny={}
  for word in dictionary:
    probs_donny[word] = dict_donny[word]/num_donald




  return probs_donny, probs_hillary, p_hillary,p_donald#, top_ten_donald, top_ten_hillary

def BernoulliPredict(tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald):
  res=[]
  for count, tweet in enumerate(tweets):
    if(count%500==0):
      print "Count:", count
    # print count
    # compute the probably of the tweet given hillary
    keys=dictionary.keys()
    x=[1 if word in list(set(tweet.tokens)) else 0 for word in keys]

    sum_logs_hillary=0
    for ii,word in enumerate(keys):
      # print dictionaryLookup(word,probs_hillary), word
      sum_logs_hillary+=math.log((dictionaryLookup(word,probs_hillary)**x[ii])*(1-dictionaryLookup(word,probs_hillary))**(1-x[ii]))

    sum_logs_donald=0
    for ii,word in enumerate(keys):
      #print word, dictionaryLookup(word, probs_donny), x[ii]
      sum_logs_donald+=math.log((dictionaryLookup(word,probs_donny)**x[ii])*(1-dictionaryLookup(word,probs_donny))**(1-x[ii]))
    #print "Tweet:", count, " - ", sum_logs_hillary + math.log(p_hillary), sum_logs_donald + math.log(p_donald)

    if (sum_logs_hillary + math.log(p_hillary)) > (sum_logs_donald + math.log(p_donald)):
      #print "MAKE AMERICA GREAT"
      res.append(1)
    else:
      #print "I STAND WITH HER"
      res.append(0)

  return res

def BernoulliTest(predicted_labels,tweets):
  count=0.
  # print len(predicted_labels)



  confusion_mat = [[0,0],[0,0]]


  for i in range(len(predicted_labels)):
    if (predicted_labels[i]==tweets[i].label):
      count+=1.

    confusion_mat[predicted_labels[i]][tweets[i].label] += 1

  print "Bernoulli Confusion Matrix"
  print confusion_mat
  return float(count)/float(len(predicted_labels))*100.