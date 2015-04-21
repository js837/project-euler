i=1
j=2

sum=2

while i+j<=4000000:
  if (i+j)%2==0:
    sum=sum+i+j
  i,j=j,i+j

print sum
    
  
