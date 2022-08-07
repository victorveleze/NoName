from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from Classes.AddRemove import AddRemoveWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.AddRemoveWindow = AddRemoveWindow()
        uic.loadUi("Resources/Scenes/MainWindow.ui", self)
        self.initUI()


    def initUI(self):   
        self.setWindowTitle("No named app")

        self.PB_AddRemoveItems.setText("Agregar o quitar productos")
        self.PB_AddRemoveItems.clicked.connect(self.addRemoveItems)

        self.PB_Inventory.setText("Ver inventario")
        self.PB_Inventory.clicked.connect(self.showInventory)

        self.PB_Exit.setText("Salir")
        self.PB_Exit.clicked.connect(self.exit)


    def addRemoveItems(self):
        self.AddRemoveWindow.show()


    def showInventory(self):
        self.L_Test.setText("Inventario")


    def exit(self):
        self.L_Test.setText("Exit")