# how many firsts of the months were Sundays in the 20th century?
# http://projecteuler.net/problem=19

START_YEAR = 1901
END_YEAR   = 2001

def firsts():
  days_in_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  num_sundays = 0
  days = -5 # 1901 starts on a Tues
  for i in range(START_YEAR, END_YEAR):
    # Feb gets extra day for leap year
    if is_leap_year(i): days_in_year[1] = 29
    else: days_in_year[1] = 28

    for m in range(12):
      if days % 7 == 0:
        num_sundays += 1
      days += days_in_year[m]
    days %= 7

  print num_sundays

def is_leap_year(y): return (not y % 400) or (y % 100) or (not y % 4)

firsts()
