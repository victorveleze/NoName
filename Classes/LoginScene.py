from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from Classes.Utilities.ActionManager import ActionManager
from Classes.SignUpScene import SignUpScene

class LoginScene(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Resources/Scenes/LoginScene.ui", self)
        self.SignUpScene = SignUpScene()
        self.initUI()
    
        
    def initUI(self):
        self.setWindowTitle("No named app")

        self.PB_Login.setText("Login")
        self.PB_Login.clicked.connect(self.login)

        self.PB_NewUser.setText("Crear Usuario")
        self.PB_NewUser.clicked.connect(self.signUp)


    def login(self):
        username = self.LE_UserName.text()
        password = self.LE_UserPass.text()

        loginInfo = {
            "username" : username,
            "password" : password
        }
        ActionManager().loadAction("login", loginInfo, self.loginCallback)


    def signUp(self):
        self.SignUpScene.show()


    def loginCallback(self, actionResponse):
        print(actionResponse)
