import nltk, math, string
from tweet import tweet
from utils import dictionaryLookup
from bernoulli import BernoulliModel, BernoulliPredict, BernoulliTest
from multinomial import MultinomialModel, MultinomialPredict, MultinomialTest

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
  print "Test accuracy: ", BernoulliTest(test_prediction,test_tweets)

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
  print "Test accuracy: ", MultinomialTest(test_prediction,test_tweets)




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