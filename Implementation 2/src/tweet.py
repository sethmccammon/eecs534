import nltk, string
from utils import cleanTokens

class tweet(object):
  def __init__(self, raw_text):
    self.text = raw_text
    self.raw_label = ""
    self.label = -1
    #Label 0 = Trump
    #Label 1 = Clinton

    text_no_punctuation = raw_text.translate(string.maketrans("",""), string.punctuation)
    raw_tokens = nltk.word_tokenize(text_no_punctuation)
    self.tokens = cleanTokens(raw_tokens)

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
    