## Jake Python Project Euler Library ##
# --- Import Lib ----
##import sys
##sys.path.append('C:\Users\Jake\Dropbox\Project Euler\libs')
##import jake_lib as lib


import math


def num_digits(n):
  if n == 0:
    return 1
  else:
    return int(math.log10(abs(n)))+1

def get_digits(n):
  if n<0:
    n=abs(n)
  digits=[]
  d=n%10
  digits.insert(0,d)
  while n>=10:
    n=(n-d)/10
    d=n%10
    digits.insert(0,d)
  return digits

def get_factors(n):
  factors=set()
  i=1
  while i*i<=n:
    if n%i==0:
      factors.add(i)
      factors.add(n/i)
    i=i+1
  return factors



def is_prime(n):
  if n<0:
    return False
  if n==2:
    return True
  if n==1 or n%2==0:
    return False
  limit=int(math.sqrt(n))
  for factor in xrange(3,limit+1,2):
    if n%factor==0:
      return False
  return True

def get_prime_factors(n):
  if n == 1:
    return []
  factors=[]
  while n%2==0:
    factors.append(2)
    n=n//2
  p=3
  limit=int(math.sqrt(n))
  while p<= limit:
    if n%p==0:
      factors.append(p)
      n=n//p
    else:
      p=p+2
  if n!=1:
    factors.append(n)
  return factors

def euclid(n,m):
  r=-1
  while r!=0:
    r=n%m
    q=(n-r)/m
    n=m
    m=r
  return n

def lcm(n,m):
  return m*n/euclid(n,m)
