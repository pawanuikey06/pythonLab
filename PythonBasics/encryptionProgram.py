import random
import string

chars ="  "+string.punctuation +string.digits +string.ascii_letters


chars1 =list(chars)
key =chars1.copy()
random.shuffle(key)
print(f"chars : {chars1}")
print(f"keys: {key}")

# print(key is chars1)

#ENCRYPT

plain_text =input("Enter a message to encrypt:")
cipher_text=""

for letter in plain_text:
    index =chars1.index(letter)
    cipher_text+=key[index]


print(f"Origional Message is : {plain_text}")
print(f"Encrypted Message is:  {cipher_text}")
decr=""
for letter in cipher_text:
    index =key.index(letter)
    decr+=chars1[index]

print(f"Message After Decryption : {decr}")

