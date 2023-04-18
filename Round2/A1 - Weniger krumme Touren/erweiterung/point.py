from math import sqrt

class P: #point
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distancemap = {}
    
    def calcDistanceMap(self, points):
        for point in points:
            self.distancemap[point] = self._lenghtTo(point)
    
    def _lenghtTo(self, point2):
        x1 = self.x
        x2 = point2.x
        y1 = self.y
        y2 = point2.y
        return sqrt(((x1-x2)**2) + ((y1-y2)**2))

    def lenghtTo(self, point2):
        return self.distancemap[point2]