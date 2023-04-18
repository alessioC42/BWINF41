import svgwrite

class Visualizer:
    def __init__(self, points):
        self.offset = self.calculateOffset(points)

    def generateLineSVG(self, points):
        if (len(points) == 0):
            return "<h1>ERROR!</h1>"

        dwg = svgwrite.Drawing("",size=("700px", "500px") , profile="full")

        for i in range(len(points)-1):
            dwg.add(dwg.line((points[i].x+self.offset["x"], points[i].y+self.offset["y"]), (points[i+1].x+self.offset["x"], points[i+1].y+self.offset["y"]), stroke=svgwrite.rgb(80, 80, 80)))

        for point in points:
            dwg.add(dwg.circle(center=(point.x+self.offset["x"], point.y+self.offset["y"]), r=2))

        return dwg.tostring()

    def calculateOffset(self, points):
        x_values = list(map(lambda o: o.x, points))
        y_values = list(map(lambda o: o.y, points))

        offsetx = -(min(x_values)) + 5
        offsety = -(min(y_values)) + 5

        return {"x": offsetx, "y": offsety}

