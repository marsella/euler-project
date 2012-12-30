# triange path-sum
# for problems 18 and 67

# the strategy is to work from the bottom, finding the max length of each 
# number in the last row. Finds these recursively, saving the max length for
# each number as it comes across them
def pathsum(tri):
  n = len(tri)
  sums = [[-1 for i in range(n)] for j in range(n)]
  print max(maxsum(tri, sums, n - 1, k) for k in range(n))

# the sum of any number (i, j) is the max of the sums of the two numbers
# above it (i - 1, j) and (i - 1, j - 1) plus the number itself
def maxsum(tri, sums, i, j):
  if i < 0 or j < 0: #out of bounds
    return 0
  if sums[i][j] != -1: #already calculated
    return sums[i][j]
  n = tri[i][j] + max(maxsum(tri, sums, i - 1, j - 1),
                      maxsum(tri, sums, i - 1, j))
  sums[i][j] = n
  return n

def main():
  tri = readdata()
  pathsum(tri)

#---------------
# reading in. this is still kind of clumsy.
def readdata(n = 100):
  triangle = [[-1 for j in range(n)] for k in range(n)]
  f = open('triangle.txt', 'r')
  i = 0
  for line in f:
    line = line.replace("\n", "")
    arr = str.split(line, ' ')
    for x in range(len(arr)):
      triangle[i][x] = int(arr[x])
    i += 1

  return triangle




