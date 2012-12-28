# triange path-sum

def readdata(n):
  triangle = [[0 for i in range(n)] for j in range(n)]
  for j in range(n):
    for i in range(i + 1):
      triangle[i][j] = 1;
  triangle[2][0] = 4
  return triangle

def pathsum(tri):
  n = len(tri[0])
  sums = [[-1 for i in range(n)] for j in range(n)]
  sums[0][0] = tri[0][0]
  print max(maxsum(tri, sums, k, n - 1) for k in range(n))


def maxsum(tri, sums, i, j):
  if i < 0 or j < 0:
    return -1
  if sums[i][j] != -1:
    return sums[i][j]
  n = tri[i][j] + max(maxsum(tri, sums, i - 1, j - 1),
                         maxsum(tri, sums, i, j - 1))
  
  return n

def main():
  tri = readdata(4)
  pathsum(tri)
