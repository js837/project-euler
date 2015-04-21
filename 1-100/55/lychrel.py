def isLychrel(n):
  i=1
  while i<50:
    new=str(int(str(n)[::-1])+n)
    newrev=new[::-1]
    #print new, newrev,i
    if newrev==new:
      return (False,i)
    n=int(new)
    i+=1
  return (True,i)

num=0
for i in xrange(1,10000):
  if isLychrel(i)[0]:
    #print i
    num+=1
print num
