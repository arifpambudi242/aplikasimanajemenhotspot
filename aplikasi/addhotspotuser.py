# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/addhotspotuser.ui'
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
        self.MainWindow = MainWindow
        self.MainMenu = MainMenu
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 374)
        MainWindow.setMinimumSize(504, 374)
        MainWindow.setMaximumSize(504, 374)
        MainWindow.setModal(True)
        MainWindow.setStyleSheet(f"background: {MainMenu.BGVIEW}")
        self.txtName = QtWidgets.QLineEdit(MainWindow)
        self.txtName.setGeometry(QtCore.QRect(60, 90, 391, 41))
        self.txtName.setObjectName("txtName")
        self.txtName.returnPressed.connect(self.addUser)
        self.txtPassword = QtWidgets.QLineEdit(MainWindow)
        self.txtPassword.setGeometry(QtCore.QRect(60, 210, 391, 41))
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.returnPressed.connect(self.addUser)
        self.cmbChooseUserProfile = QtWidgets.QComboBox(MainWindow)
        self.cmbChooseUserProfile.setGeometry(QtCore.QRect(60, 150, 391, 41))
        self.cmbChooseUserProfile.setObjectName("cmbChooseUserProfile")
        self.cmbChooseUserProfile.addItem("")
        self.profile = self.router('/ip/hotspot/user/profile/print')
        for x in range(len(self.profile)):
            self.cmbChooseUserProfile.addItem("")
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
        self.btnAdd = QtWidgets.QPushButton(MainWindow)
        self.btnAdd.setGeometry(QtCore.QRect(280, 290, 171, 41))
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.setAutoDefault(False)
        self.btnAdd.clicked.connect(self.addUser)
        self.ckShowPassword = QtWidgets.QCheckBox(MainWindow)
        self.ckShowPassword.setGeometry(QtCore.QRect(60, 260, 131, 23))
        self.ckShowPassword.setObjectName("ckShowPassword")
        self.ckShowPassword.toggled.connect(lambda: self.showPassword(self.ckShowPassword))

        MainWindow.closeEvent = self.closeEvent

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtName, self.cmbChooseUserProfile)
        MainWindow.setTabOrder(self.cmbChooseUserProfile, self.txtPassword)
        MainWindow.setTabOrder(self.txtPassword, self.ckShowPassword)
        MainWindow.setTabOrder(self.ckShowPassword, self.btnAdd)
        MainWindow.setTabOrder(self.btnAdd, self.btnCancel)

    def showPassword(self, state):
        if state.isChecked() == True:
            self.txtPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.txtPassword.setEchoMode(QLineEdit.Password)

    def blankCheck(self):
        if self.txtName.text() == '' or self.txtPassword.text() == '' or self.cmbChooseUserProfile.currentIndex() == 0:
            return True
        else:
            return False

    def resetForm(self):
        self.txtName.setText('')
        self.txtPassword.setText('')
        self.cmbChooseUserProfile.setCurrentIndex(0)
        self.txtName.setFocus()

    def addUser(self):
        if not self.blankCheck():
            name        = self.txtName.text()
            password    = self.txtPassword.text()
            profile     = self.cmbChooseUserProfile.currentText()

            try:
                self.router(f'\
                    /ip/hotspot/user/add\n\
                    =name={name}\n\
                    =password={password}\n\
                    =profile={profile}')
                QMessageBox.information(self.MainWindow, "Success", f"User name = {name}\nprofile = {profile} added")
                self.MainMenu.log.message(f'added hotspot user {name}')
                self.resetForm()
            except Exception as e:
                QMessageBox.warning(self.MainWindow, "Failed", f"Add router Failed! cause : {e}")
        else:
            QMessageBox.warning(self.MainWindow, "Blank", "Blank is not allowed!")


    def closeEvent(self, event):
        if self.blankCheck() == False:
            exit = QMessageBox.question(self.MainWindow, "Exit", "Are you sure exit without Saving?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        else:
            exit = QMessageBox.question(self.MainWindow, "Exit", "Are you sure?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

        if exit == QMessageBox.No:
            event.ignore()
        else:
            self.MainMenu.user()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | ADD HOTSPOT USER"))
        self.txtName.setPlaceholderText(_translate("MainWindow", "NAME"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.cmbChooseUserProfile.setItemText(0, _translate("MainWindow", "Choose User Profile"))
        if len(self.profile) > 0:
            for i, p in enumerate(self.profile):
                self.cmbChooseUserProfile.setItemText(i+1, _translate("MainWindow", p['name']))
        self.label.setText(_translate("MainWindow", "ADD NEW HOTSPOT USER"))
        self.btnCancel.setText(_translate("MainWindow", "CANCEL"))
        self.btnAdd.setText(_translate("MainWindow", "ADD"))
        self.ckShowPassword.setText(_translate("MainWindow", "Show Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
