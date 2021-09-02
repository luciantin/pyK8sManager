from flask import Flask
from pyK8sManager.DeploymentManager import DeploymentManager

app = Flask(__name__)
DeplManager = DeploymentManager()

@app.route("/")
def hello():
    return "hello\n"

@app.route("/api/create/<string:type>/<int:id>")
def create(type,id):
    if type == "drone":
        depl = {
            "depl_name" : "drone-d-$id-a",
            "container_name"  : "drone-c-$id-a",
            "image" : "luciantin/virtual-drone",
            "label" :  {'app': "drone-d-$id-a"},
            "container_port" : 5000,
            "requests" : {"cpu": "100m", "memory": "200Mi"},
            "limits" : {"cpu": "500m", "memory": "500Mi"},
            "command": None,
        }

        NodePort = {
            "svc_name" : "drone-svc-np-$id-a",
            "type"  : "NodePort" ,
            "label" :  {},
            "selector" :  {"app" : "drone-d-$id-a"},
            "ports" : [[5000,30000]],
        }

        ClusterIP = {
            "svc_name": 'drone-svc-cip-$id-a',
            "type": "ClusterIP",
            "label": {'svc': 'drone-svc-cip-$id-a'},
            "selector": {'app': "drone-d-$id-a"},
            "ports": [[5000, 5000]]
        }

        settings = [
            {'settings':depl, 'dtype':'pod'},
            {'settings':NodePort, 'dtype':'service'},
            {'settings':ClusterIP, 'dtype':'service'},
        ]


        depl_id = DeplManager.get_new_id()

        DeplManager.save_settings(settings, "drone")

        print(DeplManager.instantiate_settings('drone',depl_id))
    return str(id)


@app.route("/api/delete/<string:id>")
def delete(id):
    id = DeplManager.delete(id)
    return str(id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
