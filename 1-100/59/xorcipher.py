with open('cipher1.txt') as f:
  letters=f.read().strip().split(',')

def decrypt():
  for k1 in xrange(97,123):
    for k2 in xrange(97,123):
      for k3 in xrange(97,123):
        key=(k1,k2,k3)
        decrypted_letters=[]
        for i,letter in enumerate(letters):
          decrypted=key[i%3]^int(letter)
          decrypted_letters.append(chr(decrypted))
        decrypted_string = ''.join(decrypted_letters)
        if 'faithfulness' in decrypted_string:
          print decrypted_string
          print key
          return (decrypted_letters,key)

(decrypted_letters,key)=decrypt()

sum_ascii=0
for letter in decrypted_letters:
  sum_ascii+=ord(letter)

print sum_ascii
