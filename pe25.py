# this is the initital brute-force which happens to work very well.
# even though it isn't particularly sexy
# projecteuler.net/problem=25

a = b = 1
x = 0
count = 2
while len(str(x)) < 1000:
  x = a + b
  a = b
  b = x
  count += 1
print count


