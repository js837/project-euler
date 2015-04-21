max_sum=0

def digit_sum(n):
  result=0
  while n>0:
    result=result + (n % 10)
    n=n//10
  return result
    

for a in xrange(1,100):
  for b in xrange(1,100):
    max_sum=max(digit_sum(a**b),max_sum)

print max_sum
