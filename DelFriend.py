import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

Form_DelFriendWindow = uic.loadUiType("ui//DelFriend.ui")[0]

class DelFriendWindow(QDialog, QWidget, Form_DelFriendWindow):
    def __init__(self):    
        super(DelFriendWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.DelFriendButton.clicked.connect(self.DelFriend)
    
    def DelFriend(self):
        id = self.EnterFriendIdEdit.text()
        QMessageBox.about(self,"Successed","친구 삭제 완료!")
        self.close()
        #db에 id 삭제