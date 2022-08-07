from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class AddRemoveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Resources/Scenes/AddRemove.ui", self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Agregar o quitar productos")

    
