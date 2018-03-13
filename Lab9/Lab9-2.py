from math import log2
txt = ""
with open('exempeltext.txt') as f:
    txt = f.read()
    f.close()
byteArr = bytearray(txt, "utf-8")
print(len(txt))
print(len(byteArr))
"""
Print:
29090
30490
Förklaring:
utf-8 kan lagra tecken i 1,2 eller 3 bytes vilket betyder att Å, Ä, Ö lagras
som 2 eller 3 bytes i en byteArray.
"""

def makeHisto(byteArr):
    arr=[0]*256
    for i in range(256):
        arr[i] = 0
    for i in byteArr:
            arr[i] += 1
    return arr

def makeProb( histo ):
    totalcount = 0
    for i in histo:
        totalcount += i

    arr=[0]*256
    for i in range(256):
        arr[i] = histo[i]/ totalcount
    return arr

def entrpi(prob):
    H = 0
    for i in prob:
        if(i != 0):
            H += i*log2(1/i)
    return H
txt = ""
with open('exempeltext.txt') as f:
    txt = f.read()
    f.close()
byteArr = bytearray(txt, "utf-8")
histo = makeHisto(byteArr)
prob = makeProb(histo)
ent = entrpi(prob)
print(ent)
# Svar d): ca 4,6 bit!
