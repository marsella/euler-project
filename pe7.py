import pe3

# find the nth prime
# this prime-finding algorithm I wrote is really handy
# I went ahead and started with 2.
def findnth(n):
  ctr = 1
  i = 1
  while ctr < n:
    i += 2 #skip evens. 
    if pe3.isprime(i):
      ctr += 1
  print i
