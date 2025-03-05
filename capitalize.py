#Toy function largely from Homework 1, capitalizes an inputted string
#Adding more error checking to handle additional cases that might not produce expected output

def capitalize(sentence: str) -> str:
  from string import ascii_lowercase, ascii_uppercase
  
  if not sentence:
    return ""

  #check if we are trying to capitalize a number
  #if 
  
  lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
  return print(lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:])

def capitalize_no_string(sentence):
  from string import ascii_lowercase, ascii_uppercase
  
  if not sentence:
    return ""

  #check if we are trying to capitalize a number
  #if 
  
  lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
  return print(lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:])

import random
import sys
import string
from string import ascii_lowercase, ascii_uppercase

test_set_success = ["i am a cherry pie", "happy and i know it", "where is the candy", "can i have some", "abcde", "efgh", "poppyseed"]
test_set_fail = ["12345a", "$avc", "", ",abc", ".baec", " "]

test_set = test_set_success
test_set.extend(test_set_fail)
test_set.extend(string.printable)
print(test_set)
print("\n")

random.shuffle(test_set)
print(test_set)

