# find the sum of all numbers that cannot be written as the sum of two amicable numbers
#projecteuler.net/problem=23

from pe21 import d

def fctn():
  # all numbers above 28123 can be written as a sum
  # actually, the upper limit is lower than this
  x = 28124
  #abn = abundant. Lazy variable names aren't readable
  abn = []
  for i in range(x):
    if d(i) > i: abn.append(i)
  num = range(x)
  # removes the sums
  for i in abn: 
    for j in abn[abn.index(i):]:
      if i + j >= len(num): continue
      num[i + j] = 0
  print sum(num)


fctn()
