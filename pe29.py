# project euler 29
# how many distinct terms are produced by a^b, 2 <= a,b <= 100

CUTOFF = 101

# sexy python brute solution
# calculates all, removes duplicates with set
print len(set(a**b for a in range(2, CUTOFF) for b in range(2, CUTOFF)))

# annoying but thoughtful solution
# removes duplicates of the form (a^i)^(b/i), where i|b
# then throws out some other duplicates that I didn't find
SENTINEL = -1
ZERO = 0

def index_2d(a, b):
  return a * CUTOFF + b

vals = [ZERO for j in range(CUTOFF * CUTOFF)]

for a in range(2, CUTOFF):
  for b in range(2, CUTOFF):
    vals[index_2d(a, b)] = a ** b
    if vals[index_2d(a, b)] != SENTINEL:
      vals[index_2d(a, b)] = a ** b

      #prevents most duplicates
      i = 2
      while a**i < CUTOFF:
        if b % i == 0:
          vals[index_2d(a**i, b/i)] = SENTINEL
        i += 1

vals = filter(lambda v: v != SENTINEL and v != ZERO, vals)
#remove more duplicates
vals = set(vals)
print len(vals)
    
