# def myrange():
#     i = 0
#     while i<10:
#         i+=1
#         yield(i)
#
# for i in myrange():
#     print(i)
#
# print("hello \n world")
# print(r"hello \n world")
import re
str = "1222222223 456 789 123"

print(re.findall(r"\w+", str))
print(re.findall(r"\w.*3", str))
print(re.findall(r"\w.*?3", str))
