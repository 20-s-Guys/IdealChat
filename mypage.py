import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_mypagewindow = uic.loadUiType("ui//mypage.ui")[0]

class MyPageWindow(QMainWindow, form_mypagewindow):
    def __init__(self, parent=None):    
        super(MyPageWindow, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
MainWindow = MyPageWindow()
MainWindow.show()
app.exec_()