import jake_lib as lib

prime_list=[]
for i in xrange(2,1000000):
  if lib.is_prime(i):
    prime_list.append(i)

print 'done prime list'

a=0
b=1
while b<=1000000:
  if lib.is_prime(sum(prime_list[a:b])):
    b=b+1
  else:
    a=a+1
    b=a+1

 
  
  
