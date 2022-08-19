import requests

class ActionManager():
    def __init__(self):
        print("Action manager created")

    def loadAction(self, actionName, param1, param2):
        print("Loading action %s username= %s, pass = %s", actionName, param1, param2)

        request = "http://127.0.0.1:8000/" + actionName + "/" + param1 + "/" + param2
        actionRequest = requests.get(request)

        print(actionRequest.text)

    def loadPost(self):
        jsonData = {
            'data' : {
                'name' : 'Victorr'
            }
        }
        request = requests.post("http://127.0.0.1:8000/PostR/", json = jsonData)

        print(request.text)


    def __del__(self):
        print("Action manager deleted")
