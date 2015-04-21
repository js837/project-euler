import math

def score(word):
  return sum(ord(letter)-64 for letter in word)

f=open('words.txt','r')
words=f.read().split(',')
f.close()

t=0
for word in words:
  S=score(word.strip('"'))
  n=(-1+math.sqrt(1+8*S))/2
  if abs(math.floor(n)-n)<0.00001:
    t=t+1

print t
    
