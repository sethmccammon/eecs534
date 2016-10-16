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