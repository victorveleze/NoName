import requests
from Classes.Utilities.Singleton import Singleton

SERVER_URL = "http://127.0.0.1:8000/"

class ActionManager(metaclass=Singleton):
    def __init__(self):
        print("[ActionManager] Action manager created")

    def loadAction(self, actionName, paramsMap, callback):
        print("[ActionManager] Loading action ", actionName)

        request = SERVER_URL + actionName + "/"
        actionRequest = requests.post(request, json = paramsMap)

        if actionRequest.status_code == 200:
            callback(actionRequest.json())
        else:
            self.failedActionCallback(actionRequest)


    def failedActionCallback(self, actionResponse):
        print("[ActionManager] Action failed with code ", actionResponse.status_code)
            

    def __del__(self):
        print("[ActionManager] Action manager deleted")
