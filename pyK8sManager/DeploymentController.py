from kubernetes import client, config
import os


class DeploymentController:
    def __init__(self, namespace='default'):
        # check if we are inside a cluster or outside of cluster
        if os.getenv('KUBERNETES_SERVICE_HOST'):
            config.load_incluster_config()
        else:
            config.load_kube_config()

        self.namespace = namespace
        self.api_apps = client.AppsV1Api()
        self.api_service = client.CoreV1Api()

    def create_depl(self, deployment, namespace="default"):
        return self.api_apps.create_namespaced_deployment(body=deployment, namespace=namespace)

    def delete_depl(self, depl_name, namespace="default"):
        return self.api_apps.delete_namespaced_deployment(
            name=depl_name,
            namespace=namespace,
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))

    def update_depl(self, deployment, depl_name, namespace="default"):
        # depl_name = deployment.metadata.name
        return self.api_apps.patch_namespaced_deployment(
            name=depl_name,
            namespace=namespace,
            body=deployment)

    def create_svc(self, service, namespace="default"):
        return self.api_service.create_namespaced_service(body=service, namespace=namespace)

    def delete_svc(self, svc_name, namespace="default"):
        return self.api_service.delete_namespaced_service(
            name=svc_name,
            namespace=namespace)

    def update_svc(self, service, svc_name, namespace="default"):
        return self.api_service.patch_namespaced_service(
            name=svc_name,
            namespace=namespace,
            body=service)


