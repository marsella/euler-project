#sum of amicable numbers
#project_euler.com/problem=21


def sumam(n):
  dv = [0 for i in range(n)]
  for i in range(1, n):
    dv[i] = sumdivisors(i)
  ct = 0
  for i in range(n):
    if i == 220 or i == 284:
      print d(d(i, dv), dv)
    if d(d(i, dv), dv) == i and i != d(i, dv):
      ct += i
  return ct

def d(n, dv):
  if n < len(dv):
    return dv[n]
  return sumdivisors(n)

#sexify me
def sumdivisors(n):
  ct = 0
  for j in range(1, n/2 + 1):
    if not n % j: ct += j
  return ct

