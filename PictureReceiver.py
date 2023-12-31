import socket
import sys
import threading

from PyQt5.QtCore import Qt, QEventLoop
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from PR_UI import Ui_PictureReceiver
from PR_IN_UI import Ui_HostIn

PICS = ["Picture1.png", "Picture2.png", "Picture3.png", "Picture4.png"]
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = None
PORT = 8090


class PictureReceiver(QMainWindow, Ui_PictureReceiver):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def startup(self):
        rec = threading.Thread(target=self.rectime)
        rec.start()

    def rectime(self):
        while True:
            try:
                picnum = int(SOCKET.recv(1024).decode())
                print("num got")
                self.picchange(picnum)
            except ValueError:
                break
        print("disconnect")
        self.PR_Screen.setText("Connection is Terminated. Please restart.")

    def picchange(self, picnum):
        pixmap = QPixmap(PICS[picnum])
        self.PR_Screen.setPixmap(pixmap)

    def jotto(self):
        a = PR_Entrance()
        a.setAttribute(Qt.WA_DeleteOnClose)
        a.show()
        loop = QEventLoop()
        a.destroyed.connect(loop.quit)
        loop.exec()

    @staticmethod
    def check():
        global HOST
        if HOST is None:
            return -1
        else:
            return 0


class PR_Entrance(QWidget, Ui_HostIn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.EnterPush.clicked.connect(self.binding)

    def binding(self):
        global HOST
        HOST = self.EnterInput.text()
        try:
            self.ErrorPhrase.setText("Connecting. Please wait.")
            SOCKET.connect((HOST, PORT))
            print("connected")
            self.close()
        except Exception as e:
            if e.__class__.__name__ == "TimeoutError":
                print("timeout")
                self.ErrorPhrase.setText("Timeout or wrong IP. Try again.")
            else:
                self.ErrorPhrase.setText("Wrong IP. Try again.")
            HOST = None


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


form = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PictureReceiver()
    form.jotto()
    a = form.check()
    if a < 0:
        sys.exit()
    form.show()
    form.startup()
    sys.excepthook = except_hook
    sys.exit(app.exec())

