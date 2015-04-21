tot=0
for d8d9d10 in xrange(17,1000,17):
  t=d8d9d10
  d10=t % 10
  t=(t-d10)//10
  d9=t%10
  t=(t-d9)//10
  d8=t%10
  if len(set([d10,d9,d8]))==3:
    for d5d6d7 in xrange(14,1000,7):
      t=d5d6d7
      d7=t % 10
      t=(t-d7)//10
      d6=t%10
      t=(t-d6)//10
      d5=t%10
      if len(set([d10,d9,d8,d7,d6,d5]))==6:
        for d2d3d4 in xrange(12,1000,2):
          t=d2d3d4
          d4=t % 10
          t=(t-d4)//10
          d3=t%10
          t=(t-d3)//10
          d2=t%10
          s=set([d2,d3,d4,d5,d6,d7,d8,d9,d10])
          if len(s)==9:
            z=set([0,1,2,3,4,5,6,7,8,9])
            d1=z.difference(s).pop()
            #if d2==4 and d7==7:
            #  print d1,d2,d3,d4,d5,d6,d7,d8,d9,d10
            if (d3*100+d4*10+d5) % 3==0 and \
               (d4*100+d5*10+d6) % 5==0 and \
               (d6*100+d7*10+d8) % 11==0 and \
               (d7*100+d8*10+d9) % 13==0:
                 p = [str(q) for q in [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]]
                 tot+=int(''.join(p))


print tot



