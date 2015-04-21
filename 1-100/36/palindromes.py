sumi=0

for i in xrange(1,1000000):
  bin_i=bin(i)[2:]
  dec_i=str(i)

  if bin_i[::-1]==bin_i and dec_i[::-1]==dec_i:
    sumi+=1
print sumi
