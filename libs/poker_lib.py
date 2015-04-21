def rankHand(strCards):
  cards =  strCards.strip().split(' ')
  tupleCards=[]

  if len(cards)!=5:
    print "Hand must consist of 5 cards"
    return

  aceFlag=False
  num_freqs={}
  suit_freqs={}
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
      aceFlag=True
    # Freq dicts 
    if int(num) in num_freqs:
      if num_freqs[int(num)]<4:
        num_freqs[int(num)]+=1
    else:
      num_freqs[int(num)]=1

    if suit in suit_freqs:
      if suit_freqs[suit]<5:
        suit_freqs[suit]+=1
    else:
      suit_freqs[suit]=1
    tupleCards.append((int(num),suit))
  #print freqs
  byNumGroup = sorted(tupleCards,key=lambda x:(num_freqs[x[0]],x[0]),reverse=True)
  bySuitGroup= sorted(tupleCards,key=lambda x:(suit_freqs[x[1]],x[0]),reverse=True)
  byNum      = sorted(tupleCards,key=lambda x:(x[0],x[1]),reverse=True)
  #print byNumGroup
  #print bySuitGroup
  #print byNum


  ###### TO DO ########
  # Add hand high card ranking - careful for hands which aren't full eg. pair
  flush=False
  flush_rank=0
  if len(suit_freqs)==1:
    flush=True
    flush_rank=byNum[0][0]*15**5+byNum[1][0]*15**4+byNum[2][0]*15**3+byNum[3][0]*15**2+byNum[4][0]*15**1
    
  straight_rank=0
  straight=True
  for i in xrange(1,len(byNum)):
    if not (byNum[i-1][0]==byNum[i][0]+1):
      straight=False
  if straight:
    straight_rank=byNum[0][0]
    
  if byNum[0][0]==14 and byNum[1][0]==5 and byNum[2][0]==4 and byNum[3][0]==3 and byNum[4][0]==2:
    straight=True
    straight_rank=byNum[1][0]


 ## Recognise hands
      
  if flush and straight:
    print "Straight Flush"
    hand_rank=100
    sub_rank=straight_rank

  elif 4 in num_freqs.values():
    print "4 of Kind"
    hand_rank=78
    sub_rank=byNumGroup[0][0]*15+byNumGroup[4][0]

  elif 3 in num_freqs.values() and 2 in num_freqs.values():
    print "Full House"
    hand_rank=59
    sub_rank=byNumGroup[0][0]*15+byNumGroup[0][4]

  elif flush:
    print "Flush"
    hand_rank=44
    sub_rank=flush_rank

  elif straight:
    print "Straight"
    hand_rank=34
    sub_rank=straight_rank

  elif 3 in num_freqs.values():
    print "3 of a kind"
    hand_rank=22
    sub_rank=byNumGroup[0][0]*15**3+byNumGroup[3][0]*15**2+byNumGroup[4][0]*15**1

  elif num_freqs.values().count(2)==2:
    print "two pair"
    hand_rank=17
    sub_rank=byNumGroup[0][0]*15**3+byNumGroup[2][0]*15**2+byNumGroup[4][0]*15**1

  elif 2 in num_freqs.values():
    print "Pair"
    hand_rank=5
    sub_rank=byNumGroup[0][0]*15**4+byNumGroup[2][0]*15**3+byNumGroup[3][0]*15**2+byNumGroup[4][0]*15**1

  else:
    print "High Card"
    hand_rank=1
    sub_rank=byNumGroup[0][0]*15**5+byNumGroup[1][0]*15**4+byNumGroup[2][0]*15**3+byNumGroup[3][0]*15**2+byNumGroup[4][0]*15**1
    
  return hand_rank,sub_rank


f=open('poker.txt','r')

for line in f:
  hand1=line[:14]
  hand2=line[14:]
  print hand1,hand2
