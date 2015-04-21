def euclid(n,m):  
  r=-1
  while r!=0:
    r=n%m
    q=(n-r)/m
    n=m
    m=r 
  return n

def lcm(n,m):
  return m*n/euclid(n,m)

def lcm2(num_list):
  lcm2=1
  for n in num_list:
    lcm2=lcm(lcm2,n)
  return lcm2
    
print lcm2(list(xrange(1,21)))
