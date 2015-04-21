import sys

import time
start_time = time.time()

def next_collatz(n):
  if n%2==0:
    return n/2
  else:
    return 3*n+1

def next_collatz(n):
  if n%2==0:
    n=n/2
  else:
    n=3*n+1

d={}
def rec_col_len(n): #125.052000046 seconds
  if n==1:
    return 1
  else:
    if n%2==0:
      t=n/2
    else:
      t=3*n+1
    return d.setdefault(n,rec_col_len(t)+1)

# Improvements
# - Memoisation


def memo_col_len(n): #58.7120001316 seconds
  return d.setdefault(n,col_length(n))
  
def col_length(n): #36.6949999332 seconds
  col_len=1
  while n!=1:
    col_len=col_len+1
    if n%2==0:
      n=n/2
    else:
      n=3*n+1
  return col_len

mx=[0,0]
for i in xrange(1,1000000):
  if i%100000==0: print str(i/10000)+'%' ;
  t=memo_col_len(i)
  if t>mx[1]:
    mx[0]=i
    mx[1]=t
print mx[0]
print time.time() - start_time, "seconds"
