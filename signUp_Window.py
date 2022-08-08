import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic

form_signupwindow = uic.loadUiType("ui//signup.ui")[0]

class signupwindow(QMainWindow,QWidget,form_signupwindow):
    def __init__(self):
        super(signupwindow,self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.signupbutton.clicked.connect(self.SignUp)
        
    def SignUp(self):
        id = self.enterid.text()
        pw = self.enterpw.text()
        nick = self.nickname.text()
        print(id,pw,nick)
    
        