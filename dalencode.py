#!/bin/python
import binascii
import sys
file = sys.argv[1]
with open(file,"rb") as f:
    ins = f.read()

hexlist = []
hexstr = str(binascii.hexlify(ins))[2:-1]
littledick = "dalyarak"
bigdick = "DALYARAK"
tmplist = []
newlist = []
for i in range(0,len(hexstr) - 1, 2):
    hexlist.append(bin(int(hexstr[i:i+2], 16))[2:].zfill(8))

for binstr in hexlist:
    #print(binstr)
    for char in range(len(binstr)):
        tmplist = list(binstr)
        if binstr[char] == "0":
            tmplist[char] = littledick[char]
        else:
            tmplist[char] = bigdick[char]
        binstr = ''.join(tmplist)
    newlist.append(binstr)
print(''.join(newlist))
