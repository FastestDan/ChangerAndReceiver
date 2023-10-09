import time
import socket
import sys
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from PR_UI import Ui_PictureReceiver


class PictureReceiver(QMainWindow, Ui_PictureReceiver):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Initialize s to socket
        self.socket = socket.socket()

        # Initialize the host
        self.host = "127.0.0.1"

        # Initialize the port
        self.port = 8090

        # bind the socket with port and host
        self.socket.connect((self.host, self.port))

        print("Connected to Server.")

    def rectime(self):
        # receive the command from master program
        pic = open("received.png", "wb")
        data = None
        while True:
            comm = self.socket.recv(1024)
            data = comm
            if comm:
                while comm:
                    comm = self.socket.recv(1024)
                    data += comm
                else:
                    break
        pic.write(data)
        pic.close()
        pixmap = QPixmap("received.png")
        self.PR_Screen.setPixmap(pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


form = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PictureReceiver()
    form.show()
    form.rectime()
    sys.excepthook = except_hook
    sys.exit(app.exec())
