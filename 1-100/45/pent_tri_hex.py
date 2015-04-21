import math

def triangle(n):
  return n*(n+1)//2

def is_pentagonal(n):
  t=(1+math.sqrt(1+24*n))/6.0
  if abs(math.floor(t)-t)<0.0000001:
    return int(t)
  else:
    return False

def is_hexagonal(n):
  t=(1+math.sqrt(1+8*n))/4.0
  if abs(math.floor(t)-t)<0.0000001:
    return int(t)
  else:
    return False

def is_triangle(n):
  t=(-1+math.sqrt(1+8*n))/2.0
  if abs(math.floor(t)-t)<0.0000001:
    return int(t)
  else:
    return False

n=286
while not (is_pentagonal(triangle(n)) and is_hexagonal(triangle(n))):
  n+=1
print n*(n+1)//2
  
