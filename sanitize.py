#Toy function largely from Homework 1, checks for illegal characters
#Adding more error checking to handle additional cases that might not produce expected output

def sanitize(sentence: str) -> str:
  from string import ascii_lowercase, ascii_uppercase
  import string

  fail = 0

  for i in sentence:
    if not i:
      return 'FAIL'

    if i in string.punctuation:
      if (fail):
        return 'FAIL'
      else:
        fail = 0
      fail = 1

  for i in string.whitespace[0:]:
    if i in sentence:
      return 'FAIL'

  output = sentence
  return 'PASS'

def test_set_cap():
  import random
  import sys
  import string
  from string import ascii_lowercase, ascii_uppercase
  
  test_set = []
  
  while (len(test_set) < 10000):
    entry = []
    i = random.randint(2, 40)
    while (i > 0):
      entry.extend(string.printable[random.randint(0, 99)])
      i = i - 1
    entry.extend(string.punctuation[random.randint(0,31)]) #Makes sure the test set will fail
    entry.extend(string.punctuation[random.randint(0,31)])
    random.shuffle(entry)
    entry = "".join(entry)
    test_set.append(entry)    

  random.shuffle(test_set)
  return test_set

