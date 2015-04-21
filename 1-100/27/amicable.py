# Import Lib
import sys
sys.path.append('C:\Users\Jake\Dropbox\Project Euler\libs')
import jake_lib as lib
import math

max_abs_a=1000
max_abs_b=1000

# Note not as efficient as sieve
prime_list=[2]
for i in xrange(3,max_abs_b,2):
  if lib.is_prime(i):
    prime_list.append(i)

large=0
for b in prime_list:
  for a in xrange(-max_abs_a+1,max_abs_a,2):
    if (a**2-4*b < 0 or abs(math.floor(math.sqrt(a**2-4*b))-math.sqrt(a**2-4*b)) > 0.0001) and 1+a+b>0:
      n=0
      while lib.is_prime(n**2+a*n+b):
        n=n+1
      if n>large:
        large=n
        large_a=a
        large_b=b

print large_a*large_b

  
  




