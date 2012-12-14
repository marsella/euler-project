# find the largest palindrome that can is the product of two three-digit
# numbers

import math

# BRUTE FORCE YEAHHH
def products():
  i = 999
  max = 0
# how to do sequence?
  nums = [p+100 for p in range(0, 900)]
  for i in nums:
    for j in nums:
      if ispalv2(i * j) and i * j > max:
        max = i * j
  print max

# cleaner palindrome verifier
def ispalv2(k):
  dig = len(str(k))  
  dig -= 1
  while(dig >= 1):
    if k / pow(10, dig) != k % 10:
      return False
    k = (k % pow(10, dig) - k % 10) / 10
    dig -= 2
  return True



