from sys import argv
from pancake import P
from collections import deque
from time import time


def main():
    def round_down(n):
        return int(n) + 1 if n - int(n) > 0 else int(n)

    num = []
    n = int(argv[1])

    numbers = list(range(1, n+1))
    splitPoint = round_down(len(numbers)/2)
    numbersA = numbers[:splitPoint]
    numbersB = numbers[splitPoint:]

    start = True
    while len(numbersA)+len(numbersB) != 0:
        if start:
            num.append(numbersA.pop(0))
            start = False
        else:
            num.append(numbersB.pop(0))
            start = True
    del start, numbers, n
    num.reverse()

    initStack = P(num)

    #Optimierung aus "theoretische Analyse - Teilaufgabe B > Muster 2 – Nahezu identische Lösungswege"
    if not ((len(num) % 2 ) == 0):
        pass
        #initStack.flip(0)


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
