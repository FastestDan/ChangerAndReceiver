# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PR_IN_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HostIn(object):
    def setupUi(self, HostIn):
        HostIn.setObjectName("HostIn")
        HostIn.resize(700, 200)
        HostIn.setMinimumSize(QtCore.QSize(700, 200))
        HostIn.setMaximumSize(QtCore.QSize(700, 200))
        self.ErrorPhrase = QtWidgets.QLabel(HostIn)
        self.ErrorPhrase.setGeometry(QtCore.QRect(-2, 120, 701, 71))
        self.ErrorPhrase.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorPhrase.setObjectName("ErrorPhrase")
        self.horizontalLayoutWidget = QtWidgets.QWidget(HostIn)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 701, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EnterPhrase = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.EnterPhrase.setObjectName("EnterPhrase")
        self.horizontalLayout.addWidget(self.EnterPhrase)
        self.EnterInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.EnterInput.setText("")
        self.EnterInput.setAlignment(QtCore.Qt.AlignCenter)
        self.EnterInput.setObjectName("EnterInput")
        self.horizontalLayout.addWidget(self.EnterInput)
        self.EnterPush = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.EnterPush.setObjectName("EnterPush")
        self.horizontalLayout.addWidget(self.EnterPush)

        self.retranslateUi(HostIn)
        QtCore.QMetaObject.connectSlotsByName(HostIn)

    def retranslateUi(self, HostIn):
        _translate = QtCore.QCoreApplication.translate
        HostIn.setWindowTitle(_translate("HostIn", "IP Input"))
        self.ErrorPhrase.setText(_translate("HostIn", "Ask the server user for IP!"))
        self.EnterPhrase.setText(_translate("HostIn", "Input server IP:"))
        self.EnterPush.setText(_translate("HostIn", "Enter"))
