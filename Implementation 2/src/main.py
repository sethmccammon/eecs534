import nltk, math, string
from tweet import tweet
from utils import dictionaryLookup
from bernoulli import BernoulliModel, BernoulliPredict

def main():
  file_class = "train"
  tweets, dictionary = parseTweets(file_class)
  probs_donny, probs_hillary, p_hillary,p_donald=BernoulliModel(tweets,dictionary)

  #test on training data
  tweets, dictionary = parseTweets(file_class)
  prediction = BernoulliPredict(tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
  print "Prediction:", float(sum(prediction))/len(prediction)

def parseTweets(file_class):
  tweet_filename = "../data/clintontrump.tweets." + file_class
  label_filename = "../data/clintontrump.labels." + file_class

  dictionary = {}
  tweets = []

  with open(tweet_filename) as f:
    text = f.readlines()

  print "Parsing Tweets (counting the frequency of each word)"
  #text = text[:100]

  # for item in text:
  #   print item

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

  #text = text[:100]
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






if __name__ == '__main__':
  main()