import socket
import sys
import os
import random

from PyQt5.QtWidgets import QApplication, QMainWindow

from PC_UI import Ui_PictureChanger


PICS = ["Picture1.png", "Picture2.png", "Picture3.png", "Picture4.png"]


class PC(QMainWindow, Ui_PictureChanger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PC_Button.clicked.connect(self.remocon)

        self.socket = socket.socket()

        # Initialize the host
        self.host = socket.gethostname()

        # Initialize the port
        self.port = 8090

        # Bind the socket with port and host
        self.socket.bind(('', self.port))

        print("waiting for connections...")

        # listening for connections
        self.socket.listen()

        # accepting the incoming connections
        self.conn, self.addr = self.socket.accept()

        print(self.addr, "is connected to server")
        # self.pr = PR()
        # self.pr.show()

    def remocon(self):
        # take command as input
        picnum = random.randint(0, 3)
        pic = open(PICS[picnum], 'rb')
        picsize = os.path.getsize(PICS[picnum])
        command = pic.read(picsize)

        self.conn.send(command)

        print("Command has been sent successfully.")

        # # receive the confirmation
        # data = self.conn.recv(1024)
        #
        # if data:
        #     print("command received and executed successfully.")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


form = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PC()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

