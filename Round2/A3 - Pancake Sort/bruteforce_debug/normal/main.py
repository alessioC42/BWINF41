from sys import argv
import json
from pancake import P
from collections import deque
from time import time


def main():
    num = list(json.loads(argv[1]))
    initStack = P(num)
    print("-- " + str(num)+ " --")
    if (initStack.isValid()):
        initStack.printHistory()
        return 0

    pancakes = deque([initStack])

    while pancakes:
        pancake = pancakes.popleft()
        flipoints = pancake.getFlipIndexPoints()
        for i in flipoints:
            newPancake = pancake.copy()
            newPancake.flip(i)
            if (newPancake.isValid()):
                newPancake.printHistory()
                return 0
            else:
                pancakes.append(newPancake)
    return -1

if __name__ == "__main__":
    starttime = time()
    main()
    print("\nFinished in "+str(round(time()-starttime, 3))+"s")
