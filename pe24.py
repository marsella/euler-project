# lexographical permutations
# projecteuler.net/problem=24

def lexo(seq):
  if len(seq) == 1:
    return seq
  else:
    toret = []
    for i in range(len(seq)):
      for x in lexo(seq[:i]+seq[i+1:]): 
        toret.append(seq[i] + x)
    return toret

import time

stime = time.time()
seq = [str(x) for x in range(10)]
final = lexo(seq)
print final[1000000 - 1]
print time.time() - stime

