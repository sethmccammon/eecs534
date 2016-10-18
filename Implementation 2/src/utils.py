def cleanTokens(tokens):
  #removes urls from lists of tokens
  res = []
  blacklist = ["https", 't.co']
  for item in tokens:
    for item2 in blacklist:
      if item2 in item:
        break
    else:
      res.append(item.lower())

  return res


def dictionaryLookup(key, d):
  try:
    return d[key]
  except LookupError:
    return 0


def topTen(probs_hillary,probs_donny):
  print "TOP TEN WORDS"
  print "HILLARY  ||  DONNY"
  for i in range(10):
    print sorted(probs_hillary,key=probs_hillary.get,reverse=True)[i],"  ||  ", sorted(probs_donny,key=probs_donny.get,reverse=True)[i]


  return 0
