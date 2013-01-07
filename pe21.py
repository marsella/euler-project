#sum of amicable numbers
#project_euler.com/problem=21

from math import sqrt

# sums amicable numbers up to BUT NOT INCLUDING n.
# took out precalculation because it's not that much faster
def sumam(n):
  ct = 0
  for i in range(n):
    if i != d(i) and d(d(i)) == i :
      ct += i
  return ct

def d(n):
  if n == 0: return 0
  ct = 1
  for j in range(2, 1 + int(sqrt(n))):
    if not n % j: 
      ct += j + n/j
      if j == n/j: ct -= j
  return ct

print sumam(10001)
