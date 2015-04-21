sys.path.append('C:\Users\Jake\Dropbox\Project Euler\libs')
import number_words,sys


text=''
for i in xrange(1,1001):
  t=number_words.num_to_words(i)
  t=t.replace('-','')
  t=t.replace(',','')
  t=t.replace(' ','')
  text=text+t

print len(text)
  
