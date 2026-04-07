# creating a secret code language
# encoding:
import random
import string
document=input("Enter the Word to Encode: ")
lst=document.split(" ")
encodingLst=[]
for word in lst:
    if (len(word)<3):
        encode=word[::-1]
    else:
        encodeWord=word[1:]+word[0]
        # print(encodeWord)
        encode="".join(random.choices((string.ascii_letters+string.digits+string.punctuation), k=3))+encodeWord+"".join(random.choices((string.ascii_letters+string.digits+string.punctuation), k=3))
    encodingLst.append(encode)
    # print(encode, end=" ")
print("Encoding:", " ".join(encodingLst))

# decoding
decodingLst=[]
for encode in encodingLst:
    
    if (len(encode)<3):
        decode=encode[::-1]
    else:
        decodeRandom=encode[3:-3]
        decode=decodeRandom[-1]+decodeRandom[:-1]
    # print(decode, end=" ")
    decodingLst.append(decode)
print("Decoding:", " ".join(decodingLst))
print("Hope you enjoyed this encoding and decoding game!!")
feedback=input("Enter you feedback: ")
print("Thanks for your precious feeddback")
'''
NOTE: 
1. string.ascii_letters: 'abc...xyzABC...XYZ'
2. string.digits:'0123456789'
3. string.punctuation:'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
'''

# join function is used to join an element of list or any iterable to single string: syntax:
# separator.join(iterable)

