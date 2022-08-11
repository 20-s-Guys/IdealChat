import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_signupwindow = uic.loadUiType("ui//signup.ui")[0]

#MySQL

#회원가입
class SignUpWindow(QMainWindow, form_signupwindow):
    def __init__(self):    
        super(SignUpWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.signupbutton.clicked.connect(self.signup)
        
   
        
    def signup(self):
        id = self.enterid.text()
        pw = self.enterpw.text()
        pw2 = self.enterpw2.text()
        nickname = self.enternickname.text()
        print(id,pw,nickname)
        
        self.check(pw, pw2, id)
    
    def check(self, pw, re_pw, id):
        #pw 확인 / id 중복 확인
        if pw != re_pw :
            QMessageBox.about(self,"Failed","비밀번호가 같지 않습니다!")    
        elif self.checkID(id) == -1:
            QMessageBox.about(self,"Failed","이미 사용중인 ID 입니다!")
        else:
            QMessageBox.about(self,"Successed!","회원가입 완료!")
            self.close()
            
    
    def checkID(self, id):
        #db에서 id 목록 가져와서 비교 하는거 구현 예정
        return -1
            