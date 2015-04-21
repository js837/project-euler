import jake_lib as lib

k=2
count=0
ratio=1
while ratio>=0.1:
  if lib.is_prime(4*k**2-10*k+7):
    count+=1
  if lib.is_prime(4*k**2-8*k+5):
    count+=1
  if lib.is_prime(4*k**2-6*k+3):
    count+=1
  ratio = float(count)/float(4*(k-1)+1)
  #print count, 4*(k-1)+1
  k+=1
print 2*k-3
