# pyK8sManager
Abstraction over the kubernetes API for easier deployment and instantiation

# Structure

```
                                CreatePod
                                settings :
                                depl_name = "<<name>>"
                                container_name  = "<<name>>"
                                image = "<<image>>"
                                label =  {"<<name>>" : "<<name>>"}
                                container_port = <<int>>
                                requests= {"cpu": "100m", "memory": "200Mi"},
                                limits= {"cpu": "500m", "memory": "500Mi"}

                                CreateService
                                settings :
                                svc_name = "<<name>>"
                                type  = "<<name>>" , supported values: "ClusterIP", "NodePort"
                                label =  {"<<name>>" : "<<name>>"}
                                selector =  {"<<name>>" : "<<name>>"}
                                ports = [[x,y],[x,y],....]
                                   x - port                              ◄───┐
                                   y - target port                           │
                                                                             │
                                                                  ┌──────────┤
┌──────────────────────┐                                          │ Create   │
│                      │            ┌───────────────────────┐     │ Desc for │
│     Python Flask     │            │ Description Generator ├─────┤  Pod     │
│                      │            └─▲────────┬────────────┘     │   OR     │
│      "Lib Use"       │              │        │                  │ Service  │
│                      │              │        │                  └──────────┘
└──────────────────────┴──────────────┤        │
                                      │        │Deployment
                                      │        │Description
                                      │        │
                                      │        │
                                      │        │                  ┌────────────────────────────           Python OR
                                      │        │                  │             Save Deployment  ───────► Yaml format
┌──────────────────────┐            ┌─▼────────▼────────────┐     │ Pod         Delete -||-
│ Deployment Analytics ◄────────────┤  Deployment Manager   ├─────┤         ──►
└──────────┬───────────┘            └──────────┬────────────┘     │ Service     Instantiate with ID
           │                                   │                  │             Delete instance with ID
┌──────────┴──────────┐                        │                  │             Instance Analytics
│                     │                        │                  └────────────────────────────
│        Todo         │                        │
                                               │
                                               │Deployment
                                               │Description
                                               │
                                               │
                                               │                  ┌────────────────────────────
                                               │                  │             Create
                                    ┌──────────▼────────────┐     │ Pod
                                    │ Deployment Controller ├─────┤         ──► Update
                                    └───────────────────────┘     │ Service
                                      Kubernetes Connection       │             Delete
                                                                  └────────────────────────────
```

# Upload package to pypi
## Change version # in setup.py
```
> python setup.py sdist bdist_wheel
> twine upload dist/*
```
