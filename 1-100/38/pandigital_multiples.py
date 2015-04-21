def is_pandigital(str_n):
  if len(str_n)!=9:
    return False
  for i in xrange(1,10):
    if str(i) not in str_n:
      return False
  return True
    

def is_concat_pandigital(n):
  result=''
  i=1
  while len(result) < 9:
    result+=str(i*n)
    i+=1
  
  if is_pandigital(result):
    return int(result)
  else:
    return False

m=0
for i in xrange(1,987654321//10003+1):
  t=is_concat_pandigital(i)
  if t:
    m=max(m,t)

print m
  
