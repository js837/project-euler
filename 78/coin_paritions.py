lookup={}

def k_partitions(k,n):
  # we have n-k coins to play with, each of k piles must contain >=1 coin

  #Reduce down
  i=2*k-n
  if i>0:
    k=k-i
    n=n-i

  if (k,n) in lookup:
    return lookup[(k,n)]
  
  if k>n:
    return 0
  if k==1 or k==n:
    return 1
  s=0
  for i in xrange(1,min(k+1,n-k+1)):
    t=k_partitions(i,n-k)
    lookup[(i,n-k)]=t
    s+=t
  return s

def partition(n):
  s=0
  for k in xrange(1,n+1):
    s+=k_partitions(k,n)
  return s 

#i=1
#while partition(i) % 1000000 != 0:
#  i+=1
#print i
