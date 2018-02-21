# Uppgift 4.4 på python.org
# for n in range(2,10):
#     for x in range(2,n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else: # Körs om inte break har körts
#         print(n, 'is a prime number')

# Uppgift 4.4 på python.org
# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue # Fortsätter på nästa loop
#     print("Found a number", num)

# Uppgift 4.5 på python.org
# while True:
    # pass # Gör ingenting. Tryck ctrl + c. Pass används istället för {}

# Uppgift 4.6 på python.org
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ') # end=' ' gör att det inte blir en ny rad utan istället ett mellanslag efter det att den har skrivit ut variabeln
#         a, b = b, a+b
#     print()
#
# fib(2000) # Funktionsanrop

# Uppgift 1.4.6 I NetProgLab01
# 1:
# def hello(n: int):
#     for i in range(n):
#         print("Pappegoja", end=' ')
#     print()
# # hello(10)
# # 2:
# f = hello
# f(3)

# Uppgift 4.6 på python.org
# Returnerande Funktion
# def fib2(n: int):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result
#
# f100 = fib2(100)
# print(f100)

# Uppgift 4.7 på python.org
# def ask_ok(prompt, retries=4, reminder='Please try again'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
# ask_ok("Do you realy want to quit?!")

# Uppgift 1.4.6 I NetProgLab01
# 5:
# djur = ["Hund", "Katt", "Elefant"]
# def f(arg, ap):
#     arg.append(ap)
#     return arg
#
# djur = f(djur, "Loppa")
# print (djur)

# Uppgift 1.4.7 I NetProgLab01
# Keyword arguments
# def print_all(*arg, **keyword):
#     for kw in keyword:
#         print(kw, ":", keyword[kw])
#
# print_all(uh = "ababa", eh = "gross", yh = "hft", haha = "asdasd")

# def print_all2(*arg):
#     for kw in arg:
#         print(kw)
#
# print_all2("ababa", "gross", "hft")

# Uppgift 4.7.5 på python.org
# def make_incrementor(n):
#     return lambda x: x + n
# f = make_incrementor(42)
# print(f(0))
# print(f(1))
#
# g = lambda a,b: a+b
#
# print(g(3,2))
