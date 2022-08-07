from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

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
        userName = self.LE_UserName.text()
        userLastName = self.LE_UserLastName.text()
        userEmail = self.LE_UserEmail.text()
        companyName = self.LE_CompanyName.text()

        print(userName)

