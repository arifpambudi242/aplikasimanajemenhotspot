# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/edituser.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import hashlib
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, MainMenu):
        self.MainWindow = MainWindow
        self.MainMenu = MainMenu
        MainWindow.closeEvent = self.closeEvent
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(483, 379)
        MainWindow.setMaximumSize(483, 379)
        MainWindow.setMinimumSize(483, 379)
        MainWindow.setModal(True)
        MainWindow.setStyleSheet(f'background: {MainMenu.BGVIEW}')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Logo/logomikhotman.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(-1, 20, 481, 28))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("font: 75 16pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.txtUsername = QtWidgets.QLineEdit(MainWindow)
        self.txtUsername.setGeometry(QtCore.QRect(30, 90, 421, 41))
        self.txtUsername.setMouseTracking(False)
        self.txtUsername.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtUsername.setCursorPosition(0)
        self.txtUsername.setObjectName("txtUsername")
        self.txtUsername.returnPressed.connect(self.editUser)
        self.btnDelete = QtWidgets.QPushButton(MainWindow)
        self.btnDelete.setGeometry(QtCore.QRect(30, 280, 181, 41))
        self.btnDelete.setObjectName("btnDelete")
        self.btnDelete.setAutoDefault(False)
        self.btnDelete.setStyleSheet('background: red;')
        self.btnDelete.clicked.connect(self.deleteUser)
        self.btnEdit = QtWidgets.QPushButton(MainWindow)
        self.btnEdit.setGeometry(QtCore.QRect(260, 280, 191, 41))
        self.btnEdit.setObjectName("btnEdit")
        self.btnEdit.setAutoDefault(False)
        self.btnEdit.setStyleSheet('background: blue;')
        self.btnEdit.clicked.connect(self.editUser)
        self.txtPassword = QtWidgets.QLineEdit(MainWindow)
        self.txtPassword.setGeometry(QtCore.QRect(30, 150, 421, 41))
        self.txtPassword.setMouseTracking(False)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setCursorPosition(0)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.returnPressed.connect(self.editUser)
        self.cmbLevel = QtWidgets.QComboBox(MainWindow)
        self.cmbLevel.setGeometry(QtCore.QRect(30, 210, 421, 41))
        self.cmbLevel.setObjectName("cmbLevel")
        self.cmbLevel.addItem("")
        self.cmbLevel.addItem("")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtUsername, self.txtPassword)
        MainWindow.setTabOrder(self.txtPassword, self.cmbLevel)
        MainWindow.setTabOrder(self.cmbLevel, self.btnEdit)
        MainWindow.setTabOrder(self.btnEdit, self.btnDelete)

    def defineValue(self, user):
        self.id = user['id']
        self.name = user['username']
        self.txtUsername.setText(user['username'])
        if user['level'] == 1:
            self.cmbLevel.setCurrentIndex(0)
        else:
            self.cmbLevel.setCurrentIndex(1)

    def blankCheck(self):
        return True if self.txtUsername.text() == '' or self.txtPassword.text() == '' else False

    def deleteUser(self):
        if not len(self.MainMenu.db.select('users')) == 1:
            try:
                self.MainMenu.db.delete('users', where={'id' : self.id})
                self.MainMenu.log.message(f'user {self.name} was deleted')
                QMessageBox.information(self.MainWindow, "Success", "User successfully deleted")
                self.MainMenu.settings()
                self.MainWindow.close()
            except Exception as e:
                QMessageBox.warning(self.MainWindow, "Failed", f"Unable to delete\n {e}")
        else:
            QMessageBox.warning(self.MainWindow, "Failed", f"Unable to delete")


    def editUser(self):
        if not self.blankCheck():
            username    = self.txtUsername.text()
            password    = hashlib.sha256(self.txtPassword.text().encode('utf-8')).hexdigest()
            level       = self.cmbLevel.currentIndex() + 1

            try:
                data = {
                    'username'  : username,
                    'password'  : password,
                    'level'     : level,
                }

                self.MainMenu.db.update('users', data=data, where={'id' : self.id})
                self.MainMenu.log.message(f'user {self.name} was edited')
                QMessageBox.information(self.MainWindow, "Success", "User successfully Edited")
                self.MainMenu.settings()
                self.MainWindow.close()
            except Exception as e:
                QMessageBox.warning(self.MainWindow, "Failed", f"Unable to Edit {e}")
        else:
            QMessageBox.warning(self.MainWindow, "Failed", "Please fill the blank stuff!")



    def closeEvent(self, event):
        self.MainMenu.settings()
        event.accept()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | USER ACTION"))
        self.label.setText(_translate("MainWindow", "USER ACTION"))
        self.txtUsername.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.btnDelete.setText(_translate("MainWindow", "DELETE"))
        self.btnEdit.setText(_translate("MainWindow", "EDIT"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.cmbLevel.setItemText(0, _translate("MainWindow", "Full"))
        self.cmbLevel.setItemText(1, _translate("MainWindow", "Read"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
