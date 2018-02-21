# Uppgift 1.5.1 I NetProgLab01
# a = [1,2,3,1,1,1,5,7,2]
# print(a.count(1)) #Skriver ut hur många 1or som finns i listan
#
# a.sort
# print(a)

# stack = [1, 2, 3, 4]
# stack.append(8)
# stack.pop()
# stack.pop()
# print(stack)

# que = [1,2,3,4]
# que.append(8)
# que.append(9)
# que.pop(0)
# que.pop(0)
# print(que)

# Två olika funktioner som skriver ut samma sak:
# a = []
# for x in range(10):
#     a.append(x*2)
# print(a)
#
# b = [x*2 for x in range(10)]
# print(b)

# ----------------------------------------------------
# 1.5.2 TUPLES och SEQUENCES
# t = 1111, 2222, 3333
# print(t.count(1111))
# t.append(4444) # INTE OK OM DET ÄR EN TUPPLE
# print(t)
# t.pop() # INTE OK OM DET ÄR EN TUPPLE
# print(t)

# answ = ["yes", "ja", "japp", "ok"]
# a = input().lower()
# if (a in answ):
#     print("Jahop...")
# else:
#     print("Nehep")

# a = set('Hej jag heter Oscar!')
# print (a)


# 1.5.4 Looping Techniques

# def f(a):
#     for i in a:
#         print(i, a[i], end=' : ')
#     print()
#
# def func2(it):
#     for i, s in it.items():
#         print(i,s, end=' : ')
#     print()
#
# lista = {"uh": 2323, "ah": 2424, "Oscar": 2525, "Japp":8989, "Nätverk" : 6767}
# f(lista)
# func2(lista)

# 1.5.5 Kontrollfrågor på More on Conditions
def fname(age):
    if 20 <= age and age <= 65:
        print("Vad jobbar du med?")
    else:
        print("Gå och lägg dig!")

fname(32)
fname(10)
