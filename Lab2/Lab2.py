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
    f.closed
# Sortering:
sortedscores = sorted(totalscores, key=totalscores.get, reverse=True)

highscore = sortedscores[0]
for i in sortedscores:
    if totalscores[i] == totalscores[highscore]:
        print(i, totalscores[i])
    else:
        break
