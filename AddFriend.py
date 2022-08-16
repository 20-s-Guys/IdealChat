import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

Form_AddFriendWindow = uic.loadUiType("ui//AddFriend.ui")[0]

class AddFriendWindow(QDialog, QWidget, Form_AddFriendWindow):
    def __init__(self):    
        super(AddFriendWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.DelFriendButton.clicked.connect(self.AddFriend)
    
    def AddFriend(self):
        id = self.EnterFriendIdEdit.text()
        QMessageBox.about(self,"Successed","친구 추가 완료!")
        self.close()
        #db에 id 추가