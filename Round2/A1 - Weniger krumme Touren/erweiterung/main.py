from flask import Flask, send_file
from sys import exit as sysexit
from flask_socketio import SocketIO
from pathfinder import PathFinder
import argparse


app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return send_file("./site/index.html")

@app.route("/dir/<filename>")
def sendFile(filename):
    return send_file("./site/"+str(filename))


def sendUpdatedBestSVGData(SVG, lenght):
    global paths_found
    print("generated Better path.")
    socketio.emit("newBestSVG", {
        'data': SVG,
        'lenght': lenght
    })

paths_found = 0
def foundNewPath(SVG):
    global paths_found
    paths_found+=1
    socketio.emit("pathCoundUpdate", {
        'data': SVG,
        'paths_total': paths_found
    })

def finished():
    socketio.emit("finished", {
        'message': "all paths searched. Found a total of {} paths.".format(paths_found)
    })
    sysexit(0)

def main(filepath, port):
    task = PathFinder(filepath, sendUpdatedBestSVGData, foundNewPath, finished)
    task.start()
    app.run("localhost", port, False, False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='file as relative path')
    parser.add_argument('-p', '--port', help='port of flask server | 5000', default=5000)
    args = parser.parse_args()
    main(args.file, int(args.port))
