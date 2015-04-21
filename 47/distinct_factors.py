import jake_lib as lib

i=3
run=0

while run<4:
  d_factors=set(lib.get_prime_factors(i))
  if len(d_factors)==4:
    run+=1
  else:
    run=0
  i+=1
  
print i-4
