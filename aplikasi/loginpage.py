# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import hashlib
import resource_rc
import sys
import time



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 379)
        MainWindow.setMinimumSize(QtCore.QSize(493, 379))
        MainWindow.setMaximumSize(QtCore.QSize(493, 379))
        MainWindow.showNormal()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Logo/logomikhotman.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(f"background: {MainWindow.BGVIEW};")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 220, 91))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("background-image: url(:/newPrefix/Logo/logomikhotman.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.txtUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsername.setGeometry(QtCore.QRect(40, 110, 421, 41))
        self.txtUsername.setMouseTracking(False)
        self.txtUsername.setObjectName("txtUsername")
        self.txtUsername.returnPressed.connect(lambda: self.login(MainWindow))
        self.txtUsername.textChanged.connect(lambda: self.blankCheck(self.txtUsername))
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(40, 180, 421, 41))
        self.txtPassword.setMouseTracking(False)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setCursorPosition(0)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.returnPressed.connect(lambda: self.login(MainWindow))
        self.txtPassword.textChanged.connect(lambda: self.blankCheck(self.txtPassword))
        self.cekShowPassword = QtWidgets.QCheckBox(self.centralwidget)
        self.cekShowPassword.setGeometry(QtCore.QRect(40, 230, 121, 23))
        self.cekShowPassword.setObjectName("cekShowPassword")
        self.cekShowPassword.toggled.connect(lambda: self.showPassword(self.cekShowPassword.isChecked()))
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(270, 270, 191, 41))
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(lambda: self.login(MainWindow))
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(40, 270, 181, 41))
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtUsername, self.txtPassword)
        MainWindow.setTabOrder(self.txtPassword, self.cekShowPassword)
        MainWindow.setTabOrder(self.cekShowPassword, self.btnLogin)
        MainWindow.setTabOrder(self.btnLogin, self.btnCancel)
        # MainWindow.closeEvent = self.closeEvent
        # self.dashboard = lambda: MainWindow.dashboard()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | LOGIN PAGE"))
        self.txtUsername.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.btnCancel.setText(_translate("MainWindow", "CANCEL"))
        self.btnLogin.setText(_translate("MainWindow", "LOGIN"))
        self.cekShowPassword.setText(_translate("MainWindow", "Show Password"))

    def showPassword(self, checked):
        if checked == True:
            self.txtPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.txtPassword.setEchoMode(QLineEdit.Password)


    def login(self, MainWindow):
        username = self.txtUsername.text()
        password = hashlib.sha256(self.txtPassword.text().encode('utf-8')).hexdigest()

        self.blankCheck(self.txtUsername)
        self.blankCheck(self.txtPassword)
        if self.txtUsername.text() == '':
            self.txtUsername.setFocus()
        elif self.txtPassword.text() == '':
            self.txtPassword.setFocus()
        else:
            user = MainWindow.db.select('users', where={'username' : username, 'password' : password})
            if len(user) > 0:
                MainWindow.USER = username
                MainWindow.LEVEL = user[0]['level']
                MainWindow.log.message(f'username {username} logged in to App')
                MainWindow.db.update('users', data={'lastlogin' : time.time()}, where={'username' : user[0]['username']})
                time.sleep(0.5)
                MainWindow.remoteRouter()
            else:
                MainWindow.log.message(f'Trying to login username : {username}')
                QMessageBox.warning(self.centralwidget, 'Wrong', 'Wrong Username or Password!')


    def blankCheck(self, txt):
        if txt.text() == '':
            txt.setStyleSheet('border: 1px solid red;')
        else:
            txt.setStyleSheet('border: 1px solid #ABABAB;')


    # def closeEvent(self, ev):
    #     exit = QMessageBox.question(self.centralwidget, 'Close', 'Are you sure?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
    #     if exit == QMessageBox.No:
    #         ev.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
