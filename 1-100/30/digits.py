def isPower(n,power):
  t=n
  tot=0
  while t>0:
    dig=t%10
    tot=tot+dig**power
    #print tot
    t=(t-dig)//10
  if n==tot:
    return True
  else:
    return False

sum=0  
for n in xrange(10,1000000):
  if isPower(n,5):
    sum=sum+n

print sum
