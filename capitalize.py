#Toy function largely from Homework 1, capitalizes an inputted string
#Adding more error checking to handle additional cases that might not produce expected output

def capitalize(sentence: str) -> str:
  import string

  #Add options(?) for turning on and off the checks
  
  if not sentence:
    return ""

  if (sentence[0] in string.digits) or (sentence[0] in string.hexdigits) or (sentence[0] in string.octdigits):
    print("is digit")
    return ""

  if sentence[0] in string.punctuation:
    print("is punctuation")
    return ""

  if sentence[0] in string.whitespace:
    print("is whitespace")
    return ""
          
  lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
  return print(lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:])

def capitalize_no_string(sentence):
  import string
  
  if (sentence[0] in string.digits) or (sentence[0] in string.hexdigits) or (sentence[0] in string.octdigits):
    print("is digit")
    return ""

  if sentence[0] in string.punctuation:
    print("is punctuation")
    return ""

  if sentence[0] in string.whitespace:
    print("is whitespace")
    return ""
  
  lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
  return print(lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:])

def test_set_cap
  import random
  import sys
  import string
  from string import ascii_lowercase, ascii_uppercase
  
  test_set_success = ["i am a cherry pie", "happy and i know it", "where is the candy", "can i have some", "abcde", "efgh", "poppyseed"]
  test_set_fail = ["12345a", "$avc", "", ",abc", ".baec", " "]
  
  test_set = test_set_success
  test_set.extend(test_set_fail)
  test_set.extend(string.printable)
  return test_set

random.shuffle(test_set)
print(test_set)

