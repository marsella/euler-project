from math import ceil

DIM = 1001
c = 1
s = 1
for lvl in range(1,int(ceil(DIM/2))+1):
  inc = 2 * lvl
  for i in range (0,4):
    c += inc
    s += c

print s

