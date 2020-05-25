import sys


def usage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 69 420")
    exit()


if len(sys.argv) != 3:
    print("InputError: Wrong number of arguments")
    usage()
try:
    try:
        nb1 = int(sys.argv[1])
        nb2 = int(sys.argv[2])
    except ValueError:
        nb1 = float(sys.argv[1])
        nb2 = float(sys.argv[2])
    print("Sum:\t\t", nb1 + nb2)
    print("Difference:\t", nb1 - nb2)
    print("Product:\t", nb1 * nb2)
    if nb2 != 0:
        print("Quotient:\t", nb1 / nb2)
    else:
        print("Quotient:\tERROR (div by zero)")
    if nb2 != 0:
        print("Remainder:\t", nb1 % nb2)
    else:
        print("Remainder:\tERROR (modulo by zero)")
except ValueError:
    print("ImputError: Only Numbers")
    usage()
