from point import P


class StrartPointsCalculator:
    def __init__(self, points:list[P]) -> None:
        self.points = points.copy()

    def getConvexOutlinePoints(self, points: list[P]) -> list[P]:
        """
        Calculating the Convex shape of the points and returns it.
        """

        points.sort(key=lambda p: p.x)
        upper_hull = []
        lower_hull = []
        for p in points:
            while len(upper_hull) >= 2 and self.crossProduct(upper_hull[-2], upper_hull[-1], p) <= 0:
                upper_hull.pop()
            upper_hull.append(p)
            while len(lower_hull) >= 2 and self.crossProduct(lower_hull[-2], lower_hull[-1], p) >= 0:
                lower_hull.pop()
            lower_hull.append(p)
        upper_hull.pop()
        lower_hull.reverse()
        return lower_hull + upper_hull

    def crossProduct(self, p1, p2, p3) -> float:
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

    def avg(self, list):
        return sum(list)/len(list)

    def getFullOutlinePoints(self) -> list[P]:
        points = self.points
        convexOutline = self.getConvexOutlinePoints(points)
        newConvex = []

        for i in convexOutline:
            points = list(filter(lambda item: item!=i,points))

        for i in range(len(convexOutline)-1):
            newConvex.append(convexOutline[i])
            for j in range(len(points)-1, -1, -1):
                if self.point_on_line(convexOutline[i], convexOutline[i+1], points[j]):
                    newConvex.append(points.pop(j))

        newConvex.append(convexOutline[len(convexOutline)-1])
        for j in range(len(points)-1, -1, -1):
            if self.point_on_line(convexOutline[len(convexOutline)-1], convexOutline[0], points[j]):
                newConvex.append(points.pop(j))

        return newConvex

    def point_on_line(self, A , B , C) -> bool:
        if (A.x == B.x):
            v = [A.y, B.y]
            if C.x == A.x and C.y >= min(v) and C.y <= max(v):
                return True
            else:
                return False
        else:
            m = (B.y - A.y) / (B.x - A.x)
            b = A.y - m * A.x

            if C.y == m * C.x + b:
                if (A.x <= C.x <= B.x or B.x <= C.x <= A.x) and (A.y <= C.y <= B.y or B.y <= C.y <= A.y):
                    return True
                else:
                    return False
            else:
                return False

    def getStartPoints(self):
        outlinePoints = self.getFullOutlinePoints()

        avg_x = self.avg(list(map(lambda x: x.x, self.points)))
        avg_y = self.avg(list(map(lambda x: x.y, self.points)))

        first_point = max(outlinePoints, key=lambda x: abs(x.x)+abs(x.y))
        self.points.remove(first_point)
        second_point = min(self.points, key=lambda x: first_point.lenghtTo(x))

        return [first_point, second_point]
