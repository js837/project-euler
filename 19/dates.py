year=1900
month = 1
weekday=1 # Monday

def isLeapYear(year):
  if year%4==0:
    result=True
    if year%100==0:
      result=False
      if year%400==0:
        result=True
      else:
        pass
    else:
      pass
  else:
    result=False
  return result

def daysInMonth(month,year):
  month30 = [9,4,6,11]
  if month == 2:
    if isLeapYear(year):
      return 29
    else:
      return 28
  elif month in month30:
    return 30
  else:
    return 31
  
count=0
while year < 2001:
  while month <=12 and year < 2001:
    days = daysInMonth(month,year)
    for day in xrange(1,days+1):
      if year>=1901 and weekday==0 and day==1:
        print (year,month,day,weekday)
        count=count+1
      weekday=((weekday+1)%7)
    month=month+1
    if month ==13:
      month=1
      year = year+1      
   
