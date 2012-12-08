# find sum of even-valued terms of the fibonacci sequence under 4 mil.

# huh. those mods sure are ugly.
def fib(k):
  a, b = 1, 2
  sum = 0
  while b < k: # b is always bigger
    if a % 2 == 0: sum += a
    if b % 2 == 0: sum += b
    a = a + b
    b = a + b
  print sum

# hold on. every third number in the fibonacci sequence is even.
def fibv2(k):
  a = b = 1
  sum = 0
  while(b < k):
    c = a + b
    sum += c
    a = b + c
    b = a + c
  print sum
      
