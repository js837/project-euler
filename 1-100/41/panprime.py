from jake_lib import num_digits, is_prime
import itertools

def is_pandigital(n):
  digits=set()
  n_digits=num_digits(n)
  max_digit=0
  for i in xrange(1,n_digits+1):
    digit=n%10
    max_digit=max(max_digit,digit)
    if digit in digits:
      return False
    else:
      digits.add(digit)
      n=n//10
  return max_digit==n_digits
    
for n in xrange(1,10):
  perms = itertools.permutations(range(1,n+1))
  for perm in perms:
    x=int(''.join(str(y) for y in perm))
    if is_prime(x):
      print x
  
  
