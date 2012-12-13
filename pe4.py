# find the largest palindrome that can is the product of two three-digit
# numbers

import math

# BRUTE FORCE YEAHHH
def products():
  i = 999
  max = 0
  while i > 99:
    j = 999
    while j > 99:
      if ispalv2(i * j) and i * j > max:
        max = i * j
      j -= 1
    i -= 1
  print max

# cleaner palindrome verifier
def ispalv2(k):
  dig = len(str(k))  
  if True: # dig % 2 != 0:
    dig -= 1
    while(dig >= 1):
      if k / pow(10, dig) != k % 10:
        return False
      k = (k % pow(10, dig) - k % 10) / 10
      dig -= 2
  return True



