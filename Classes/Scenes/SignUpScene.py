from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from Classes.Utilities.ActionManager import ActionManager

class SignUpScene(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Resources/Scenes/SignUpScene.ui", self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Registrarse")

        self.PB_Submit.setText("Enviar")
        self.PB_Submit.clicked.connect(self.submit)


    def submit(self):
        userInfo = {
            "user_name" : self.LE_UserName.text(),
            "user_last_name" : self.LE_UserLastName.text(),
            "user_email" : self.LE_UserEmail.text(),
            "company_name" : self.LE_CompanyName.text(),
            "password" : self.LE_Password.text()
        }

        ActionManager().loadAction("addUser", userInfo, self.submitCallback)


    def submitCallback(self, response):
        print(response)

