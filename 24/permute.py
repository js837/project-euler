import math

cur=(0,1,2,3,4,5,6,7,8,9)

def tupToPerm(tup):
  available=[0,1,2,3,4,5,6,7,8,9]
  perm=[]
  for i in tup:
    perm.append(available[i])
    available.pop(i)
  return tuple(perm)

i=0

for i1 in xrange(0,10):
  for i2 in xrange(0,9):
    for i3 in xrange(0,8):
      for i4 in xrange(0,7):
        for i5 in xrange(0,6):
          for i6 in xrange(0,5):
            for i7 in xrange(0,4):
              for i8 in xrange(0,3):
                for i9 in xrange(0,2):
                  for i10 in xrange(0,1):
                    i=i+1
                    if i==1000000:
                      print tupToPerm((i1,i2,i3,i4,i5,i6,i7,i8,i9,i10))
                      break
                    
    
