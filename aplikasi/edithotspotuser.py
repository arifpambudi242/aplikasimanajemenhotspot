# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/edithotspotuser.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, MainMenu):
        self.router = MainMenu.send
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 374)
        MainWindow.setMaximumSize(504, 374)
        MainWindow.setMinimumSize(504, 374)
        MainWindow.setModal(True)
        MainWindow.setStyleSheet(f'background: {MainMenu.BGVIEW}')
        MainWindow.closeEvent = self.closeEvent
        self.MainWindow = MainWindow
        self.MainMenu = MainMenu
        self.txtName = QtWidgets.QLineEdit(MainWindow)
        self.txtName.setGeometry(QtCore.QRect(60, 90, 391, 41))
        self.txtName.setObjectName("txtName")
        self.txtName.setFocus()
        self.txtName.returnPressed.connect(self.editUser)
        self.txtPassword = QtWidgets.QLineEdit(MainWindow)
        self.txtPassword.setGeometry(QtCore.QRect(60, 210, 391, 41))
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.returnPressed.connect(self.editUser)
        self.cmbChooseUserProfile = QtWidgets.QComboBox(MainWindow)
        self.cmbChooseUserProfile.setGeometry(QtCore.QRect(60, 150, 391, 41))
        self.cmbChooseUserProfile.setObjectName("cmbChooseUserProfile")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(3, 30, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnCancel = QtWidgets.QPushButton(MainWindow)
        self.btnCancel.setGeometry(QtCore.QRect(60, 290, 171, 41))
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.setAutoDefault(False)
        self.btnCancel.clicked.connect(MainWindow.close)
        self.btnEdit = QtWidgets.QPushButton(MainWindow)
        self.btnEdit.setGeometry(QtCore.QRect(280, 290, 171, 41))
        self.btnEdit.setObjectName("btnEdit")
        self.btnEdit.setAutoDefault(False)
        self.btnEdit.clicked.connect(self.editUser)
        self.ckShowPassword = QtWidgets.QCheckBox(MainWindow)
        self.ckShowPassword.setGeometry(QtCore.QRect(60, 260, 131, 23))
        self.ckShowPassword.setObjectName("ckShowPassword")
        self.ckShowPassword.toggled.connect(lambda: self.showPassword(self.ckShowPassword))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtName, self.cmbChooseUserProfile)
        MainWindow.setTabOrder(self.cmbChooseUserProfile, self.txtPassword)
        MainWindow.setTabOrder(self.txtPassword, self.ckShowPassword)
        MainWindow.setTabOrder(self.ckShowPassword, self.btnEdit)
        MainWindow.setTabOrder(self.btnEdit, self.btnCancel)

    def showPassword(self, state):
        if state.isChecked() == True:
            self.txtPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.txtPassword.setEchoMode(QLineEdit.Password)

    def defineValue(self, user):
        self.name = user['name']
        self.profiles = self.router('/ip/hotspot/user/profile/print')
        self.txtName.setText(user['name'])
        self.txtPassword.setText(user['password'])
        for i in range(len(self.profiles)):
            self.cmbChooseUserProfile.addItem("")
        for i, p in enumerate(self.profiles):
            self.cmbChooseUserProfile.setItemText(i, p['name'])
            if p['name'] == user['profile']:
                self.cmbChooseUserProfile.setCurrentIndex(i)

    def blankCheck(self):
        if self.txtName.text() == '' or self.txtPassword.text() == '':
            return True
        else:
            return False

    def editUser(self):
        if not self.blankCheck():
            edit = QMessageBox.question(self.MainWindow, "Edit", "Are you sure?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
            if edit == QMessageBox.Yes:
                name        = self.txtName.text()
                password    = self.txtPassword.text()
                profile     = self.cmbChooseUserProfile.currentText()

                try:
                    self.router(f'/ip/hotspot/user/set\n\
                        =numbers={self.name}\n\
                        =name={name}\n\
                        =profile={profile}\n\
                        =password={password}')
                    self.MainMenu.log.message(f'hotspot user {self.name} was edited')
                    QMessageBox.information(self.MainWindow, "Success", f"{self.name} was Edited")
                    self.name = name
                except Exception as e:
                    QMessageBox.warning(self.MainWindow, "Failed", f"Unable to edit{self.name} cause{e}")
        else:
            QMessageBox.warning(self.MainWindow, "Failed", f"Blank is not Allowed")



    def closeEvent(self, event):
        exit = QMessageBox.question(self.MainWindow, "exit", "Are you sure?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

        if exit == QMessageBox.No:
            event.ignore()
        else:
            self.MainMenu.user()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | EDIT HOTSPOT USER"))
        self.txtName.setPlaceholderText(_translate("MainWindow", "NAME"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.label.setText(_translate("MainWindow", "EDIT HOTSPOT USER"))
        self.btnCancel.setText(_translate("MainWindow", "CANCEL"))
        self.btnEdit.setText(_translate("MainWindow", "EDIT"))
        self.ckShowPassword.setText(_translate("MainWindow", "Show Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
