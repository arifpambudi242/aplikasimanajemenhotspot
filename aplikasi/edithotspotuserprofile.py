# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/edithotspotuserprofile.ui'
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
        MainWindow.setMaximumSize(504, 374)
        MainWindow.setMinimumSize(504, 374)
        MainWindow.setModal(True)
        MainWindow.setStyleSheet(f'background: {MainMenu.BGVIEW}')
        MainWindow.closeEvent = self.closeEvent
        self.txtName = QtWidgets.QLineEdit(MainWindow)
        self.txtName.setGeometry(QtCore.QRect(60, 90, 391, 41))
        self.txtName.setObjectName("txtName")
        self.txtName.returnPressed.connect(self.editUserProfile)
        self.txtRateLimit = QtWidgets.QLineEdit(MainWindow)
        self.txtRateLimit.setGeometry(QtCore.QRect(60, 210, 391, 41))
        self.txtRateLimit.setObjectName("txtRateLimit")
        self.txtRateLimit.returnPressed.connect(self.editUserProfile)
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
        self.btnCancel.setAutoDefault(False)
        self.btnCancel.clicked.connect(MainWindow.close)
        self.btnAdd = QtWidgets.QPushButton(MainWindow)
        self.btnAdd.setGeometry(QtCore.QRect(280, 290, 171, 41))
        self.btnAdd.setAutoDefault(False)
        self.btnAdd.clicked.connect(self.editUserProfile)
        self.txtSharedUsers = QtWidgets.QLineEdit(MainWindow)
        self.txtSharedUsers.setGeometry(QtCore.QRect(60, 150, 391, 41))
        self.txtSharedUsers.setObjectName("txtSharedUsers")
        self.txtSharedUsers.setValidator(QIntValidator(1, 999))
        self.txtSharedUsers.returnPressed.connect(self.editUserProfile)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtName, self.txtSharedUsers)
        MainWindow.setTabOrder(self.txtSharedUsers, self.txtRateLimit)
        MainWindow.setTabOrder(self.txtRateLimit, self.btnAdd)
        MainWindow.setTabOrder(self.btnAdd, self.btnCancel)

    def defineValue(self, profile):
        self.name   = profile['name']
        sharedUser  = profile['shared-users']
        rateLimit   = profile['rate-limit'] if 'rate-limit' in profile else ''

        self.txtName.setText(self.name)
        self.txtSharedUsers.setText(sharedUser)
        self.txtRateLimit.setText(rateLimit)

    def blankCheck(self):
        return True\
        if self.txtName.text() == ''\
        or self.txtSharedUsers.text() == ''\
        or self.txtRateLimit.text() == ''\
        else False

    def editUserProfile(self):
        if not self.blankCheck():
            name        = self.txtName.text()
            sharedUsers = self.txtSharedUsers.text()
            rateLimit   = self.txtRateLimit.text()

            try:
                self.router(f'/ip/hotspot/user/profile/set\n\
                    =numbers={self.name}\n\
                    =name={name}\n\
                    =shared-users={sharedUsers}\n\
                    =rate-limit={rateLimit}')
                self.MainMenu.log.message(f'hotspot user profile {self.name} was edited')
                QMessageBox.information(self.MainWindow, "Edited", f"{self.name} was edited")
                self.name = name
            except Exception as e:
                QMessageBox.warning(self.MainWindow, "Failed", f"{self.name} unable to edit\n cause {e}")

    def closeEvent(self, event):
        exit = QMessageBox.question(self.MainWindow, "Close", "Are you sure?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        event.ignore() if exit == QMessageBox.No else self.MainMenu.userProfile()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | EDIT HOTSPOT USER PROFILE"))
        self.txtName.setPlaceholderText(_translate("MainWindow", "NAME"))
        self.txtRateLimit.setPlaceholderText(_translate("MainWindow", "RATE LIMIT"))
        self.label.setText(_translate("MainWindow", "EDIT HOTSPOT USER PROFILE"))
        self.btnCancel.setText(_translate("MainWindow", "CANCEL"))
        self.btnAdd.setText(_translate("MainWindow", "EDIT"))
        self.txtSharedUsers.setPlaceholderText(_translate("MainWindow", "SHARED USERS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
