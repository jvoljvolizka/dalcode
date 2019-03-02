#!/bin/python
import binascii
import sys


filename = sys.argv[1]

outname = sys.argv[2]
with open(filename, "r") as f:
    ins = f.read()
ins = ins[:-1]
dallist = []
littledick = "dalyarak"
bigsick = "DALYARAK"
tmplist = []
newlist = []

hexdata = ""

for i in range(0,len(ins) - 1, 8):
    dallist.append(ins[i:i+8])

for binstr in dallist:
    #print(binstr)
    for char in range(len(binstr)):
        tmplist = list(binstr)
        if binstr[char] == littledick[char]:
            tmplist[char] = "0"
        else:
            tmplist[char] = "1"
        binstr = ''.join(tmplist)
    newlist.append(binstr)

for i in newlist:
    a = hex(int(i,2))[2:]
    a = a.zfill(2)
    hexdata = hexdata + a

out = open(outname, "wb")
out.write(binascii.unhexlify(hexdata))
