from HexConvert import encode, decode

# encode()
print(encode('T'))
# 54

# Sentence Usage - You may change however You want.
text = "To Every You I've Loved Before"
lst = list(text)
result = '' # You can add 0x in here so the result will start in 0x...
for i in lst:
	result = result + encode(i)
print(result)
# 546F20457665727920596F752049277665204C6F766564204265666F7265
# If the character is not part of ASCII printable characters (extended not included) it returns 00

### ### ### ###

# decode()
decode('54')
# T

# Sentence Usage - You may change however You want.
import textwrap
text = '546F20457665727920596F752049277665204C6F766564204265666F7265'
lst = textwrap.wrap(text, width=2) # If the Hex starts with 0x... You can offset by chnaging text to text[2:]
result = ''
for i in lst:
	result = result + decode(i)
print(result)
# To Every You I've Loved Before
# If the character is not part of ASCII printable characters (extended not included) it returns ' '
