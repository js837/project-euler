import math
solsMax=0
solsMaxp=0
for p in xrange(12,1000,2):
  sols=0
  for b in xrange(1,p):
    for a in xrange(1,b+1):
      if not (a%2==1 and b%2==1):
        if p**2 == 2*(p*(a+b)-a*b):
          print p,a,b
          sols+=1
  if sols>solsMax:
    solsMax=sols
    solsMaxp=p
          
print solsMaxp    
    
  
