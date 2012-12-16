#
# find the difference of the sum of the squares and the square of the sums of
# the first 100 natural numbers
#

def diff(n):
  s1 = sumofsq(n)
  s2 = sqofsums(n)
  print s2-s1

def sumofsq(n):
  sum = 0
  for i in range(0, n + 1):
    sum += i * i
  return sum


def sqofsums(n):
  sum = 0
  for i in range(0, n + 1):
    sum += i
  return sum * sum

