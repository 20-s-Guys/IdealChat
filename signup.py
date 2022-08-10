import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_signupwindow = uic.loadUiType("ui//signup.ui")[0]

#회원가입
class SignUpWindow(QMainWindow, form_signupwindow):
    def __init__(self, parent=None):    
        super(SignUpWindow, self).__init__(parent)
        self.setupUi(self)
        

app = QApplication(sys.argv)
MainWindow = SignUpWindow()
MainWindow.show()
app.exec_()