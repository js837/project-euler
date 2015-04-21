import math

def isPowerFact(n):
  t=n
  tot=0
  while t>0:
    dig=t%10
    tot=tot+math.factorial(dig)
    #print tot
    t=(t-dig)//10
  if n==tot:
    return True
  else:
    return False

sum=0  
for n in xrange(10,100000000):
  if isPowerFact(n):
    sum=sum+n

print sum
