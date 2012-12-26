# max number of paths in a kxk grid

# can this be simplified?
def maxpaths(k):
  num = fact(2*k)
  kf = fact(k)
  print num / (kf * kf)

def fact(k):
  if k < 1:
    return 1
  return k * fact(k-1)

