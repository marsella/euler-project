#sum of amicable numbers
#project_euler.com/problem=21


def sumam(n):
  d = sumdivisors(n + 1)
  ct = 0
  for i in range(n):
    if d[d[i]] == i:
      ct += i
  return ct

def sumdivisors(n):
  d = [0 for i in range(n)]
  for i in range(1, n):
    ct = 0
    for j in range(1, i/2 + 1):
      if not i % j: ct += j
    d[i] = ct
  return d
