# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PC_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PictureChanger(object):
    def setupUi(self, PictureChanger):
        PictureChanger.setObjectName("PictureChanger")
        PictureChanger.resize(900, 900)
        self.centralwidget = QtWidgets.QWidget(PictureChanger)
        self.centralwidget.setObjectName("centralwidget")
        self.PC_Button = QtWidgets.QPushButton(self.centralwidget)
        self.PC_Button.setGeometry(QtCore.QRect(375, 380, 191, 71))
        self.PC_Button.setObjectName("PC_Button")
        PictureChanger.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PictureChanger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 24))
        self.menubar.setObjectName("menubar")
        PictureChanger.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PictureChanger)
        self.statusbar.setObjectName("statusbar")
        PictureChanger.setStatusBar(self.statusbar)

        self.retranslateUi(PictureChanger)
        QtCore.QMetaObject.connectSlotsByName(PictureChanger)

    def retranslateUi(self, PictureChanger):
        _translate = QtCore.QCoreApplication.translate
        PictureChanger.setWindowTitle(_translate("PictureChanger", "PictureChanger"))
        self.PC_Button.setText(_translate("PictureChanger", "PUSH!"))