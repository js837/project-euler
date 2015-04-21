import math
import jake_lib as lib

n=3
while True:
  flag=False
  if not lib.is_prime(n):
    limit=int(math.sqrt(float(n)/float(2)))
    for k in xrange(1,limit+1):
      if lib.is_prime(n-2*k**2):
        flag=True
    if flag==False:
      print n
      break
  n+=2
    
