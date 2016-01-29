#string = "olly olly in come free"
'''def words(string):
  words = {}
  for word in string:
    if word not in words:
      words[word] = 1
    elif word in words:
      words[word]+= 1
  return words'''
  
def words(string):
	phrase = {}
	for word in string.split():
		if phrase.get(word):
			phrase[word] += 1
		else:
		  try:
		    phrase[int(word)] = 1
		  except (TypeError, ValueError) as e:
		    phrase[word] = 1
	return phrase