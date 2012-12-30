# find the largest product of 4 numbers in a row.

def main():
  nums = getdata()
  findmax(nums)

# learning file i/o
def getdata():
  f = open("pe11.dat", "r")
  nums = [[] for i in range(20)]
  i = 0
  for line in f:
     nums[i] = line.split(' ')
     i += 1
  for i in range(20):
    for j in range(20):
      if len(nums[i][j]) == 3:
        nums[i][j] = nums[i][j][:2]
      nums[i][j] = int(nums[i][j])
  return nums

# this is unnecessarily complicated.
# assumes an entirely positive array
# assumes size 20x20
# prints the max of 4-number sequences
def findmax(nums):
  lmax = [0 for i in range(5)]
  lmax[0] = -1
  for i in range(20):
    for j in range(20):
      lmax[1] = r(nums, i, j) 
      lmax[2] = c(nums, i, j) 
      lmax[3] = dr(nums, i, j) 
      lmax[4] = dl(nums, i, j) 
      lmax[0] = max(lmax)
  print lmax[0] 

def r(nums, i, j):
  prod = -1
  if j < 17:
    prod = 1
    for k in range(4):
      prod *= nums[i][j + k]
  return prod

def c(nums, i, j):
  prod = -1
  if i < 17:
    prod = 1
    for k in range(4):
      prod *= nums[i + k][j]
  return prod

def dr(nums, i, j):
  prod = -1
  if i < 17 and j < 17:
    prod = 1
    for k in range(4):
      prod *= nums[i + k][j + k]
  return prod

def dl(nums, i, j):
  prod = -1
  if i > 4 and j < 17:
    prod = 1
    for k in range(4):
      prod *= nums[i - k][j + k]
  return prod

