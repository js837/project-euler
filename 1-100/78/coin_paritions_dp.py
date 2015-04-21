lookup={}

def k_partitions(k,n,mod):

  # Populate the table
  for n_i in xrange(1,n+1):
    t=0
    for k_i in xrange(1,n_i+1):
      #print k_i,n_i
      if k_i==1 or k_i==n_i:
        t=(t+1)%mod
      else:
        t=(t+lookup[(min(k_i,n_i-k_i),n_i-k_i)])%mod
      lookup[(k_i,n_i)]=t
  return lookup[(k,n)]
      
    
n=1
while k_partitions(n,n,1000000)!=0:
  n+=1
print n
