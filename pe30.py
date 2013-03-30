# project euler 30
# sum of powers of digits

POWER = 5
UPPER_BOUND = 900000 # how to find this?

digits = [i**POWER for i in range(10)]

def sumofdigits(i):
  return sum([digits[int(n)] for n in str(i)])
  
sums = [sumofdigits(i) for i in range(UPPER_BOUND)]
for i in range(UPPER_BOUND):
  if sums[i] != i:
    sums[i] = 0

print sum(sums) - 1






