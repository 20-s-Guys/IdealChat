import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from mypage import MyPageWindow

form_signinwindow = uic.loadUiType("ui//signin.ui")[0]

#로그인
class SignInWindow(QMainWindow, form_signinwindow):
    def __init__(self):
        super(SignInWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.loginbutton.clicked.connect(self.login)
    
    def login(self):
        id = self.enterid.text()
        pw = self.enterpw.text()
        ip = requests.get("http://ip.jsontest.com").json()['ip']
        port = 2003
        
        #테스트
        print(id,pw,ip,port)
        
        #대강 로그인 하는 부분
        LoginStatus = 1
        #로그인 시스템에서 무슨 조건 충족
        if(LoginStatus == 1):
            QMessageBox.about(self,"Successed","로그인 성공!")
            self.MyPageWindow = MyPageWindow()
        else:
            QMessageBox.about(self,"Failed","로그인 실패!")
        
        
    

