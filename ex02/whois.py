import sys

if len(sys.argv) != 2:
    print("ERROR")
    print("Too many args")
    exit()

if not sys.argv[1].isnumeric():
    print("ERROR")
    print("Arg is not an integer")
    exit()

sys.argv[1] = int(sys.argv[1])

if (sys.argv[1] == 0):
    print("I'm Zero.")
    exit()

if (sys.argv[1] % 2):
    print("I'm odd.")
else:
    print("I'm even.")
