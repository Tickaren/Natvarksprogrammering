# 9.1:
# Uppgift 1:
txt = "ABC abc"
b = bytearray(txt, "ASCII")
print(len(txt))
print(len(b))
for i in b:
    print(i)
""" Print:
7
7
65
66
67
32
97
98
99
"""

# UPPGIFT 2:
a = bytearray("ÅÄÖ", "ASCII") # ÅÄÖ ingår inte i unicode!
print(a)
#UnicodeEncodeError

# UPPGIFT 3:
a = bytearray("ÅÄÖ", "LATIN-1")
print(a)
# Print: bytearray(b'\xc5\xc4\xd6')

a = bytearray("ÅÄÖ", "UTF-8")
print(a)
# Print: bytearray(b'\xc3\x85\xc3\x84\xc3\x96')
