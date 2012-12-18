#find the sum of all primes below 2 million
# below 10 = 17

import pe3

def sumprimes(k):
  sum = 2
  i = 3
  while i < k:
    # trying to speed it up by not calling isprime as often
    if i % 3 != 0 and pe3.isprime(i):
      sum += i
    i += 2
  print sum
