#Toy function largely from Homework 1, checks for illegal characters
#Adding more error checking to handle additional cases that might not produce expected output

def sanitize(sentence: str) -> str:
  from string import ascii_lowercase, ascii_uppercase
  import string

  for i in sentence:
    if not i:
      return 'FAIL'

    if i in string.digits:
      return 'FAIL'

    if i in string.punctuation:
      return 'FAIL'

    if string.whitespace in i:
      return 'FAIL'
          
  output = sentence
  return 'PASS'

def test_set_cap():
  import random
  import sys
  import string
  from string import ascii_lowercase, ascii_uppercase
  
  test_set = ["12345a", "$avc", ",abc", ".baec"]
  
  while (len(test_set) < 50):
    entry = []
    i = random.randint(2, 40)
    while (i > 0):
      entry.extend(string.printable[random.randint(0, 99)])
      i = i - 1
    entry.extend(string.punctuation[random.randint(0,31)])
    random.shuffle(entry)
    entry = "".join(entry)
    test_set.append(entry)    

  random.shuffle(test_set)
  return test_set

