import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_mypagewindow = uic.loadUiType("ui//MyPageDialog.ui")[0]



class MyPageWindow(QDialog, QWidget, form_mypagewindow):
    def __init__(self):    
        super(MyPageWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.FriendListAdd()
        self.LoadMyNickName()
            
    def FriendListAdd(self):
        #while(): db 행 갯수만큼 반복 혹은 index null 값이 나올때 까지
        StrNickname = "test"#db 불러오기
        BoolOnline = 1# db 불러오기
        BoolFriend = 1 #db 불러오기
        if(BoolFriend == 1 and BoolOnline == 1):
            self.FriendList.addItem(StrNickname)
            
    def LoadMyNickName(self):
        StrNickname = "test"#db 불러오기
        self.NickNameDisplayLabel.setText(StrNickname)
    
    
        
        
        
            