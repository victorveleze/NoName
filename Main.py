import sys
from PyQt5.QtWidgets import QApplication
from Classes.LoginScene import LoginScene

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = LoginScene()
    GUI.show()
    sys.exit(app.exec())