# how many firsts of the months were Sundays in the 20th century?

def firsts():
  year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  sundays = 0
  days = -5 #1901 starts on a Tues
  for i in range(1901, 2001):
    if isleapyear(i): year[1] = 29
    else: year[1] = 28
    for m in range(12):
      if days % 7 == 0:
        sundays += 1
      days += year[m]
    days %= 7
  print sundays

def isleapyear(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  return False
