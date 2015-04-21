import math,sys

for a in xrange(0,1000):
  for b in xrange(a,1000):
    if (1000-a-b)**2==a**2+b**2:
      print a*b*(1000-a-b)
      
      
      
