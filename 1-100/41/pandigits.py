import jake_lib as lib
import math

def isPanDigital(n):
  ndigits=int(math.log10(abs(n)))+1
  digits=set()
  while n>0:
    dig=n%10
    if dig>ndigits or dig==0:
      return False
    digits.add(dig)
    n=(n-dig)//10
  if ndigits == len(digits):
    return True
  else:
    return False
  
for i in xrange(987654321,0,-2):
  if lib.is_prime(i):
    if isPanDigital(i):
      print i
      break
