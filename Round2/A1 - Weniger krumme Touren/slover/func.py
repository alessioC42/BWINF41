from functools import cmp_to_key
from visualizer import Visualizer as Vis
from point import P
vis = Vis()


def first(n, lst):
    if len(lst) < n:
        return lst
    else:
        return lst[:n]

def isValidAngleList(path, distancemap):
    if not (len(path) <2):
        A:P = path[-2]
        B:P = path[-1]

        if(A.x==B.x):
            if(A.y<B.y):
                return list(filter(lambda C: C[1].y>=B.y, distancemap))
            elif(A.y>B.y):
                return list(filter(lambda C: C[1].y<= B.y, distancemap))
            else: return True #Both points are the same
        elif(A.y==B.y):
            if(A.x<B.x):
                return list(filter(lambda C: C[1].x>= B.x, distancemap))
            elif(A.x>B.x):
                return list(filter(lambda C: C[1].x<= B.x, distancemap))
        elif(A.x>B.x):
            m = -((A.x-B.x)/(A.y-B.y))
            b = B.y - (m*B.x)

            if (A.y > B.y):
                return list(filter(lambda C: (C[1].y <= m*C[1].x+b), distancemap))
            elif (A.y < B.y):
                return list(filter(lambda C: (C[1].y >= m*C[1].x+b), distancemap))
            
        elif(A.x < B.x):
            m = -((A.x-B.x)/(A.y-B.y))
            b = B.y - (m*B.x)
            
            if (A.y > B.y):
                return list(filter(lambda C: (C[1].y <= m*C[1].x+b), distancemap))
            elif (A.y < B.y):
                return list(filter(lambda C: (C[1].y >= m*C[1].x+b), distancemap))

            return []
        else: return []
    else: return distancemap

def isValidAngle(A, B, C):
    if(A.x==B.x):
        if(A.y<B.y):
            return C.y>=B.y
        elif(A.y>B.y):
            return C.y<= B.y
        else: 
            print("lala")
            return True
    elif(A.y==B.y):
        if(A.x<B.x):
            return C.x>= B.x
        elif(A.x>B.x):
            return C.x<= B.x
    elif(A.x>B.x):
        m = -((A.x-B.x)/(A.y-B.y))
        b = B.y - (m*B.x)

        if (A.y > B.y):
            return (C.y <= m*C.x+b)
        elif (A.y < B.y):
            return (C.y >= m*C.x+b)
        
    elif(A.x < B.x):
        m = -((A.x-B.x)/(A.y-B.y))
        b = B.y - (m*B.x)
        
        if (A.y > B.y):
            return (C.y <= m*C.x+b)
        elif (A.y < B.y):
            return (C.y >= m*C.x+b)

def step(path:list[P], points:list[P] ,endLen:int, depth:int=2):
    if (len(path) == endLen):
        vis.generateAndShowWithSystemViewerLineSVG(path)
        print("points: "+str(endLen))
        print("total lenght: "+str(getTotalLenght(path)))
        return 0

    lastpoint = path[-1]
    distancemap = list(map(lambda x: [lastpoint.lenghtTo(x), x], points.copy()))
    distancemap = isValidAngleList(path, distancemap)


    if(len(distancemap) == 0):
        return -1

    distancemap = sorted(distancemap, key=lambda x: x[0])

    for point in first(depth, distancemap):
        newPath = path.copy()
        newpoints = points.copy()
        newPath += [point[1]]
        newpoints.remove(point[1])
        c = step(newPath, newpoints, endLen, depth)
        if (c == -1):
            continue
        elif (c==0):
            return 0
    return -1

def getTotalLenght(l:list[P]) -> float:
        lenght = 0
        for i in range(len(l)-1):
            lenght += l[i].lenghtTo(l[i+1])
        return lenght

def getImpossiblePoints(convex):
    impossible = []
    cv = [convex[-1]] + convex.copy() + [convex[0]]
    for i in range(1, len(cv)-1):
        if not(isValidAngle(cv[i-1], cv[i], cv[i+1])):
            impossible.append(cv[i])
    return impossible

def getStartPoints(points):
    points = points.copy()
    convex = convexHull(points)
    impossiblePoints = getImpossiblePoints(convex)
    impossiblePointCount = len(impossiblePoints)
    if(impossiblePointCount >2):
        print("no solution possible!")
        exit()
    elif (impossiblePointCount >= 1):
        first_point = impossiblePoints[0]
        convex.remove(first_point)
        second_point = min(convex, key=lambda x: first_point.lenghtTo(x))
        return [first_point, second_point]
    else:
        first_point = max(convex, key=lambda x: abs(x.x)+abs(x.y))
        points.remove(first_point)
        second_point = min(points, key=lambda x: first_point.lenghtTo(x))
        return [first_point, second_point]    

def validPoints(path, points):
    points = points.copy()
    convex = convexHull(points)
    impossiblePoints = getImpossiblePoints(convex)
    impossiblePointCount = len(impossiblePoints)
    if(impossiblePointCount >2):
        return False
    elif (impossiblePointCount == 2):
        lastPoint = path[-1]
        if (lastPoint in impossiblePoints):
            return True
        else:
            return False
    else:
        return True

def dStr(p): #Debug-Str
    return "({}, {}) ".format(p.x, p.y)

def dList(pList): #Debug-Str-List
    p = map(dStr, pList)
    for i in p:
        print(i, end="")


##############################################
#  convex Hull code By: Kevin Joshi
#  https://www.geeksforgeeks.org/convex-hull-using-graham-scan/

def convexHull(points:list[P]):
    n = len(points)
    def nextToTop(S):
        return S[-2]
    
    def distSq(p1, p2):
        return ((p1.x - p2.x) * (p1.x - p2.x) +
                (p1.y - p2.y) * (p1.y - p2.y))

    def orientation(p, q, r):
        val = ((q.y - p.y) * (r.x - q.x) -
            (q.x - p.x) * (r.y - q.y))
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def compare(p1, p2):
        o = orientation(p0, p1, p2)
        if o == 0:
            if distSq(p0, p2) >= distSq(p0, p1):
                return -1
            else:
                return 1
        else:
            if o == 2:
                return -1
            else:
                return 1

    ymin = points[0].y
    min = 0
    for i in range(1, n):
        y = points[i].y
 
        if ((y < ymin) or
            (ymin == y and points[i].x < points[min].x)):
            ymin = points[i].y
            min = i
 
    points[0], points[min] = points[min], points[0]
 
    p0 = points[0]
    points = sorted(points, key=cmp_to_key(compare))
 
    m = 1
    for i in range(1, n):
        while ((i < n - 1) and (orientation(p0, points[i], points[i + 1]) == 0)):
            i += 1
 
        points[m] = points[i]
        m += 1

    if m < 3:
        return
 
    S = []
    S.append(points[0])
    S.append(points[1])
    S.append(points[2])
 
    for i in range(3, m):
        while ((len(S) > 1) and
        (orientation(nextToTop(S), S[-1], points[i]) != 2)):
            S.pop()
        S.append(points[i])
 
    return S
