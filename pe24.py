# lexographical permutations
# projecteuler.net/problem=24

def lexo(seq):
  length = len(seq)
  if length == 1:
    return seq
  else:
    toret = []
    for i in range(len(seq)):
      val = seq[i]
      seq.remove(val)
      for x in lexo(seq):
        toret.append(val + x)
      seq.insert(i, val)
    return toret

seq = [str(x) for x in range(10)]
final = lexo(seq)
print final[1000000]




