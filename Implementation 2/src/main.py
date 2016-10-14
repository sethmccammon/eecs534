import nltk
import string
from tweet import tweet

def main():
  file_class = "train"
  tweets, dictionary = parseTweets(file_class)




def parseTweets(file_class):
  tweet_filename = "../data/clintontrump.tweets." + file_class
  label_filename = "../data/clintontrump.labels." + file_class

  dictionary = {}
  tweets = []

  with open(tweet_filename) as f:
    text = f.readlines()

  print "Parsing Tweets"
  for raw_text in text:
    new_tweet = tweet(raw_text)
    tweets.append(new_tweet)


    for token in new_tweet.tokens:
      if token in dictionary:
        dictionary[token] += 1
      else:
        dictionary[token] = 1

  print "Adding Labels"
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

  return tweets, dictionary




if __name__ == '__main__':
  main()