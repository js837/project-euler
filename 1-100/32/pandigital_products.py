def is_pandigital(str_n):
  if not len(str_n)==9:
    return False
  for i in xrange(1,10):
    if str(i) not in str_n:
      return False
  return True

s=set()

#2 digit times 3 digit
for i in xrange(1,9876):
  for j in xrange(1,98):
    k=i*j
    if is_pandigital(str(i)+str(j)+str(k)):
      if k not in s:
        s.add(k)

print sum(s)
