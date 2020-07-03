# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/MainWindow-user.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import resource_rc


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		self.router = MainWindow.send
		self.MainWindow = MainWindow
		# MainWindow.resize(1360, 712)
		# MainWindow.setMinimumSize(QtCore.QSize(1360, 712))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.top = QtWidgets.QWidget(self.centralwidget)
		self.top.setGeometry(QtCore.QRect(-10, 0, 1381, 51))
		# self.top.setStyleSheet("background-color: rgb(115, 210, 22);")
		self.top.setObjectName("top")
		self.LLogo = QtWidgets.QLabel(self.top)
		self.LLogo.setGeometry(QtCore.QRect(10, 0, 231, 51))
		self.LLogo.setStyleSheet("font: 75 20pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);")
		self.LLogo.setText("MIKHOTMAN")
		self.LLogo.setAlignment(QtCore.Qt.AlignCenter)
		self.LLogo.setObjectName("LLogo")
		self.layoutWidget = QtWidgets.QWidget(self.top)
		self.layoutWidget.setGeometry(QtCore.QRect(330, 0, 1041, 51))
		self.layoutWidget.setObjectName("layoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label_5 = QtWidgets.QLabel(self.layoutWidget)
		self.label_5.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"color: #000000;")
		self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_5.setObjectName("label_5")
		self.horizontalLayout.addWidget(self.label_5)
		self.LLoginAs = QtWidgets.QLabel(self.layoutWidget)
		self.LLoginAs.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"color: #000000;")
		# self.LLoginAs.setText("LLoginAs")
		self.LLoginAs.setObjectName("LLoginAs")
		self.horizontalLayout.addWidget(self.LLoginAs)
		self.label_6 = QtWidgets.QLabel(self.layoutWidget)
		self.label_6.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"color: #000000;")
		self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_6.setObjectName("label_6")
		self.horizontalLayout.addWidget(self.label_6)
		self.LRouterName = QtWidgets.QLabel(self.layoutWidget)
		self.LRouterName.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"color: #000000;")
		# self.LRouterName.setText("LRouterName")
		self.LRouterName.setObjectName("LRouterName_2")
		self.horizontalLayout.addWidget(self.LRouterName)
		self.sidebar = QtWidgets.QWidget(self.centralwidget)
		self.sidebar.setGeometry(QtCore.QRect(0, 50, 231, 631))
		# self.sidebar.setStyleSheet("background-color: rgb(78, 154, 6);")
		self.sidebar.setObjectName("sidebar")
		self.btnDashboard = QtWidgets.QPushButton(self.sidebar)
		self.btnDashboard.setGeometry(QtCore.QRect(0, 30, 231, 51))
		self.btnDashboard.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"text-align: left;")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/newPrefix/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.btnDashboard.setIcon(icon)
		self.btnDashboard.setIconSize(QtCore.QSize(25, 25))
		self.btnDashboard.setObjectName("btnDashboard")
		self.btnUser = QtWidgets.QPushButton(self.sidebar)
		self.btnUser.setGeometry(QtCore.QRect(0, 90, 231, 51))
		self.btnUser.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"text-align: left;")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/newPrefix/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.btnUser.setIcon(icon1)
		self.btnUser.setIconSize(QtCore.QSize(25, 25))
		self.btnUser.setObjectName("btnUser")
		self.btnUserProfile = QtWidgets.QPushButton(self.sidebar)
		self.btnUserProfile.setGeometry(QtCore.QRect(0, 150, 231, 51))
		self.btnUserProfile.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"text-align: left;")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/newPrefix/user profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.btnUserProfile.setIcon(icon2)
		self.btnUserProfile.setIconSize(QtCore.QSize(25, 25))
		self.btnUserProfile.setObjectName("btnUserProfile")
		self.btnSettings = QtWidgets.QPushButton(self.sidebar)
		self.btnSettings.setGeometry(QtCore.QRect(0, 270, 231, 51))
		self.btnSettings.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"text-align: left;")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(":/newPrefix/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.btnSettings.setIcon(icon3)
		self.btnSettings.setIconSize(QtCore.QSize(25, 25))
		self.btnSettings.setObjectName("btnSettings")
		self.btnLog = QtWidgets.QPushButton(self.sidebar)
		self.btnLog.setGeometry(QtCore.QRect(0, 330, 231, 51))
		self.btnLog.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"text-align: left;")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(":/newPrefix/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.btnLog.setIcon(icon4)
		self.btnLog.setIconSize(QtCore.QSize(25, 25))
		self.btnLog.setObjectName("btnLog")
		self.btnActiveUser = QtWidgets.QPushButton(self.sidebar)
		self.btnActiveUser.setGeometry(QtCore.QRect(0, 210, 231, 51))
		self.btnActiveUser.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"text-align: left;")
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(":/newPrefix/multiple-users-silhouette.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.btnActiveUser.setIcon(icon5)
		self.btnActiveUser.setIconSize(QtCore.QSize(25, 25))
		self.btnActiveUser.setObjectName("btnActiveUser")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(":/newPrefix/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.btnLog.setIcon(icon4)
		self.btnLog.setIconSize(QtCore.QSize(25, 25))
		self.btnLog.setObjectName("btnLog")
		self.contentview = QtWidgets.QWidget(self.centralwidget)
		self.contentview.setGeometry(QtCore.QRect(230, 50, 1141, 631))
		# self.contentview.setStyleSheet("background-color: rgb(186, 189, 182);")
		self.contentview.setObjectName("contentview")
		self.line = QtWidgets.QFrame(self.contentview)
		self.line.setGeometry(QtCore.QRect(40, 50, 1091, 31))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.LTitle = QtWidgets.QLabel(self.contentview)
		self.LTitle.setGeometry(QtCore.QRect(40, 30, 141, 21))
		self.LTitle.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"color: #000000;")
		self.LTitle.setObjectName("LTitle")
		self.btnAddUser = QtWidgets.QPushButton(self.contentview)
		self.btnAddUser.setGeometry(QtCore.QRect(40, 80, 121, 31))
		if MainWindow.RLEVEL == 'read':
			self.btnAddUser.setEnabled(False)
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(":/newPrefix/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.btnAddUser.setIcon(icon5)
		self.btnAddUser.setIconSize(QtCore.QSize(13, 13))
		self.btnAddUser.setObjectName("btnAddUser")
		self.cmbActionOnSelected = QtWidgets.QComboBox(self.contentview)
		if MainWindow.RLEVEL == 'read':
			self.cmbActionOnSelected.setEnabled(False)
		self.cmbActionOnSelected.setGeometry(QtCore.QRect(40, 130, 161, 31))
		self.cmbActionOnSelected.setObjectName("cmbActionOnSelected")
		self.cmbActionOnSelected.addItem("")
		self.cmbActionOnSelected.addItem("")
		self.cmbActionOnSelected.addItem("")
		self.cmbActionOnSelected.addItem("")
#         self.cmbActionOnSelected.setStyleSheet("color: #000;\n"
# "font: 75 10pt \"Arial Black\";")
		self.lcdAllUser = QtWidgets.QLCDNumber(self.contentview)
		self.lcdAllUser.setGeometry(QtCore.QRect(600, 100, 91, 31))
		self.lcdAllUser.setObjectName("lcdAllUser")
		self.lcdAllUser.display(len(self.router('/ip/hotspot/user/print')) - 1)
		self.lcdActiveUser = QtWidgets.QLCDNumber(self.contentview)
		self.lcdActiveUser.setGeometry(QtCore.QRect(770, 100, 91, 31))
		self.lcdActiveUser.setObjectName("lcdActiveUser")
		self.lcdActiveUser.display(len(self.router('/ip/hotspot/active/print')))
		self.label = QtWidgets.QLabel(self.contentview)
		self.label.setGeometry(QtCore.QRect(710, 110, 54, 17))
		self.label.setObjectName("label")
		self.label_3 = QtWidgets.QLabel(self.contentview)
		self.label_3.setGeometry(QtCore.QRect(880, 110, 91, 16))
		self.label_3.setObjectName("label_3")
		self.defineTable()



		self.cmbActionOnSelected.currentIndexChanged.connect(lambda: self.actionOnSelected(self.cmbActionOnSelected))

		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def defineTable(self):
		self.tableWidget = QtWidgets.QTableWidget(self.contentview)
		self.tableWidget.setGeometry(QtCore.QRect(40, 170, 1091, 451))
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setStyleSheet(f"background: {self.MainWindow.BGVIEW}")
		if self.MainWindow.RLEVEL != 'read':
			self.tableWidget.doubleClicked.connect(self.editUser)
		self.users = self.router('/ip/hotspot/user/print')
		self.tableWidget.setRowCount(len(self.users)-1)
		self.tableWidget.setColumnCount(5)
		header = self.tableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
		self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("#"))
		self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
		self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("User Profile"))
		self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Uptime"))
		self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Status"))
		self.tableWidget.verticalHeader().setVisible(False)
		self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
		self.tableWidget.itemClicked.connect(self.itemchecked)
		for row, user in enumerate(self.users):
			if 'profile' in user:
				self.tableWidget.setItem(row-1, 0, QTableWidgetItem(str(row)))
				self.tableWidget.setItem(row-1, 1, QTableWidgetItem(str(user['name'])))
				self.tableWidget.setItem(row-1, 2, QTableWidgetItem(str(user['profile'])))
				self.tableWidget.setItem(row-1, 3, QTableWidgetItem(str(user['uptime'])))
				self.tableWidget.setItem(row-1, 4, QTableWidgetItem("Disabled" if user['disabled'] == 'true' else "Active"))

	def editUser(self):
		# unselect all row
		for item in self.tableWidget.selectedItems():
			item.setSelected(False)

		row 	= self.tableWidget.currentItem().row()
		name 	= self.tableWidget.item(row, 1).text()
		users 	= self.router(f'/ip/hotspot/user/print\n\
			?name={name}')
		if users != None:
			if len(users):
				self.MainWindow.editHotspotUser(users[0])

	def itemchecked(self):
		items = []
		for item in (self.tableWidget.selectedItems()):
			getname = self.tableWidget.item(item.row(), 1).text()

			if getname not in items:
				items.append(getname)
		return items

	def actionOnSelected(self, cmb):
		items = self.itemchecked()
		# jika items belum ada yang terpilih
		if len(items) < 1 and cmb.currentIndex() != 0:
			# muncul pesan tolong pilih user
			QMessageBox.warning(self.centralwidget, f'Error' , f'Please Select user')
			cmb.setCurrentIndex(0)

		# jika sudah pilih user
		else:
			# cek apakah action sudah terpilih!
			# jika sudah
			if cmb.currentIndex() > 0:
				comm = None
				if cmb.currentText() == 'activate':
					activate = QMessageBox.question(self.centralwidget, 'Activate', f'are you sure to activate?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
					if activate == QMessageBox.Yes:
						for item in items:
							comm = f'/ip/hotspot/user/set\n=numbers={item}\n=disabled=no'
							self.router(comm)
						self.MainWindow.log.message(f'hotspot user {", ".join(items)} was Activate')
				elif cmb.currentText() == 'disable':
					disable = QMessageBox.question(self.centralwidget, 'Disable', f'are you sure to disable?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
					if disable == QMessageBox.Yes:
						pass
						for item in items:
							comm = f'/ip/hotspot/user/set\n=numbers={item}\n=disabled=yes'
							self.router(comm)
						self.MainWindow.log.message(f'hotspot user {", ".join(items)} was Disabled')
				else:
					delete = QMessageBox.question(self.centralwidget, 'delete', f'are you sure to delete?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
					if delete == QMessageBox.Yes:
						for item in items:
							comm = f'/ip/hotspot/user/remove\n=numbers={item}'
							self.router(comm)
						self.MainWindow.log.message(f'hotspot user {", ".join(items)} was deleted')
				self.MainWindow.user()

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | USER"))
		self.label_5.setText(_translate("MainWindow", "Login As : "))
		self.label_6.setText(_translate("MainWindow", "Router Name : "))
		self.btnDashboard.setText(_translate("MainWindow", "DASHBOARD"))
		self.btnUser.setText(_translate("MainWindow", "USER"))
		self.btnUserProfile.setText(_translate("MainWindow", "USER PROFILE"))
		self.btnActiveUser.setText(_translate("MainWindow", "ACTIVE USER"))
		self.btnSettings.setText(_translate("MainWindow", "SETTINGS"))
		self.btnLog.setText(_translate("MainWindow", "LOG"))
		self.LTitle.setText(_translate("MainWindow", "USER"))
		self.btnAddUser.setText(_translate("MainWindow", "Add User"))
		self.cmbActionOnSelected.setItemText(0, _translate("MainWindow", "Action on selected"))
		self.cmbActionOnSelected.setItemText(1, _translate("MainWindow", "activate"))
		self.cmbActionOnSelected.setItemText(2, _translate("MainWindow", "disable"))
		self.cmbActionOnSelected.setItemText(3, _translate("MainWindow", "delete"))
		self.label.setText(_translate("MainWindow", "All User"))
		self.label_3.setText(_translate("MainWindow", "Active User"))



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
