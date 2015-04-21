def has_3digit_factor(n):
  for i in xrange(100,1000):
    if n%i==0 and len(str(n/i))==3:
      return i
  return 0

cans=[]
for n in xrange(999,100,-1):
  str_n=str(n)
  pal=int(str_n+str_n[::-1])
  #print pal
  if has_3digit_factor(pal) !=0:
    cans.append(pal)
    
    
