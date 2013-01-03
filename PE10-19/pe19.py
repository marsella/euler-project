# how many firsts of the months were Sundays in the 20th century?
# http://projecteuler.net/problem=19

import datetime

START_YEAR = 1901
END_YEAR   = 2001
SUNDAY     = 6

def firsts():
  num_sundays = 0
  for y in range(START_YEAR, END_YEAR):
    for m in range(1, 13):
      if datetime.datetime(y, m, 1).weekday() == SUNDAY:
        num_sundays += 1
  print num_sundays

firsts()
