from string import Template
from pyK8sManager.DeploymentController import DeploymentController
from pyK8sManager.DescriptionGenerator import *


class DeploymentManager:
    def __init__(self):
        self.depl_controller = DeploymentController()

        self.ids = {}
        self.id_counter = 0

        self.settings = {}

    # settings is and array of settings dictionary [ {settings: settings, dtype:dtype}, .... ]
    def save_settings(self, settings, settings_id):
        self.settings[settings_id] = settings

    def delete_settings(self, settings_id):
        self.settings.pop(settings_id)

    def instantiate_settings(self, settings_id, depl_id):
        settings = self.settings[settings_id]

        for setting in settings:
            if setting['dtype'] == 'pod':
                setting['settings']["depl_name"] = Template(setting['settings']["depl_name"]).substitute(id=depl_id)
                for key in setting['settings']["label"]:
                    setting['settings']["label"][key] = Template(setting['settings']["label"][key]).substitute(id=depl_id)
                print(setting)
                self.depl_controller.create_depl(CreatePod(setting['settings']))


            if setting['dtype'] == 'service':
                setting['settings']["svc_name"] = Template(setting['settings']["svc_name"]).substitute(id=depl_id)
                for key in setting['settings']["selector"]:
                    setting['settings']["selector"][key] = Template(setting['settings']["selector"][key]).substitute(id=depl_id)
                for key in setting['settings']["label"]:
                    setting['settings']["label"][key] = Template(setting['settings']["label"][key]).substitute(id=depl_id)
                print(setting)
                self.depl_controller.create_svc(CreateService(setting['settings']))
        
        # names, depl_settings, svc_settings, svc_np_settings = self.create_drone(id)
        # self.ids[id] = names

        # self.depl_controller.create_depl(depl_settings)
        # self.depl_controller.create_svc(svc_settings)
        # self.depl_controller.create_svc(svc_np_settings)

        return settings

    # def delete_instance_with_id(self, id):
    #     if int(id) in self.ids:
    #         names = self.ids[int(id)]
    #         self.depl_controller.delete_depl(names[0])
    #         self.depl_controller.delete_svc(names[1])
    #         self.depl_controller.delete_svc(names[2])
    #         return 1
    #     else:
    #         return -1

    def delete_settings_instance(self, settings_id):
        for settings in self.settings[settings_id]:
            if settings['dtype'] == 'pod':
                self.depl_controller.delete_depl(settings['settings']["depl_name"])
            if settings['dtype'] == 'service':
                self.depl_controller.delete_svc(settings['settings']["svc_name"])

    def get_new_id(self):
        self.id_counter += 1
        return self.id_counter

    def get_instance_url(self, settings_id):
        for settings in self.settings[settings_id]:
            if settings['dtype'] == 'service':
                if settings['settings']['type'] == 'ClusterIP':
                    return {
                        'url':"'{}'.helloworldsvc.test.svc.cluster.local".format(settings['settings']['svc_name']),
                        'port':settings['settings']['ports']
                    }

    # test deployment
    # def create_drone(self, id):
    #     depl_name = Template("drone-$id").substitute(id=id)
    #     svc_name = Template("drone-svc-$id").substitute(id=id)
    #     container_name = Template("drone-c-$id").substitute(id=id)
    #     np_svc_name = Template("drone-svc-np-$id").substitute(id=id)

    #     depl_settings = {
    #         "depl_name": depl_name,
    #         "container_name": container_name,
    #         "image": "luciantin/virtual-drone",
    #         "label": {'app': container_name},
    #         "container_port": 80,
    #         "command": None,
    #     }

    #     svc_settings = {
    #         "svc_name": svc_name,
    #         "type": "ClusterIP",
    #         "label": {'svc': svc_name},
    #         "selector": {'app': container_name},
    #         "ports": [[5000, 5000]]
    #     }

    #     svc_np_settings = {
    #         "svc_name": np_svc_name,
    #         "type": "NodePort",
    #         "label": None,
    #         "selector": {'app': container_name},
    #         "ports": [[5000, 5000]]
    #     }
    #     names = [depl_name, svc_name, np_svc_name]
    #     return names, CreatePod(depl_settings), CreateService(svc_settings), CreateService(svc_np_settings)
