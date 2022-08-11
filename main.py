import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from signup import SignUpWindow
from signin import SignInWindow

form_mainwindow = uic.loadUiType("ui//main.ui")[0]

class MainWindow(QMainWindow, form_mainwindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    
    def initUI(self):
        self.setupUi(self)
        self.signup.clicked.connect(self.SignUpBtn_clicked)
        self.signin.clicked.connect(self.SignIpBtn_clicked)
        
    # 버튼이 클릭될 때 새로운 창 생성
    def SignUpBtn_clicked(self):
        self.hide()
        self.SignUpWindow = SignUpWindow()
        self.SignUpWindow.exec()
        self.show()
        
    def SignIpBtn_clicked(self):
        self.SignInWindow = SignInWindow()


app = QApplication(sys.argv)
MainWindow = MainWindow()
MainWindow.show()
app.exec_()