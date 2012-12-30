# collatz sequence
# find the longest chain starting under 1000000

# save chain lengths under k to reduce computation time
# start at k / 2 because every number n in the lower half has a corresponding
# 2n in the top half
def collatz(k):
  colz = [-1 for i in range(k)]
  colz[1] = 1

  i = k / 2
  if i % 2 == 0: i += 1
  while i < k:
    clen(colz, i)
    i += 2
  print colz.index(max(colz))

# find the collatz length of a given number
def clen(colz, i):
  if i < len(colz) and colz[i] != -1:
    rval = colz[i]
  elif i % 2:
    rval = 1 + clen(colz, 3 * i + 1)
  else:
    rval = 1 + clen(colz, i / 2)
  # save it
  if i < len(colz):
    colz[i] = rval
  return rval
