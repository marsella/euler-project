
# What's the value of the first triangle number with over 500 divisors?

import math

# test triangles
def gettriangle(k):
  i = tri = 1
  while numfactor(tri) < k:
    i += 1
    tri += i
  print tri


# count factors
# slows down for larger numbers
def numfactor(k):
  count = 0
  for i in range(1, int(math.sqrt(k))):
    if k % i == 0:
      count += 2
  if int(math.sqrt(k)) == math.sqrt(k):
    count += 1
  return count
