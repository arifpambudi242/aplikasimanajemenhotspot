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
from theme import THEME
import hashlib
from dbhandler import DbHandler
import time

class Ui_MainWindow(object):
	def setupUi(self, MainWindow, MainMenu):
		self.MainMenu = MainMenu
		self.save = False
		MainWindow.setObjectName("MainWindow")
		self.db = DbHandler('mhm.db')
		MainWindow.resize(483, 380)
		MainWindow.setMaximumSize(483, 380)
		MainWindow.setMinimumSize(483, 380)
		MainWindow.setModal(True)
		MainWindow.setStyleSheet(f"background: {THEME[open('theme.tmhm', 'r').read()]['BGVIEW']}")
		self.btnCancel = QtWidgets.QPushButton(MainWindow)
		self.btnCancel.setGeometry(QtCore.QRect(30, 310, 181, 41))
		self.btnCancel.setObjectName("btnCancel")
		self.btnCancel.setAutoDefault(False)
		self.btnCancel.clicked.connect(MainWindow.close)
		self.btnAdd = QtWidgets.QPushButton(MainWindow)
		self.btnAdd.setGeometry(QtCore.QRect(260, 310, 191, 41))
		self.btnAdd.setObjectName("btnAdd")
		self.btnAdd.setAutoDefault(False)
		self.btnAdd.clicked.connect(self.addUser)
		self.label = QtWidgets.QLabel(MainWindow)
		self.label.setGeometry(QtCore.QRect(-1, 50, 481, 28))
		self.label.setMinimumSize(QtCore.QSize(0, 0))
		self.label.setStyleSheet("font: 75 16pt \"Arial Black\";")
		self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label.setObjectName("label")
		self.cmbLevel = QtWidgets.QComboBox(MainWindow)
		self.cmbLevel.setGeometry(QtCore.QRect(30, 240, 421, 41))
		self.cmbLevel.setObjectName("cmbLevel")
		self.cmbLevel.addItem("")
		self.cmbLevel.addItem("")
		self.cmbLevel.addItem("")
		self.txtUsername = QtWidgets.QLineEdit(MainWindow)
		self.txtUsername.setGeometry(QtCore.QRect(30, 120, 421, 41))
		self.txtUsername.setMouseTracking(False)
		self.txtUsername.setEchoMode(QtWidgets.QLineEdit.Normal)
		self.txtUsername.setCursorPosition(0)
		self.txtUsername.setObjectName("txtUsername")
		self.txtUsername.setFocus()
		self.txtPassword = QtWidgets.QLineEdit(MainWindow)
		self.txtPassword.setGeometry(QtCore.QRect(30, 180, 421, 41))
		self.txtPassword.setMouseTracking(False)
		self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
		self.txtPassword.setCursorPosition(0)
		self.txtPassword.setObjectName("txtPassword")

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		MainWindow.closeEvent = self.closeEvent
		MainWindow.setTabOrder(self.txtUsername, self.txtPassword)
		MainWindow.setTabOrder(self.txtPassword, self.cmbLevel)
		MainWindow.setTabOrder(self.cmbLevel, self.btnAdd)
		MainWindow.setTabOrder(self.btnAdd, self.btnCancel)
		self.MainWindow = MainWindow

		self.defineTxtEvent()


	def defineTxtEvent(self):
		txts = [self.txtUsername, self.txtPassword]
		for txt in txts:
			txt.returnPressed.connect(self.addUser)

	def blankCheck(self):
		txts = [self.txtUsername, self.txtPassword]
		blanktxt = True
		blankcmb = True

		for txt in txts:
			if txt.text() == '':
				txt.setStyleSheet('border: 1px solid red')
				txt.setFocus()
				blanktxt = True
				break
			else:
				txt.setStyleSheet('border: 1px solid #ABABAB')
				blanktxt = False

		if self.cmbLevel.currentIndex() == 0:
			blankcmb = True
		else:
			blankcmb = False


		return blanktxt or blankcmb

	def resetForm(self):
		self.txtUsername.setText('')
		self.txtPassword.setText('')
		self.cmbLevel.setCurrentIndex(0)

	def addUser(self):
		self.save = True
		if self.blankCheck() == False:
			username    = self.txtUsername.text()
			password    = hashlib.sha256(self.txtPassword.text().encode('utf-8')).hexdigest()
			level       = self.cmbLevel.currentIndex()

			data = {
				'username'  : username,
				'password'  : password,
				'level'     : int(level),
				'lastlogin' : time.time()
			}

			if self.db.insert('users', data) > 0:
				self.MainMenu.log.message(f'user {username} was added')
				self.resetForm()
				QMessageBox.information(self.MainWindow, 'Success', 'User successfully saved!')
			else:
				QMessageBox.warning(self.MainWindow, 'Failed', 'Failed to save!')

	def closeEvent(self, event):
		if self.save == False:
			keluar = QMessageBox.question(self.MainWindow, "exit", "do you want to exit without save?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
		else:
			keluar = QMessageBox.question(self.MainWindow, "exit", "are you sure?",  QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

		if keluar == QMessageBox.No:
			event.ignore()
		else:
			self.MainMenu.settings()



	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | ADD USER"))
		self.btnCancel.setText(_translate("MainWindow", "CANCEL"))
		self.btnAdd.setText(_translate("MainWindow", "ADD"))
		self.label.setText(_translate("MainWindow", "ADD NEW USER"))
		self.cmbLevel.setItemText(0, _translate("MainWindow", "Choose Level"))
		self.cmbLevel.setItemText(1, _translate("MainWindow", "Full"))
		self.cmbLevel.setItemText(2, _translate("MainWindow", "Read"))
		self.txtUsername.setPlaceholderText(_translate("MainWindow", "USERNAME"))
		self.txtPassword.setPlaceholderText(_translate("MainWindow", "PASSWORD"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QDialog()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
