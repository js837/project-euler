lookup={}

mod=1000000
n=100
k=n

# Populate the table and iterate
n_i=1
while True:
  t=0
  for k_i in range(1,n_i+1):
    #print k_i,n_i
    if k_i==1 or k_i==n_i:
      t=(t+1)%mod
    else:
      t=(t+lookup[(min(k_i,n_i-k_i),n_i-k_i)])%mod
    lookup[(k_i,n_i)]=t
  if lookup[(n_i,n_i)]==0:
    print(n_i)
    break
  n_i+=1
      
