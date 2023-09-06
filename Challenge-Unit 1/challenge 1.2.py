#1.2 leap year
def leap_year(year):
  if ( year % 4 == 0 & year % 100 != 0)| year % 400 == 0:
    return True
  else:
    return False
year=int(input("Enter the year:"))
if leap_year(year):
  print("{} is a leap year ".format(year))
else:
  print("{} is not a leap year".format(year))1111111111111111111111