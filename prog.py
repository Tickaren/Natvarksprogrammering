import random

def getLotto():
    return [random.randint(1, 35) for _ in range(7)]
def getLotto2():
    a = []
    for _ in range(7):
        a.append(random.randint(1, 35))
    return a
