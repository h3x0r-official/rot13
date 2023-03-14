import sys # to get input form terminal
import codecs # to encode and decode rot13

file = sys.argv[1] # taking 1st passed argument e.g. data.txt
with open(file) as text: #opening file data.txt
  fetched_txt = text.read() # reading lines of the file 
s = (len(fetched_txt)) # getting length of characters
leng = (s-1) 

phrase = fetched_txt # assigning fetched_text data to new phrase variable
enc = "rot_13" # encryption method

print("\n***************")
print("Length: ", leng)
print("Encrption method: rot13")
print("***************\n")


print("Decoded text: ", fetched_txt)
print("Encoded text: ", codecs.encode(phrase, enc), "\n") # encoding