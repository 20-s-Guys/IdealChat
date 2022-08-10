import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_signupwindow = uic.loadUiType("ui//signup.ui")[0]

#회원가입
class SignUpWindow(QMainWindow, form_signupwindow):
    def __init__(self):    
        super(SignUpWindow, self).__init__()
        self.setupUi(self)
        self.show()
        
