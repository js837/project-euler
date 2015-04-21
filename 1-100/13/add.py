f=open('numbers.txt')
total=0
for line in f:
  total=(total+int(line))
f.close()
print str(total)[:10]
