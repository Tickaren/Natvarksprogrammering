import sqlite3

conn = sqlite3.connect('mytest.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS persons")
c.execute("DROP TABLE IF EXISTS scores")

c.execute('''CREATE TABLE persons
            (id INTEGER PRIMARY KEY AUTOINCREMENT, name1 text, name2 text)''')
c.execute('''CREATE TABLE scores
            (upgnr INTEGER, score INTEGER, id INTEGER)''')
with open('score2.txt') as f:
    for line in f:
        a = line.split()

        c.execute('SELECT * FROM persons WHERE name1 = ? AND name2 = ?',(str(a[2]), str(a[3]) ))
        data = c.fetchall()

        if len(data) == 0:
            c.execute("INSERT INTO persons (name1, name2) VALUES (?, ?)", (str(a[2]), str(a[3])))

        c.execute('SELECT * FROM persons WHERE name1 = ? AND name2 = ?',(str(a[2]), str(a[3])))
        data = c.fetchone()
        c.execute("INSERT INTO scores (upgnr, score, id) VALUES (?, ?, ?)", (int(a[1]),int(a[4]), data[0] ))

conn.commit()

# S
c.execute('SELECT name1, name2, SUM(score) FROM persons JOIN scores ON persons.id = scores.id GROUP BY persons.id ORDER BY SUM(score) DESC LIMIT 10')
topscores = c.fetchall()
print("Top scores:")
for i in topscores:
    print(i[0], " ", i[1], " ", i[2])

# Skriva ut de svåraste uppgifterna:
c.execute('SELECT upgnr, SUM(score) FROM scores GROUP BY upgnr ORDER BY SUM(score) ASC LIMIT 10')
topupg = c.fetchall()
print()
print("Hardest upg:")
for i in topupg:
    print("Upg: ", i[0], " score: ", i[1])

conn.close()
