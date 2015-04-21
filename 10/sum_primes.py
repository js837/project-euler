# Header for Project Euler Projects
import sys,time
sys.path.append("C:\Users\Jake\Dropbox\Project Euler\libs")
start_time = time.time()

from jake_lib import is_prime

# Note: could use sieve of Eraosthenes or Legendre method

sum=0
for i in xrange(1,100):
  if is_prime(i):
    sum=sum+i
print sum


# Footer for Project Euler Projects
print time.time() - start_time, "seconds"
