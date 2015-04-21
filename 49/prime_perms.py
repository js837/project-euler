import jake_lib as lib
import itertools

def is_arithmetic(list_n):
  list_n=sorted(list_n)
  diffs = [list_n[i]-list_n[i-1] for i in xrange(1,len(list_n))]
  if max(diffs)==min(diffs):
    return True
  else:
    return False

def has_arithmetic(list_n,size):
  for tup in itertools.combinations(list_n, size):
    #print tup
    if is_arithmetic(tup):
      return tup
  return False
    
  

d=dict()
p_list=list()

for i in xrange(1000,10000):
  if lib.is_prime(i):
    p_list.append(i)
    key=tuple(sorted(lib.get_digits(i)))
    if key not in d:
      d[key]=[]
    d[key].append(i)

for i in d.iterkeys():
  t=has_arithmetic(d[i],3)
  if t:
    if t != (1487, 4817, 8147):
      print repr(t).replace('(','').replace(', ','').replace(')','')
    
      
