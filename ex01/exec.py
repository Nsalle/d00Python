import sys

total = ""

for arg in sys.argv[1:]:
    arg = arg + ' '
    total += arg

total = total[:-1]
total = total.swapcase()
print(total[::-1])
