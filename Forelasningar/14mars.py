# Regular expressions:
import re
print(re.search("ab|bb", "aaa"))
print(re.search("ab|bb", "aaba"))
r = re.search("ab|bb", "aaba")
print(r.group())
