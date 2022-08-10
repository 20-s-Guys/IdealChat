import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_signinwindow = uic.loadUiType("ui//signin.ui")[0]

#로그인
class SignInWindow(QMainWindow, form_signinwindow):
    def __init__(self):
        super(SignInWindow, self).__init__()
        self.setupUi(self)
        self.show()

