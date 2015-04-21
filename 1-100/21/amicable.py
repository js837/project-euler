# Import Lib
import sys
sys.path.append('C:\Users\Jake\Dropbox\Project Euler\libs')
import jake_lib as lib

def div_sum(n):
  factors=lib.get_factors(n)
  factors.remove(n)
  return sum(factors)

div_sums={}
for i in xrange(1,10001):
  div_sums[i]=div_sum(i)

suma=0
for i in xrange(1,10001):
  t=div_sums[i]
  if t in div_sums:
    if div_sums[t]==i and i!=t:
      suma=suma+t+i
      print i,t

print suma/2  
  




