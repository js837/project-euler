import sys
sys.path.append("C:\Users\Jake\Dropbox\Project Euler\libs")

from jake_maths import is_prime

n=10001

i=2
count=0
last_prime=0

while count<n:
  if is_prime(i):
    count=count+1
    last_prime=i
    #print last_prime
  i=i+1

print last_prime
