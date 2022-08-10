from ipaddress import ip_address
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests

form_signinwindow = uic.loadUiType("ui//signin.ui")[0]

#로그인
class SignInWindow(QMainWindow, form_signinwindow):
    def __init__(self):
        super(SignInWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.loginbutton.clicked.connect(self.login)
    
    def login(self):
        id = self.enterid.text()
        pw = self.enterpw.text()
        ip = requests.get("http://ip.jsontest.com").json()['ip']
        port = 2003
        
        print(id,pw,ip,port)
    

