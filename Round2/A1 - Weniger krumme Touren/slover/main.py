import argparse
from time import time
from point import P
import func

def main(filename, depth):
    points = []

    with open(filename, "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            xy = line.split(" ")
            points.append(
                P(float(xy[0]), float(xy[1]))
            )
    
    for point in points:
        point.calcDistanceMap(points)

    endLen = len(points)
    
    path = func.getStartPoints(points)

    for p in path:
        points.remove(p)
    
    return func.step(path, points, endLen, depth)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='file as relative path')
    parser.add_argument('-d', '--depth', help='search depth - defaul=2', default=2)
    args = parser.parse_args()
    starttime = time()
    code = main(args.file, int(args.depth))
    print("\n time: "+str((time()-starttime))+" s")
    if(code == 0):
        exit(0)
    else:
        exit(-1)
