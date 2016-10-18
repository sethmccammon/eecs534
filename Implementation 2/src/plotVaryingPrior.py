import matplotlib.pyplot as plt
from bernoulli import BernoulliModel, BernoulliPredict, BernoulliTest
from multinomial import MultinomialModel, MultinomialPredict, MultinomialTest
from tweet import tweet,parseTweets

def plotPriors():
  bernoulli_accuracies=[]
  multinomial_accuracies=[]
  for ii in range(-5,1):
    print "ITERATION=",6+ii
    alpha=10.**ii

    file_class = "train"
    tweets, dictionary = parseTweets(file_class)
    probs_donny, probs_hillary, p_hillary,p_donald=BernoulliModel(tweets,dictionary,alpha)

    #test on test data
    file_class="dev"
    test_tweets,test_dictionary=parseTweets(file_class)
    # probs_donny, probs_hillary, p_hillary,p_donald=BernoulliModel(tweets,dictionary,alpha)
    test_prediction = BernoulliPredict(test_tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
    bernoulli_accuracies.append(BernoulliTest(test_prediction,test_tweets))
    # print "Test accuracy: ", BernoulliTest(test_prediction,test_tweets)

    #now do it for multinomial cases
    file_class = "train"
    tweets, dictionary = parseTweets(file_class)
    probs_donny, probs_hillary, p_hillary,p_donald=MultinomialModel(tweets,dictionary,alpha)

    #test on test data
    file_class="dev"
    test_tweets,test_dictionary=parseTweets(file_class)
    # probs_donny, probs_hillary, p_hillary,p_donald=BernoulliModel(tweets,dictionary,alpha)
    test_prediction = MultinomialPredict(test_tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
    multinomial_accuracies.append(BernoulliTest(test_prediction,test_tweets))

  
  plt.title('Alpha values vs. Accuracies for Bernoulli and Multinomial Models')
  alphas=[10.**-5.,10.**-4.,10.**-3.,10.**-2.,10.**-1.,10.**0.]
  plt.semilogx(alphas,bernoulli_accuracies,'r-',label='bernoulli')
  plt.semilogx(alphas,multinomial_accuracies,'b-',label='multinomial')

  plt.xlabel('Alpha values')
  plt.ylabel('Accuracies (as percentages)')
  plt.legend()
  plt.show()

  # plt.semilogx(alphas,multinomial_accuracies)
  # plt.show()
    #multiomial
    # file_class="train"
    # tweets, dictionary = parseTweets(file_class)
    # probs_donny, probs_hillary, p_hillary,p_donald=MultinomialModel(tweets,dictionary)

    # # predict multinomial
    # prediction = MultinomialPredict(tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
    # print "Training accuracy: ", MultinomialTest(prediction,tweets)

    # #test multinomial
    # file_class="dev"
    # test_tweets,test_dictionary=parseTweets(file_class)
    # test_prediction = MultinomialPredict(test_tweets,dictionary,probs_donny, probs_hillary, p_hillary,p_donald)
    # print "Test accuracy: ", MultinomialTest(test_prediction,test_tweets)