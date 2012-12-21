# collatz sequence
# find the longest chain starting under 1000000


# brute force
# save chain lengths under 1000000 to reduce computation time
def collatz(k):
  colz = [-1 for i in range(k)]
  colz[1] = 1

  for i in range(1, k):
    clen(colz, i)
  print colz.index(max(colz))


def clen(colz, i):
  rval = -1
  if i < len(colz) and colz[i] != -1:
    rval = colz[i]
  elif i % 2:
    rval = 1 + clen(colz, 3 * i + 1)
  else:
    rval = 1 + clen(colz, i / 2)

  if i < len(colz):
    colz[i] = rval
  return rval
