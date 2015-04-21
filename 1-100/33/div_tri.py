import sys
sys.path.append('C:\Users\Jake\Dropbox\Project Euler\libs')
import jake_lib as lib

def num_factors_tri(n):
  if n%2==0:
    factors=lib.get_prime_factors(n//2)+lib.get_prime_factors(n+1)
  else:
    factors=lib.get_prime_factors(n)+lib.get_prime_factors((n+1)//2)
  factors.sort()
  count=1
  last=factors[0]
  i=0
  for factor in factors:
    if factor==last:
      i=i+1
    else:
      count=count*(i+1)
      #print 'i:',i  
      i=1
      last=factor
  #print 'i:',i
  #return factors
  return count*(i+1)
    
  
t=2
while num_factors_tri(t)<500:
  t=t+1
print t*(t+1)//2
print 't=',t
