import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from changenickname import ChangeMyNickWindow
from time import sleep
from PyQt5.QtCore import *

form_mypagewindow = uic.loadUiType("ui//MyPageDialog.ui")[0]

class LoadFriendList(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self):
        while True:
            StrNickname = "test"#db 불러오기
            BoolOnline = 1# db 불러오기
            BoolFriend = 1 #db 불러오기
            if(BoolFriend == 1 and BoolOnline == 1):
                self.parent.FriendList.addItem(StrNickname)
                self.parent.list_count += 1
            #친구 리스트 새로 갱신
            sleep(5)
            self.parent.FriendList.clear()
            self.parent.list_count = 0

class MyPageWindow(QDialog, QWidget, QThread, form_mypagewindow):
    #클래서 변수
    list_count = 0
    MyNickName = "test"
    
    #기본 함수
    def __init__(self):    
        super(MyPageWindow, self).__init__()
        self.initUI()
        self.show()
    
    #창의 기능 함수
    def initUI(self):
        self.setupUi(self)
        self.LoadFriendList()
        self.LoadMyNickName()
        #self.AddFriend.clicked.connect()
        self.EditNicknameButton.clicked.connect(self.ChangeMyNickName)
        
    def LoadFriendList(self):
        x = LoadFriendList(self)
        x.start()
    
    
    #내 닉네임 변경 함수 
    def ChangeMyNickName(self):
        self.ChangeMyNickNameWindow = ChangeMyNickWindow()
        #db_data 로드 추가
        #DB 내 닉네임 변경
        self.ChangeMyNickNameWindow.exec()
        #for i in range(1, MyPageWindow.list_count):
        #    if("test" == MyPageWindow.MyNickName):
                #DB_NickName와 DB_TEST은 나중에 DB에서 데이터를 INSERT, LOAD 하는 항목으로 수정해야함!
        DB_NickName = ChangeMyNickWindow.EditNickName
        self.MyNickName = ChangeMyNickWindow.EditNickName
        self.NickNameDisplayLabel.setText(self.MyNickName)
                #테스트 부분
        print(DB_NickName)
                
                
    #내 닉네임 로드 함수
    def LoadMyNickName(self):
        MyPageWindow.MyNickName = "test"#db 불러오기
        print(self.MyNickName)
        self.NickNameDisplayLabel.setText(self.MyNickName)
    
    
        
        
        
            