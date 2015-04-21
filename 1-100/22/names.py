f=open('names.txt','r')

names=f.readlines()[0]

names=names.replace('"',"")
names=names.split(',')

names.sort()


scores=[0]*len(names)
for i,name in enumerate(names):
  scores[i]=sum([(ord(j)-64) for j in name])*(i+1)
f.close() 
print sum(scores)

