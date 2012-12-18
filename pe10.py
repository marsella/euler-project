#find the sum of all primes below 2 million
# below 10 = 17

import pe3

def sumprimes(k):
  sum = 2
  # I think 1 doesn't count
  i = 3
  while i < k:
  #for i in range(2, k):
    if(pe3.isprime(i)):
      sum += i
    i += 2
  print sum
