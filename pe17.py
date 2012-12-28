# how many letters used if the numbers from 1 to 1000 were written in words?

# first thought: program in the numbers that compose other numbers
# 1-9, 20, 30, 40, etc. Get the weirdos (10-19). Then build the rest.
def numletters(k = 1000):
  cts = [0 for i in range(k + 1)]
  # set the basics
  cts[1] = cts[2] = cts[6] = cts[10] = andd = 3
  cts[4] = cts[5] = cts[9] = 4
  cts[3] = cts[7] = cts[8] = cts[40] = cts[50] = cts[60] = 5
  cts[11] = cts[12] = cts[20] = cts[30] = cts[80] = cts[90] = 6
  cts[15] = cts[16] = cts[70] = hundred = 7
  cts[13] = cts[14] = cts[18] = cts[19] = 8
  cts[17] = 9
  cts[1000] = 11

  for i in range(k):
    if cts[i] == 0:
      cts[i] = cts[i / 10 * 10] + cts[i % 10]
      if i < 100: print i, cts[i]
    if i >= 100:
      cts[i] = cts[i / 100] + hundred 
      if i % 100 != 0:
        cts[i] += andd + cts[i % 100]
      print i, cts[i], '=', cts[i/100], '+ 10 +', cts[i % 100]

  print sum(cts[i] for i in range(k + 1))
