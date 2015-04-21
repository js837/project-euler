import jake_lib as lib
import math

def isCircular(n):
  ndigits=int(math.log10(abs(n)))+1
  #print ndigits
  if lib.is_prime(n):
    for i in xrange(ndigits-1):
      dig=n%10
      n=(n-dig)//10
      n=n+dig*10**(ndigits-1)
      #print n
      if not lib.is_prime(n):
        return False
    return True
  else:
    return False

sum=0  
for n in xrange(2,1000000):
  if isCircular(n):
    print n
    sum=sum+1

print sum
