import argparse
from time import time
from pancake import P
from func import rateStack
from func import first

def main(filename, n, m):
    with open(filename, "r") as file:
        num=[]
        for line in file.read().splitlines()[1:]:
            num.append(int(line))

    initStack = P(num, [])
    del num

    pkListA = [initStack.copy()]
    pkListB:list = []
    while pkListA:
        for pancake in pkListA:
            flipPoints = pancake.getFlipIndexPoints()
            mutationPancakes = []
            for i in flipPoints:
                newPancake = pancake.copy()
                newPancake.flip(i)
                if newPancake.isValid():
                    newPancake.printHistory()
                    return 0
                mutationPancakes.append((newPancake, rateStack(newPancake)))
                del newPancake
            mutationPancakes.sort(key = lambda x: x[1], reverse=True)
            pkListB += (first(n, mutationPancakes))
        pkListB.sort(key=lambda x: x[1], reverse=True)
        pkListB = list(map(lambda x: x[0], pkListB))
        pkListA = first(m, pkListB)
        pkListB = []


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='pancake File as relative Path')
    parser.add_argument('-p', '--preset', help='normal - fast - accurate', default="normal")
    args = parser.parse_args()
    starttime = time()
    print("USING SCAN PRESET: "+str(args.preset))
    if (args.preset == "normal"):
        main(args.filename, 3, 800)
    elif (args.preset == "fast"):
        main(args.filename, 2, 100)
    elif (args.preset == "accurate"):
        main(args.filename, 6, 1000)
    print("\n time: "+str(round(time()-starttime, 3))+"s")
    exit(0)