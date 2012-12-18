# find the pythagorean triplet (a^2 + b^2 = c^2) such that a + b + c = 1000
# return a * b * c

# for any two n, m we have
# a = n^2 - m^2
# b = 2nm
# c = n^2 + m^2
# so we want to find n, m such that m = n - (500 / n)
def findnm(k):
 n = 1
 two = float(2)
 while n < 1000:
   m = (k / (two * n)) - n
   if m > 0 and m < n and  (k / (2 * n)) - n == m:
     triple(m, n)
     break
   n += 1



def triple(m, n):
  a = n * n - m * m
  b = 2 * n * m
  c = n * n + m * m
  print a, b, c 
  print "sum: ", a+b+c
  print "product: ", a*b*c
