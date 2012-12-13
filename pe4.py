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
      if ispalindrome(i * j) and i * j > max:
        max = i * j
      j -= 1
    i -= 1
  print max

# this only works for 5 and 6 digit numbers. 
# there must be a way to generalize this.
def ispalindrome(k):
  if k < 10000 or k > 998001:
    return False
  if k < 100000: #5-digits
    if k / 10000 != k % 10:
      return False
    k = (k % 10000 - k % 10) / 10
    if k / 100 != k % 10:
      return False
  else:
    if k / 100000 != k % 10:
      return False
    k = (k % 100000 - k % 10) / 10
    if k / 1000 != k % 10:
      return False
    k = (k % 1000 - k % 10) / 10
    if k / 10 != k % 10:
      return False
  return True
