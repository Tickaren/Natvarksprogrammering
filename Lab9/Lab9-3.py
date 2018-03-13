import random
import zlib
txt = ""
with open('exempeltext.txt') as f:
    txt = f.read()
    f.close()
byteArr = bytearray(txt, "utf-8")
theCopy = bytearray(byteArr)
random.shuffle(theCopy)

kod = zlib.compress(theCopy)
print("Blandad array:")
print("Komprimerad bit : ", len(kod)*8, " byte: ", len(kod))
print("Okomprimerad bit : ", len(theCopy)*8, " byte: ", len(theCopy))

kod = zlib.compress(byteArr)
print("Orginal array:")
print("Komprimerad bit : ", len(kod)*8, " byte: ", len(kod))
print("Okomprimerad bit : ", len(byteArr)*8, " byte: ", len(byteArr))

print("Entropyn: ", 30490/4.6)
"""
i. lägst antal bit/källsymbol:
Entropyn
ii. och i vilket fall  ck vi högst antal bit/källsymbol
zlib-kodning av randomiserad källa.
iii. förklara detta!
Entropyn är om man skulle skriva komprimering för endast det dokumentet.
Z-lib funktionen är standardiserad för att kunna fungera i många olika fall.

Den shufflade arrayen blev störst då alla tal hamnade på slumpmässiga platser.
Då blir det svårare att komprimera och förutse plattserna i arrayen.
"""
# 9-4
t1   = """Hoppas att denna laboration aldrig tar slut för nu börjar ett mycket intressant experiment! """
t10 = 10*t1

kod1 = zlib.compress(bytearray(t1, "utf-8"))
kod10 = zlib.compress(bytearray(t10, "utf-8"))

print ("T1: ", len(kod1))
print ("T10: ", len(kod10))
"""
För den repeteras bara 10 gånger och det känner komprimeringen av!
"""
