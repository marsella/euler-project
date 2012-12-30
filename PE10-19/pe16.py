# find the sum of the digits of a power

def sumpow(p, b=2):
  num = str(b ** p)
  sum = 0
  for i in range(len(num)):
    sum += int(num[i])
  print sum
