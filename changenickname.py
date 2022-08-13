import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_changenickwindow = uic.loadUiType("ui//changenickname.ui")[0]

#MySQL

#회원가입
class ChangeMyNickWindow(QDialog, QWidget, form_changenickwindow):
    def __init__(self):    
        super(ChangeMyNickWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.ChangeButton.clicked.connect(self.ChangeMyNickName)
        
    def ChangeMyNickName(self):
        ChangeMyNickWindow.EditNickName = self.ChangeNickNameLineEdit.text()
        #db에 넘김
        QMessageBox.about(self,"Successed","닉네임이 변경되었습니다!")
        self.close()
        