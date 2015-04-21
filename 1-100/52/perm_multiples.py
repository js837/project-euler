import jake_lib as lib

x=0
while True:
  x+=1
  
  s=lib.get_digits(x)
  s.sort()

  t=lib.get_digits(2*x)
  t.sort()

  if s!=t:
    continue
  
  u=lib.get_digits(3*x)
  u.sort()

  if t!=u:
    continue

  v=lib.get_digits(4*x)
  v.sort()

  if u!=v:
    continue

  w=lib.get_digits(5*x)
  w.sort()

  if v!=w:
    continue

  y=lib.get_digits(6*x)
  y.sort()
  
  if w==y:
    print x
    break




