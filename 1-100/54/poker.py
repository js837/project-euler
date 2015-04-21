def rankHand(strCards):
  cards =  strCards.strip().split(' ')
  tupleCards=[]

  if len(cards)!=5:
    print "Hand must consist of 5 cards"
    return

  num_freqs={}
  
  for card in cards:
    num= card[0]
    suit=card[1]
    if num.upper() == 'T':
      num=10
    elif num.upper() == 'J':
      num=11
    elif num.upper() == 'Q':
      num=12
    elif num.upper() == 'K':
      num=13
    elif num.upper() == 'A': #Note for straights Ace is high or low
      num=14
    tupleCards.append((int(num),suit))
    
    # Freq Distribution
    if int(num) in num_freqs:
      if num_freqs[int(num)]<4:
        num_freqs[int(num)]+=1
    else:
      num_freqs[int(num)]=1

  # Sort the cards
  byNumGroup = sorted(tupleCards,key=lambda x:(num_freqs[x[0]],x[0]),reverse=True)
  byNum      = sorted(tupleCards,key=lambda x:(x[0],x[1]),reverse=True)

  #Check for Straight or Flush
  straight_rank=0
  straight=True
  flush=True
  for i in xrange(1,len(byNum)):
    if not (byNum[i-1][0]==byNum[i][0]+1):
      straight=False
      #break
    if not (byNum[i-1][1]==byNum[i][1]):
      flush=False
    if not (straight or flush):
      break
  # Rank Straight     
  if straight:
    straight_rank=byNum[0][0]   
  # Special case of Ace High Straight    
  if byNum[0][0]==14 and byNum[1][0]==5 and byNum[2][0]==4 and byNum[3][0]==3 and byNum[4][0]==2:
    straight=True
    straight_rank=byNum[1][0]

  # Rank Hands    
  if flush and straight:
    hand_rank=9
    sub_rank=straight_rank
    desc= "Straight Flush"
    # Special Case of Royal Flush
    if sub_rank==14:
      desc= "Royal Flush"  
  elif 4 in num_freqs.values():
    desc= "4 Of A Kind"
    hand_rank=8
    sub_rank=byNumGroup[0][0]*15+byNumGroup[4][0]
  elif 3 in num_freqs.values() and 2 in num_freqs.values():
    desc= "Full House"
    hand_rank=7
    sub_rank=byNumGroup[0][0]*15+byNumGroup[4][0]
  elif flush:
    desc= "Flush"
    hand_rank=6
    sub_rank=byNum[0][0]*15**5+byNum[1][0]*15**4+byNum[2][0]*15**3+byNum[3][0]*15**2+byNum[4][0]*15**1
  elif straight:
    desc= "Straight"
    hand_rank=5
    sub_rank=straight_rank
  elif 3 in num_freqs.values():
    desc= "3 Of A Kind"
    hand_rank=4
    sub_rank=byNumGroup[0][0]*15**3+byNumGroup[3][0]*15**2+byNumGroup[4][0]*15**1
  elif num_freqs.values().count(2)==2:
    desc= "Two pairs"
    hand_rank=3
    sub_rank=byNumGroup[0][0]*15**3+byNumGroup[2][0]*15**2+byNumGroup[4][0]*15**1
  elif 2 in num_freqs.values():
    desc= "One Pair"
    hand_rank=2
    sub_rank=byNumGroup[0][0]*15**4+byNumGroup[2][0]*15**3+byNumGroup[3][0]*15**2+byNumGroup[4][0]*15**1
  else:
    desc= "High Card"
    hand_rank=1
    sub_rank=byNumGroup[0][0]*15**5+byNumGroup[1][0]*15**4+byNumGroup[2][0]*15**3+byNumGroup[3][0]*15**2+byNumGroup[4][0]*15**1
    
  return (hand_rank,sub_rank,desc)


f=open('poker.txt','r')
count=0
for i,line in enumerate(f):
  hand1=line[:14]
  hand2=line[14:]
  if rankHand(hand1)>rankHand(hand2):
    count+=1

print count
