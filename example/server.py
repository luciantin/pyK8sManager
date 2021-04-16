from flask import Flask
from pyK8sManager import deplManager

app = Flask(__name__)
DeplManager = deplManager.DeplManager()

@app.route("/")
def hello():
    return "hello\n"

@app.route("/api/create/<string:type>")
def create(type):
    id = -1
    if type == "drone":
        id = DeplManager.create(type)
    return str(id)


@app.route("/api/delete/<string:id>")
def delete(id):
    id = DeplManager.delete(id)
    return str(id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
