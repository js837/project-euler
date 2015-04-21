coinlist = [200,100,50,20,10,5,2,1]

perms=[]

def num_ways(amount, coins, combs=[]):
  #print coins
  if amount == 0:
    combs.append(coins)
    coins=tuple()
    return
  else:
    for coin in coinlist:
      if coin<=amount and (len(coins)==0 or coin <= coins[-1]):
        num_ways(amount-coin,coins+(coin,),combs)
  return combs


t=num_ways(200,tuple())
print len(t)
