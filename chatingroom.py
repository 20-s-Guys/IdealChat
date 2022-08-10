import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_chatwindow = uic.loadUiType("ui//chatingroom.ui")[0]

class ChatRoomWindow(QMainWindow, form_chatwindow):
    def __init__(self, parent=None):    
        super(ChatRoomWindow, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
MainWindow = ChatRoomWindow()
MainWindow.show()
app.exec_()