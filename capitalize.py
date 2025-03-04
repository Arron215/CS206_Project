#Toy function from Homework 1, capitalizes an inputted string

def capitalize(sentence: str) -> str:
  from string import ascii_lowercase, ascii_uppercase
  
  if not sentence:
  return ""
