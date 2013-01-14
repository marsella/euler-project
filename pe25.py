# this is the initital brute-force
# I'm sure there's a formula for the ith Fibonacci number but I'm on a plane
# TO BE UPDATED
# projecteuler.net/problem=25

a = b = 1
x = 0
count = 2
while len(str(x)) < 1000:
  x = a + b
  a = b
  b = x
  count += 1
print b, count


