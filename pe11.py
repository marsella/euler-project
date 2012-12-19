# find the largest product of 4 numbers in a row.

def main():
  nums = getdata()
  findmax(nums)

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

# so ugly. but it works
def findmax(nums):
  max = -1
  #rows
  for i in range(20):
    for j in range(16):
      prod = 1
      for k in range(4):
        prod *= nums[i][j + k]
      if prod > max:
        max = prod
  #cols
  for i in range(16):
    for j in range(20):
      prod = 1
      for k in range(4):
        prod *= nums[i + k][j]
      if prod > max:
        max = prod
  #diag right
  for i in range(16):
    for j in range(16):
      prod = 1
      for k in range(4):
        prod *= nums[i + k][j + k]
      if prod > max:
        max = prod
  #diag left
  for i in range(4, 20):
    for j in range(16):
      prod = 1
      for k in range(4):
        prod *= nums[i - k][j + k]
      if prod > max:
        max = prod
  print max 


