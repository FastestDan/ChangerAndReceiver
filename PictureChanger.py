import socket
import sys
import random
import os

import PyQt5
from PyQt5.QtCore import Qt, QEventLoop
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from PC_UI import Ui_PictureChanger
from PC_IN_UI import Ui_HostGo


SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 8090
SOCKET.bind((HOST, PORT))
CONN = None
ADDR = None


class PC(QMainWindow, Ui_PictureChanger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PC_Button.clicked.connect(self.remocon)

    def remocon(self):
        picnum = str(random.randint(0, 3))
        CONN.send(picnum.encode())

        print("command sent")

    def anone(self):
        a = PC_Entrance()
        a.show()
        a.setAttribute(Qt.WA_DeleteOnClose)
        loop = QEventLoop()
        a.destroyed.connect(loop.quit)
        loop.exec()

    @staticmethod
    def check():
        if CONN is None or ADDR is None:
            return -1
        else:
            return 0


class PC_Entrance(QWidget, Ui_HostGo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.OnPush.clicked.connect(self.wait)
        self.IPPhrase.setText(socket.gethostbyname(HOST))
        self.IPPhrase.setReadOnly(True)

    def wait(self):
        global CONN, ADDR
        self.ShowPhrase.setText("Waiting for connection...")
        print("waiting for connection...")
        SOCKET.listen()
        CONN, ADDR = SOCKET.accept()
        print("connected")
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


form = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PC()
    form.anone()
    a = form.check()
    if a < 0:
        sys.exit()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())