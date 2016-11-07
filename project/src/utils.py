def dictCombine(d1, d2):
  res = {}
  for item in d1:
    if item in res:
      res[item] += d1[item]
    else:
      res[item] = d1[item]

  for item in d2:
    if item in res:
      res[item] += d2[item]
    else:
      res[item] = d2[item]

  return res