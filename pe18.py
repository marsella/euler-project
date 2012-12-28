# triange path-sum

# something is going on with triange orientation.
# figure that out.
def readdata(n):
  triangle = [[-1 for j in range(n)] for k in range(n)]
  f = open('pe18.dat', 'r')
  i = 0
  for line in f:
    arr = str.split(line, ' ')
    for x in range(len(arr)):
      triangle[i][x] = arr[x]
    i += 1
  # str to int
  for j in range(i):
    for k in range(j + 1):
      if len(triangle[j][k]) == 3:
        triangle[j][k] = triangle[j][k][:2]
      triangle[j][k] = int(triangle[j][k])

  return triangle


def pathsum(tri):
  n = len(tri)
  sums = [[-1 for i in range(n)] for j in range(n)]
  sums[0][0] = tri[0][0]

  print max(maxsum(tri, sums, n - 1, k) for k in range(n))


def maxsum(tri, sums, i, j):
  if i < 0 or j < 0 :
    return 0
  if sums[i][j] != -1:
    return sums[i][j]
  n = tri[i][j] + max(maxsum(tri, sums, i - 1, j - 1),
                      maxsum(tri, sums, i - 1, j))
  sums[i][j] = n
  return n

def main():
  tri = readdata(15)
  pathsum(tri)
