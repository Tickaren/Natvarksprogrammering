#Läsning av fil och lägga in i dict:
totalscores = {}
with open('score2.txt') as f:
    for line in f:
        a = line.split()
        name = a[2] +" "+ a[3]
        if name not in totalscores:
            totalscores[name] = int(a[4])
        else:
            totalscores[name] = totalscores[name] + int(a[4])
# Sortering:
sortedscores = sorted(totalscores, key=totalscores.get, reverse=True)

numb = 0
for i in sortedscores:
    print(i, totalscores[i])
    numb = numb +1
    if numb > 5: break
#Stänger filen
f.closed
