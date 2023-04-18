import subprocess, os, platform, svgwrite
from pathlib import Path

class Visualizer:
    """
    Class that contains funktions to visualize given databases of points and lines in scalable vector grafics (SVG).
    """

    def __init__(self):
        pass

    def generateLineSVG(self, filepath, points):
        """
        funktion to render a list of points with lines to an SVG file.
        """
        offset = self.calculateOffset(points)

        dwg = svgwrite.Drawing(filepath, profile="tiny")

        for i in range(len(points)-1):
            dwg.add(dwg.line((points[i].x+offset["x"], points[i].y+offset["y"]), (points[i+1].x+offset["x"], points[i+1].y+offset["y"]), stroke=svgwrite.rgb(80, 80, 80)))

        for point in points:
            dwg.add(dwg.circle(center=(point.x+offset["x"], point.y+offset["y"]), r=2))

        dwg.save()
        return Path(filepath)

    def generateAndShowWithSystemViewerLineSVG(self, points):
        """
        generates a SVG file with "self.generateLineSVG()" and opens it with systemviewer.
        """

        for i in ((list(map(lambda x: str(x.x)+", "+ str(x.y), points)))):
            print(i)
        print()

        path = self.generateLineSVG("tmp.svg", points)
        self.openWithSystemViewer(path)


    def openWithSystemViewer(self, path):
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', path))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(path)
        else:                                   # linux variants0
            subprocess.call(('xdg-open', path), stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=3)

    def calculateOffset(self, points):
        x_values = list(map(lambda o: o.x, points))
        y_values = list(map(lambda o: o.y, points))

        offsetx = -(min(x_values)) + 5
        offsety = -(min(y_values)) + 5

        return {"x": offsetx, "y": offsety}

