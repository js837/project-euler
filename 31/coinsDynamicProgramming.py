coinlist = [200,100,50,20,10,5,2,1]

# Let array[i,j]=number of ways of making sum i using j largest coin as last coin in sequence.

def count(i,j,array={}):
  if (i,j) in array:
    return array[i,j]
  if i==0:
    return 1
  if i<0:
    return 0
  if j<0:
    return 0
  array[i,j]=count(i-coinlist[j],j,array)+count(i,j-1,array)
  return array[i,j]

print count(200,7)