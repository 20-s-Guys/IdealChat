import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_changenickwindow = uic.loadUiType("ui//changenickname.ui")[0]

#MySQL

#회원가입
class ChangeNickWindow(QDialog, QWidget, form_changenickwindow):
    def __init__(self):    
        super(ChangeNickWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.ChangeButton.clicked.connect(self.ChangeMyNickName)
        
    def ChangeMyNickName(self):
        StrNickname = self.ChangeNickNameLineEdit.text()
        #db에 넘김