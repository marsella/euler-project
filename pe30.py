# project euler 30
# sum of powers of digits
# now with upper bounds and enumerations

POWER = 5
digits = [i**POWER for i in range(10)]

numdigits = 1
while numdigits * digits[9] > 10**numdigits:
  numdigits += 1
print numdigits
UPPER_BOUND = int('9' * numdigits) # this is very high. but it works

def sumofdigits(i):
  return sum([digits[int(n)] for n in str(i)])
  
sums = [sumofdigits(i) for i in range(UPPER_BOUND)]
answers = [i for i,x in enumerate(sums) if i == x]

print sum(answers) - 1






