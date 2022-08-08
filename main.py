import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import

import signUp_Window
#UI파일 연결 코드
UI_class = uic.loadUiType("ui//main.ui")[0]

class WindowClass(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.signup.clicked.connect(self.btnSecond)
    
    def btnCLick(self):
        print("버튼이 클릭되었습니다.")
        
    def btnSecond(self):
        self.hide()
        self.second = signUp_Window.signupwindow()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
