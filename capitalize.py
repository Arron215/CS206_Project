#Toy function largely from Homework 1, capitalizes an inputted string
#Adding more error checking to handle additional cases that might not produce expected output

def capitalize(sentence: str) -> str:
  from string import ascii_lowercase, ascii_uppercase
  import string

  for i in sentence:
    if not i:
      return 'FAIL'

    if (i[0] in string.digits) or (i[0] in string.hexdigits) or (i[0] in string.octdigits):
      return 'FAIL'

    if i[0] in string.punctuation:
      return 'FAIL'

    if i[0] in string.whitespace:
      return 'FAIL'
          
    lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
    out = lower_to_upper.get(i[0], i[0]), i[1:]

  return 'PASS'

def test_set_cap():
  import random
  import sys
  import string
  from string import ascii_lowercase, ascii_uppercase
  
  test_set_success = ["i am a cherry pie", "happy and i know it", "abcde", "efgh", "poppyseed"]
  test_set_fail = ["12345a", "$avc", "", ",abc", ".baec", " "]
  
  test_set = test_set_success
  test_set.extend(test_set_fail)
  test_set.extend(string.printable)

  random.shuffle(test_set)
  return test_set

