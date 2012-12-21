#
# what is the smallest possible number that is divisible by all the numbers from
# 1 to 20?
#

# n > 1
def divisible(n):
  k = n * (n - 1)
  nums = [n - p for p in range(0, n/2)]
  found = True
  while True:
    for i in nums:
      if k % i != 0:
        found = False
        break
    if found == True:
      print "FOUND IT:", k
      break
    found = True
    k += 20
  print "DONE"
