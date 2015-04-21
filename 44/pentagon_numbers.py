import math

def pentagonal(n):
  return n*(3*n-1)//2

def is_pentagonal(n):
  t=(1+math.sqrt(1+24*n))/6.0
  if abs(math.floor(t)-t)<0.0000001:
    return int(t)
  else:
    return False

D_min=100000000000000000000

for j in xrange(1020,2000):
  for k in xrange(j,3000):
    p_sum=pentagonal(j)+pentagonal(k)
    p_diff=abs(pentagonal(j)-pentagonal(k))

    if is_pentagonal(p_sum) and is_pentagonal(p_diff):
      print j,k
      D_min=min(D_min,p_diff)

print D_min
