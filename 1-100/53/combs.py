def choose(n, k):
  if 0 <= k <= n:
    ntok = 1
    ktok = 1
    for t in xrange(1, min(k, n - k) + 1): #use symmetry of function
      ntok *= n
      ktok *= t
      n -= 1
    return ntok // ktok
  else:
    return 0

count=0
for n in xrange(1,101):
  for r in xrange(0,n+1):
    if choose(n,r)>1000000:
      count+=1

print count
