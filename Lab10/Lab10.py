# Uppgift 1
import queue

def printAndPop(pq):
    while pq.qsize()>0:
        print( pq.get() )

def test1():
    print("Running test 1")
    pq = queue.PriorityQueue()
    pq.put( (4.0, 10) )
    pq.put( (2.0, 8) )
    pq.put( (5.0, 2)  )
    pq.put( (1.5, 8) )
    pq.put( (4.0, 8) )
    pq.put( (1.0, 8) )
    pq.put( (3.0, (1,2)) )
    # pq.put( (2.0, (1,2)) )
    """
Krashar för att den försöker jämföra (1,2) med 8 vilket inte fungerar.
Förra uppgiften fungerade för att tuplens första element var unikt.
    """
    printAndPop( pq)
test1()

# Uppgift 2
class Node:
    def __init__(self, prio, data):
        self.prio = prio
        self.data = data
    def __lt__(self, other):
        return self.prio<other.prio
    def __str__(self):
        return "({} {})".format(self.prio, self.data)

def printAndPop2(pq):
    while pq.qsize()>0:
        print( pq.get() )

def test2():
    print("Running test 2")
    pq = queue.PriorityQueue()
    pq.put( Node(4.0, 10) )
    pq.put( Node(2.0, 8) )
    pq.put( Node(5.0, 2)  )
    pq.put( Node(1.5, 8) )
    pq.put( Node(4.0, 8) )
    pq.put( Node(1.0, 8) )
    pq.put( Node(3.0, (1,2)) )
    pq.put( Node(2.0, (1,2)) )
    printAndPop2( pq)
test2()
