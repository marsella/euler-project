# project euler 30
# sum of powers of digits
# now with upper bounds and enumerations

POWER = 5
digits = [i**POWER for i in range(10)]

# upper bound calculations
numdigits = 1
while numdigits * digits[9] > 10**numdigits:
  numdigits += 1
UPPER_BOUND = digits[9] * numdigits

def sumofdigits(i):
  return sum([digits[int(n)] for n in str(i)])
  
sums = [sumofdigits(i) for i in range(UPPER_BOUND)]
answers = [i for i,x in enumerate(sums) if i == x]

print sum(answers) - 1

