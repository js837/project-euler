from fractions import gcd
tp=1
tq=1
for p in xrange(10, 100):
  for q in xrange(10,100):
    r=float(p)/float(q)
    strp=str(p)
    strq=str(q)
    if q%10!=0 and p%11!=0 and p<q:
      if abs(float(strp[0])/float(strq[1])-r)<0.000001 and strp[1]==strq[0] or \
         abs(float(strp[1])/float(strq[0])-r)<0.000001 and strp[0]==strq[1]:
           tp*=p
           tq*=q
           d=gcd(tp,tq)

print tq//d
      
      
