# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/remoterouter.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 400)
        MainWindow.setMinimumSize(QtCore.QSize(493, 400))
        MainWindow.setMaximumSize(QtCore.QSize(493, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Logo/logomikhotman.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(f'background: {MainWindow.BGVIEW}')
        self.txtHost = QtWidgets.QLineEdit(self.centralwidget)
        self.txtHost.setGeometry(QtCore.QRect(40, 80, 421, 41))
        self.txtHost.setMouseTracking(False)
        self.txtHost.setObjectName("txtHost")
        self.txtHost.textChanged.connect(lambda: self.singleBlankCheck(self.txtHost))
        self.txtHost.setFocus()
        self.txtUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsername.setGeometry(QtCore.QRect(40, 150, 421, 41))
        self.txtUsername.setMouseTracking(False)
        self.txtUsername.setObjectName("txtUsername")
        self.txtUsername.textChanged.connect(lambda: self.singleBlankCheck(self.txtUsername))
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(40, 220, 421, 41))
        self.txtPassword.setMouseTracking(False)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setCursorPosition(0)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.textChanged.connect(lambda: self.singleBlankCheck(self.txtPassword))
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(40, 310, 181, 41))
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.clicked.connect(MainWindow.close)
        self.btnRemote = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemote.setGeometry(QtCore.QRect(270, 310, 191, 41))
        self.btnRemote.setObjectName("btnRemote")
        self.btnRemote.clicked.connect(self.remote)
        self.ckShowPassword = QtWidgets.QCheckBox(self.centralwidget)
        self.ckShowPassword.setGeometry(QtCore.QRect(40, 270, 121, 23))
        self.ckShowPassword.setObjectName("ckShowPassword")
        self.ckShowPassword.toggled.connect(lambda: self.showPassword(self.ckShowPassword))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(3, 20, 491, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.MainWindow = MainWindow
        self.defineEvents()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtHost, self.txtUsername)
        MainWindow.setTabOrder(self.txtUsername, self.txtPassword)
        MainWindow.setTabOrder(self.txtPassword, self.ckShowPassword)
        MainWindow.setTabOrder(self.ckShowPassword, self.btnRemote)
        MainWindow.setTabOrder(self.btnRemote, self.btnCancel)

    def defineEvents(self):
        txts = [self.txtHost, self.txtUsername, self.txtPassword]
        for txt in txts:
            txt.returnPressed.connect(self.remote)

    def showPassword(self, btn):
        if btn.isChecked() == True:
            self.txtPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.txtPassword.setEchoMode(QLineEdit.Password)

    def singleBlankCheck(self, txt):
        if txt.text() == '':
            txt.setStyleSheet('border: 1px solid red')
        else:
            txt.setStyleSheet('border: 1px solid #ABABAB')

    def blankCheck(self):
        txts = [self.txtHost, self.txtUsername, self.txtPassword]

        blank = True
        for txt in txts:
            if txt.text() == '':
                txt.setStyleSheet('border: 1px solid red')
                txt.setFocus()
                blank = True
                break
            else:
                txt.setStyleSheet('border: 1px solid #ABABAB')
                blank = False


        return blank

    def remote(self):
        txts = [self.txtHost, self.txtUsername, self.txtPassword]
        if self.blankCheck() == False:
            self.MainWindow.remote(host=txts[0].text(), user=txts[1].text(), password=txts[2].text())




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | REMOTE ROUTER"))
        self.txtUsername.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.btnCancel.setText(_translate("MainWindow", "CANCEL"))
        self.btnRemote.setText(_translate("MainWindow", "REMOTE"))
        self.ckShowPassword.setText(_translate("MainWindow", "Show Password"))
        self.txtHost.setPlaceholderText(_translate("MainWindow", "HOST/ IP ADDRESS"))
        self.label.setText(_translate("MainWindow", "REMOTE ROUTER"))

import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
