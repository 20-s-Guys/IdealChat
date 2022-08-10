import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_signinwindow = uic.loadUiType("ui//signin.ui")[0]

#로그인
class SignInWindow(QMainWindow, form_signinwindow):
    def __init__(self, parent=None):
        super(SignInWindow, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
MainWindow = SignInWindow()
MainWindow.show()
app.exec_()