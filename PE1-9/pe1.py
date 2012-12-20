#
# problem 1: find the sums of the natural numbers under 1000 that are
# multiples of 3 or 5. 
#

# hmm... I'll just go through and find them all!
def sumv1(n):
  sum = 0
  for i in range(0, n):
    if i % 5 == 0 or i % 3 == 0:
      sum += i
  return sum

# better: use properties of arithmetic sequences
def sumv2(k):
  nums = [3, 5, 15]
  sums = [0 for i in range(3)]
  i = 0
  while i < 3:
    n = (k - 1) / nums[i]
    an = nums[i] * n
    sums[i] = n * (nums[i] + an) / 2  # fun with integer division
    i += 1
  return sums[0] + sums[1] - sums[2]
