import math

def has_correct_form(n):
  t=str(n)
  for i in xrange(0,10):
    if t[2*i]!=str((i+1)%10):
      return False
  return True
    
for i in xrange(1010101010,1389026623,10):
  if has_correct_form(str(i**2)):
    print i
