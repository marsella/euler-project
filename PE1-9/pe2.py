# find sum of even-valued terms of the fibonacci sequence under 4 mil.

# every third number in the fibonacci sequence is even.
def fib(k):
  a = b = 1
  sum = 0
  while b < k:
    c = a + b
    sum += c
    a = b + c
    b = a + c
  print sum
      
