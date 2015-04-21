import jake_lib as lib
import math

s=''
i=1
while len(s)<1000000:
  s=s+str(i)
  i=i+1

prod=1
for i in xrange(0,7):
  prod=prod*int(s[10**i-1])
print prod
