from kubernetes import client, config

# CreatePod
# settings :
# depl_name = "<<name>>"
# container_name  = "<<name>>"
# image = "<<image>>"
# label =  {"<<name>>" : "<<name>>"}
# container_port = <<int>>
# requests= {"cpu": "100m", "memory": "200Mi"},
# limits= {"cpu": "500m", "memory": "500Mi"}



def CreatePod(settings):
    container = client.V1Container(
        name=settings['container_name'],
        image=settings["image"],
        ports=[client.V1ContainerPort(container_port=settings["container_port"])],
        resources=client.V1ResourceRequirements(
            requests=settings["requests"],
            limits=settings["limits"]
        ),
        command=settings["command"]
    )

    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels=settings["label"]),
        spec=client.V1PodSpec(containers=[container]))

    spec = client.V1DeploymentSpec(
        replicas=1,
        template=template,
        selector={'matchLabels': settings["label"]})

    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=settings["depl_name"]),
        spec=spec)

    return deployment


# CreateService
# settings :
# svc_name = "<<name>>"
# type  = "<<name>>" , supported values: "ClusterIP", TODO TEST "NodePort"
# label =  {"<<name>>" : "<<name>>"}
# selector =  {"<<name>>" : "<<name>>"}
# ports = [[x,y],[x,y],....]
#    x - port
#    y - target port

def CreateService(settings):
    metadata = client.V1ObjectMeta(
        name=settings["svc_name"],
        labels=settings["label"]
    )

    ports = list()
    if settings['type'] == 'NodePort':
        for port in settings["ports"]:
            k_port = client.V1ServicePort(port=port[0], target_port=port[0], node_port=port[1])
            ports.append(k_port)

    else :
        for port in settings["ports"]:
            k_port = client.V1ServicePort(port=port[0], target_port=port[1])
            ports.append(k_port)

    spec = client.V1ServiceSpec(
        type=settings["type"],
        selector=settings["selector"],
        ports=ports
    )

    service = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=metadata,
        spec=spec
    )

    return service
