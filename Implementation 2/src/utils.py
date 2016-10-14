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