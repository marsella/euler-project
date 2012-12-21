#find the sum of all primes below 2 million
# below 10 = 17

# prime checking using a sieve
def sieve(k):
  nums = [1 for i in range(k)]
  nums[0] = nums[1] = 0
  for p in range(k):
    if nums[p] == 0: continue
    i = 2
    while p * i < k:
      nums[p * i] = 0
      i += 1
  return nums

def getsum(k):
  nums = sieve(k)
  sum = 0
  for i in range(k):
    if nums[i]:
      sum += i
  print sum 
