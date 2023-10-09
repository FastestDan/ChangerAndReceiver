import time
import socket
import sys
import os
import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia

import PictureReceiver
from PC_UI import Ui_PictureChanger
from PR_UI import Ui_PictureReceiver


PICS = ["FD'S LOGO 3.0 MINI.png", "Фотография Кота Дэна.png", "Фотография Сана.png", "Птица Варя.png"]

class PC(QMainWindow, Ui_PictureChanger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PC_Button.clicked.connect(self.remocon)
        self.pr = PR()
        self.pr.show()

    def remocon(self):
        self.pr.showtime()


class PR(QMainWindow, Ui_PictureReceiver):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showtime(self):
        picnum = random.randint(0, 3)
        self.pic = QPixmap(PICS[picnum])
        self.PR_Screen.setPixmap(self.pic)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


form1 = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form1 = PC()
    form1.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

