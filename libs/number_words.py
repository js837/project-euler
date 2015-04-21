import math

hundred_list={
1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen',
20:'twenty',
30:'thirty',
40:'forty',
50:'fifty',
60:'sixty',
70:'seventy',
80:'eighty',
90:'ninety'}

multipliers={
2:'hundred',
3:'thousand',
6:'million',
9:'billion',
12:'trillion',
15:'quadrillion',
18:'quintillion',
21:'sextillion',
24:'septillion',
27:'octillion',
30:'nonillion',
33:'decillion',
36:'undecillion',
39:'duodecillion',
42:'tredecillion',
45:'quattuordecillion',
48:'quindecillion',
51:'sexdecillion',
54:'septendecillion',
57:'octodecillion',
60:'novemdecillion',
63:'vigintillion'
}

def hundred_to_words(n): #numbers less than 100 into words
  if n>=100: ##error check
    raise Exception
  if n in hundred_list:
    return hundred_list[n]
  else:
    return hundred_list[n-(n%10)]+'-'+hundred_list[n%10]
    
def thousand_to_words(n): # turns numbers less than 1000 into words
  if n>=1000: ##error check
    raise Exception
  if n==0:
    return hundred_to_words(0)
  hundreds=n/100
  tens=n%100
  string1=''
  string2=''
  string3=''    
  if hundreds!=0:
    string1=hundred_list[hundreds]+' '+multipliers[2]
  if tens!=0:
    string3=hundred_to_words(tens)
  if hundreds!=0 and tens!=0:
    string2=' and '
  return string1 + string2 + string3

def num_to_words(n):
  if n==0:
    return 'zero'
  else:
    num_digits=int(math.log10(n))+1
  thousand_groups=int(math.ceil(num_digits/3.0))
  words=[]
  thousands=0
  for i in xrange(0,thousand_groups):
    group=n%1000
    n=(n-group)/1000
    if group!=0:
      if i==0:
        thousands=group
        words.insert(0,thousand_to_words(group))
      else:
        words.insert(0,thousand_to_words(group)+' '+multipliers[3*i])

  len_words=len(words)
  string = words[0]
  for i in xrange(1,len_words):
    if thousand_groups>1 and thousands<100 and thousands>0 and i==len_words-1:
      string=string+' and '
    else:
      string=string+', '
    string=string+words[i]
  return string

if __name__=='__main__':
  print '------------ Test ------------'
  print num_to_words(1203902193021)
  print num_to_words(2500)
  print num_to_words(2040)
