import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_mainwindow = uic.loadUiType("ui//main.ui")[0]
form_signupwindow = uic.loadUiType("ui//signup.ui")[0]
form_signinwindow = uic.loadUiType("ui//signin.ui")[0]

#회원가입
class SignUpWindow(QMainWindow, form_signupwindow):
    def __init__(self, parent=None):    
        super(SignUpWindow, self).__init__(parent)
        self.setupUi(self)

#메인
class MainWindow(QMainWindow, form_mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signup.clicked.connect(self.SignUpBctn_clicked)
        self.signin.clicked.connect(self.SignIpBtn_clicked)
        
    # 버튼이 클릭될 때 새로운 창 생성
    def SignUpBctn_clicked(self):
        self.SignUpWindow = SignUpWindow(self)
        self.SignUpWindow.show()
        
    def SignIpBtn_clicked(self):
        self.SignInWindow = SignInWindow(self)
        self.SignInWindow.show()


app = QApplication(sys.argv)
MainWindow = MainWindow()
MainWindow.show()
app.exec_()