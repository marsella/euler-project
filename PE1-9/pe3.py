# find largest prime factor

import random
import math

# this brute-force algorithm is fairly slow.
def gpf(k):
  i = 1
  while i < k:
    if k % i == 0:
      n = k / i
      if isprime(n):
        return n
    i += 1
    
# what if I just factor it? then every factor will be prime.
# way faster!!
def gpfv2(k):
  if isprime(k): return k
  i = 2
  while i * i < k:
    if k % i == 0:
      a = gpfv2(i)
      b = gpfv2(k / i)
      if a > b: return a
      else: return b
    i += 1

############################################################################

# well gee. this is a lot like the crypto stuff I did earlier this year.
# I probably need a primality tester.
# I'll translate the one I wrote in c++
def isprime(k, t=20):
  random.seed()
  while t > 0:
    # random element generator gets r st 0 < r < k
    # acts as witness that k is prime
    rand = math.floor(random.random() * (k-1) + 1)
    if egcd(rand, k) != 1:
      return 0
    if modexp(k, rand, k-1) != 1:
      return 0
    t -= 1
  return 1
  
# greatest common denominator with dijkstra's algorithm
def gcd(a, b): 
  if a > b:
    return gcd(a-b, b)
  elif a < b:
    return gcd(a, b-a)
  else:
    return a

# gcd with extended euclidean algorithm
# dijkstra's algorithm had too much recursion.
def egcd(a, b):
  if a % b == 0:
    return b
  else:
    q = a / b
    r = a % b
    return egcd(b, r)

# modular exponent: a^b mod N
def modexp(N, a, b):
  if b == 1:
    return a
  elif b == 0:
    return 1
  else:
    if b % 2 == 0:
      t = modexp(N, a, b/2)
      return (t * t) % N
    else:
      t = modexp(N, a, (b - 1) / 2)
      return (a * t * t) % N

