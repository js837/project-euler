import jake_lib as lib
import math

def isPalPrime(n):
  ndigits=int(math.log10(abs(n)))+1
  #print ndigits
  if lib.is_prime(n):
    t=n
    for i in xrange(ndigits-1):
      dig=n%10
      n=(n-dig)//10
      #print n
      if not lib.is_prime(n):
        return False
    n=t
    #print n
    for i in xrange(ndigits-1):
      dig=n//10**(ndigits-1-i)
      #print dig
      n=(n-dig*10**(ndigits-1-i))
      #print n
      if not lib.is_prime(n):
        return False
    return True
  else:
    return False

sum=0
sum1=0
for n in xrange(11,1000000):
  if isPalPrime(n):
    print n
    sum=sum+1
    sum1=sum1+n

print sum,sum1
