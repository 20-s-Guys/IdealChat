import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_mypagewindow = uic.loadUiType("ui//mypage.ui")[0]

class MyPageWindow(QMainWindow, form_mypagewindow):
    def __init__(self):    
        super(MyPageWindow, self).__init__()
        self.setupUi(self)
        self.show()