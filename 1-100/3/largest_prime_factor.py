import time
start_time = time.time()


import math


n=600851475143

def is_prime(n):
  if n==2:
    return True
  if n%2==0:
    return False
  limit=int(math.sqrt(n))
  for factor in xrange(3,limit+1,2):
    if n%factor==0:
      return False
  return True

def get_prime_factors(n):
  factors=[] 
  limit=int(math.sqrt(n))
  factor=2
  while factor<=limit:
    if n%factor==0:
      factors.append(factor)
      n=n/factor
    else:
      factor=factor+1
  if len(factors)==0:
    factors.append(n)
  return factors


print get_prime_factors(n)

  
  


print time.time() - start_time, "seconds"
