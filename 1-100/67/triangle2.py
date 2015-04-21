f=open('triangle2.txt','r')
triangle=[]
for line in f:
  triangle.append([int(x) for x in line.split()])
f.close()

height=len(triangle)

for i in xrange(height-2,-1,-1): #row
  #print triangle
  #print i,'i'
  for j in xrange(i+1):
    triangle[i][j]=triangle[i][j]+max(triangle[i+1][j],triangle[i+1][j+1])

print triangle[0][0]
    
