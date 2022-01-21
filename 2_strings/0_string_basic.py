# String (str) - A sequence of characters in "" or ''

# + string concatenation : combining two strings
print("Hello" + " World")

# * repeat strings
print("Hello" * 10)

# String indexing (position)
singer = "Justin Bieber"
#         0123456789012

print(singer[0])
print(singer[12])
# print(singer[15])  "index out of range"
print(singer[6])  # " "
print(singer[-1])

# len(str) - returns the length of a string
print(len(singer))
print(singer[len(singer) - 1])  # last character

# string slicing (substring)
# str[start:end]    start <=  < end
print(singer[0:5])

actor = "Ryan Reynolds"
#        0123456789012

print(actor[:4])  # Ryan
print(actor[5:])  # Reynolds
print(actor[:])  # copy the string
