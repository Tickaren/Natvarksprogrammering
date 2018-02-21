# def printTable(TRange : int):
#     for x in range(1, TRange):
#         print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
# printTable(11)
# print("A={} och B={}".format(1,2))
#

# Reading and Writing files
with open('test.txt') as f:
    for line in f:
        print(line, end='')
f.closed
