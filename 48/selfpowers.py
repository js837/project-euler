sum=0
for i in xrange(1,1001):
  sum=(sum+i**i)%10000000000

print sum
