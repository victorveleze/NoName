from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class MainScene(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Resources/Scenes/MainScene.ui", self)
        self.initUI()


    def initUI(self):   
        pass