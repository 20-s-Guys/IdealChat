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
        self.signin.clicked.connect(self.SignInBtn_clicked)
        
    # 버튼이 클릭될 때 새로운 창 생성
    def SignUpBtn_clicked(self):
        self.hide()
        self.SignUpWindow = SignUpWindow()
        self.SignUpWindow.exec()
        self.show()
        
    def SignInBtn_clicked(self):
        self.hide()
        self.SignInWindow = SignInWindow()
        self.SignInWindow.exec()
        boolLoginSuccess = self.SignInWindow.LoginStatus
        if(boolLoginSuccess == 1):
            #마이페이지가 닫히면 메인 창이 다시 보임.
            self.SignInWindow.MyPageWindow.exec()
            self.show()
        else:
            #로그인 닫히면 메인 창이 다시 보임.
            self.show()
            
            


app = QApplication(sys.argv)
MainWindow = MainWindow()
MainWindow.show()
app.exec_()