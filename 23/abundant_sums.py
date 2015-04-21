import sys
sys.path.append('C:\Users\Jake\Dropbox\Project Euler\libs')
import jake_lib as lib

def isAbundant(n):
  if sum(lib.get_factors(n))>2*n:
    return True
  else:
    return False
  
ab_list=[]
ab_set=set()
for i in xrange(1,28124):
  if isAbundant(i):
    ab_list.append(i)
    ab_set.add(i)

ab_list.sort(reverse=True)

sumi=0

for i in xrange(28123,1,-1):
  for j in ab_list:
    if i-j in ab_set:
      #print i
      pass
      sumi=sumi+i
      break
    
print 28123*(28124)//2 - sumi
