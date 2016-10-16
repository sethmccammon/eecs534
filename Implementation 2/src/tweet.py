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
    self.tokens = list(set(cleanTokens(raw_tokens)))
    