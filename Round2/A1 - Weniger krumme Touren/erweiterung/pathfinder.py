import threading
from point import P
from startpointcalculator import StrartPointsCalculator
import func 
from time import sleep

class PathFinder(threading.Thread):
    def __init__(self, filename, cb, counter, finished):
        threading.Thread.__init__(self)
        self.cb = cb
        self.counter = counter
        self.filename = filename
        self.finished = finished

    def run(self):
        print("starting pathfinding in 5s...")
        sleep(1)
        func.openWithSystemViewer("http://localhost:5000")
        sleep(4)
        print("start pathfinding")
        points = []

        with open(self.filename, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                xy = line.split(" ")
                points.append(
                    P(float(xy[0]), float(xy[1]))
                )
        
        for point in points:
            point.calcDistanceMap(points)

        func.initVisualizer(points)

        endLen = len(points)


        path = func.getStartPoints(points)

        for p in path:
            points.remove(p)
        
        func.step(path, points, endLen, self.cb, self.counter)
        self.finished()