# Uppgift 4.1
def myTest():
    yield 1
    yield 5
    yield 6
    yield 99

a = myTest()
b = myTest()

print (a.__next__())
print (a.__next__())


print (b.__next__())
print (b.__next__())

print (a.__next__())
print (a.__next__())

# Uppgift 4.2
def fib(n):
    a,b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

for a in fib(1000000):
    print (a)
