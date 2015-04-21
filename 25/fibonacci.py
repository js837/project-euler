# Import Lib
import sys
sys.path.append('C:\Users\Jake\Dropbox\Project Euler\libs')
import jake_lib as lib

i=1
j=1
count=2
while lib.num_digits(j)<1000:
  i,j = j,i+j
  count=count+1

print count




