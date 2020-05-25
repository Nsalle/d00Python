import string
import sys
import re

if len(sys.argv) != 3:
    print("ERROR")
    quit()

try:
    nb = int(sys.argv[2])
except ValueError:
    print("ERROR")
    quit()

stri = str(sys.argv[1])
for c in string.punctuation:
    stri = stri.replace(c, '')
splitlist = stri.split(' ')
i = 0
while i < len(splitlist):
    if len(splitlist[i]) <= nb:
        splitlist.remove(splitlist[i])
        i -= 1
    i += 1

if len(splitlist) == 0:
    print("ERROR")
    quit()
print(splitlist)
