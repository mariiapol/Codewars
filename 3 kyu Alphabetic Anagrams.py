from math import factorial, prod
from collections import Counter

def listPosition(word):
  #Return the anagram list position of the word.
    s = 0
    n = len(word)
    if n == 1:
        return 1
    else:        
        for letter in sorted(set(word)):
            if letter != list(word)[0]:
                #Use the integer division operator (//) to divide two numbers and round their quotient down to nearest integer.
                s += factorial(n-1)//find_prod(Counter(sorted(word)),letter)
                continue
            else:
                s+= listPosition(word[1:])
            return s
    
def find_prod(d,l):
    return prod([factorial(d[key]-1) if key == l else factorial(d[key]) for key in d])
