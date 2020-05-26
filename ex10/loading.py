from time import sleep
from time import time
import subprocess

listy = range(1000)
ret = 0


def ft_progress(lst):
    startime = time()
    percent = 0
    turn = 0
    maxr = len(lst)
    while percent < len(lst):
        percent = turn / maxr * 100
        subprocess.call("clear")
        curtime = time() - startime
        print("ETA: {:.2f}s\t".format(curtime), end='')
        print("[{:3.0f}%] ".format(percent), end='')
        print("{}/{}".format(turn, maxr))
        yield turn
        turn += 1


for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
