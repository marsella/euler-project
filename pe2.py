# find sum of even-valued terms of the fibonacci sequence under 4 mil.

def fib(k):
  a, b = 1, 2
  sum = 0
  while b < k: # b is always bigger
    if a % 2 == 0: sum += a
    if b % 2 == 0: sum += b
    a = a + b
    b = a + b
  print sum
