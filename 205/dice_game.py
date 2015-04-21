from operator import mul
from math import factorial

def product(tup):
    p = 1
    for i in tup:
        p *= i
    return p

def no_pos(comb):
  l=len(comb)
  return factorial(l)//product(factorial(comb.count(x)) for x in xrange(1,l+1))

p_dist={}

for i1 in xrange (1,5):
  for i2 in xrange (i1,5):
    for i3 in xrange (i2,5):
      for i4 in xrange (i3,5):
        for i5 in xrange (i4,5):
          for i6 in xrange (i5,5):
            for i7 in xrange (i6,5):
              for i8 in xrange (i7,5):
                for i9 in xrange (i8,5):
                  tup=(i1,i2,i3,i4,i5,i6,i7,i8,i9)
                  t=no_pos(tup)
                  if sum(tup) not in p_dist:
                    p_dist[sum(tup)]=t
                  else:
                    p_dist[sum(tup)]+=t
  


c_dist={}

for i1 in xrange (1,7):
  for i2 in xrange (i1,7):
    for i3 in xrange (i2,7):
      for i4 in xrange (i3,7):
        for i5 in xrange (i4,7):
          for i6 in xrange (i5,7):
            tup=(i1,i2,i3,i4,i5,i6)
            t=no_pos(tup)
            if sum(tup) not in c_dist:
              c_dist[sum(tup)]=t
            else:
              c_dist[sum(tup)]+=t

s=0
for p_key in sorted(p_dist.keys()):
  for c_key in sorted(c_dist.keys()):
    if p_key > c_key:
      s+=p_dist[p_key]*c_dist[c_key]

print round(float(s)/float(4**9*6**6),7)
