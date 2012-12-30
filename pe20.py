# http://projecteuler.net/problem=20
# Just want to point out how BAD ASS this solution is
# <3 marshall

def factorial_digit_sum(n):
  fact = reduce(lambda x, y: x*y, range(1,n))
  return sum([int(s) for s in list(str(fact))])
print factorial_digit_sum(100)


