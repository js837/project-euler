# Gives number of digits in recurring part of fraction 1/q
def num_reccurring(q):
  p=1
  prev_digits={}
  i=1
  while True:
    digit=p*10//q
    p=p*10-digit*q   
    if p in prev_digits:
      a=prev_digits[p]
      b=i
      return b-a
    else:
      prev_digits[p]=i
    i+=1

max_recurring=0
d=1
for q in xrange(2,1000):
  t=num_reccurring(q)
  if t > max_recurring:
    d=q
    max_recurring=t
    
  
  
print d
