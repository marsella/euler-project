

from pe21 import d

#doesn't work yet

def fctn():
  x = 28123
  x = 25
  abn = [d(i) > i for i in range(x/2 + 1)]
  num = range(x)
  # removes the sums of two abundant numbers within the range
  for i in range(len(abn)): 
    if not abn[i]: continue 
    for j in range(i, len(abn)):
      if not abn[j]: continue
      num[i + j] = 0
  print sum(num)


fctn()
print sum(range(24))
