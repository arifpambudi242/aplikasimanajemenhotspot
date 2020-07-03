# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/MainWindow-settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import resource_rc
import time


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		self.themeChange = MainWindow.activeTheme()
		self.THEME = MainWindow.THEME
		self.MainWindow = MainWindow
		MainWindow.setObjectName("MainWindow")
		# MainWindow.resize(1360, 712)
		# MainWindow.setMinimumSize(QtCore.QSize(1360, 712))
		MainWindow.setStyleSheet("color: #000;")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.top = QtWidgets.QWidget(self.centralwidget)
		self.top.setGeometry(QtCore.QRect(-10, 0, 1381, 51))
		self.top.setStyleSheet(f"background-color: {MainWindow.BGTOP};")
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
		self.LLoginAs.setText("LLoginAs")
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
		self.LRouterName.setText("LRouterName")
		self.LRouterName.setObjectName("LRouterName")
		self.horizontalLayout.addWidget(self.LRouterName)
		self.sidebar = QtWidgets.QWidget(self.centralwidget)
		self.sidebar.setGeometry(QtCore.QRect(0, 50, 231, 631))
		self.sidebar.setStyleSheet(f"background-color: {MainWindow.BGSIDEBAR};")
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
		self.contentview = QtWidgets.QWidget(self.centralwidget)
		self.contentview.setGeometry(QtCore.QRect(230, 50, 1141, 631))
		self.contentview.setStyleSheet(f"background-color: {MainWindow.BGVIEW};")
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
		self.themeWidget = QtWidgets.QWidget(self.contentview)
		self.themeWidget.setGeometry(QtCore.QRect(40, 80, 1091, 271))
		self.themeWidget.setObjectName("widget")
		self.LTitle_2 = QtWidgets.QLabel(self.themeWidget)
		self.LTitle_2.setGeometry(QtCore.QRect(20, 20, 141, 21))
		self.LTitle_2.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"color: #000000;")
		self.LTitle_2.setObjectName("LTitle_2")
		self.rbtnBlue = QtWidgets.QRadioButton(self.themeWidget)
		self.rbtnBlue.setGeometry(QtCore.QRect(20, 80, 121, 23))
		self.rbtnBlue.setObjectName("rbtnBlue")
		self.rbtnBlue.toggled.connect(lambda: self.changeTheme(self.rbtnBlue, "blue"))
		self.rbtnDark = QtWidgets.QRadioButton(self.themeWidget)
		self.rbtnDark.setGeometry(QtCore.QRect(20, 110, 121, 23))
		self.rbtnDark.setObjectName("rbtnDark")
		self.rbtnDark.toggled.connect(lambda: self.changeTheme(self.rbtnDark, "dark"))
		# self.rbtnGrey = QtWidgets.QRadioButton(self.themeWidget)
		# self.rbtnGrey.setGeometry(QtCore.QRect(20, 140, 121, 23))
		# self.rbtnGrey.setObjectName("rbtnGrey")
		# self.rbtnGrey.toggled.connect(lambda: self.changeTheme(self.rbtnGrey, "grey"))
		self.rbtnMaroon = QtWidgets.QRadioButton(self.themeWidget)
		self.rbtnMaroon.setGeometry(QtCore.QRect(20, 140, 121, 23))
		self.rbtnMaroon.setObjectName("rbtnMaroon")
		self.rbtnMaroon.toggled.connect(lambda: self.changeTheme(self.rbtnMaroon, "maroon"))
		self.rbtnGreen = QtWidgets.QRadioButton(self.themeWidget)
		self.rbtnGreen.setGeometry(QtCore.QRect(20, 170, 121, 23))
		self.rbtnGreen.setObjectName("rbtnGreen")
		self.rbtnGreen.toggled.connect(lambda: self.changeTheme(self.rbtnGreen, "green"))
		self.btnApply = QtWidgets.QPushButton(self.themeWidget)
		self.btnApply.setGeometry(QtCore.QRect(230, 200, 88, 33))
		self.btnApply.setObjectName("btnApply")
		if MainWindow.LEVEL == 2:
			self.btnApply.setEnabled(False)
		else:
			self.btnApply.clicked.connect(lambda: self.applyThemeChange(MainWindow))
		self.prtop = QtWidgets.QWidget(self.themeWidget)
		self.prtop.setGeometry(QtCore.QRect(520, 40, 471, 21))
		# self.prtop.setStyleSheet("background-color: rgb(32, 74, 135);")
		self.prtop.setObjectName("prtop")
		self.prsidebar = QtWidgets.QWidget(self.themeWidget)
		self.prsidebar.setGeometry(QtCore.QRect(520, 60, 100, 171))
		# self.prsidebar.setStyleSheet("background-color: rgb(32, 74, 135);")
		self.prsidebar.setObjectName("prsidebar")
		self.prcontentview = QtWidgets.QWidget(self.themeWidget)
		self.prcontentview.setGeometry(QtCore.QRect(610, 60, 381, 171))
		# self.prcontentview.setStyleSheet(f"background-color: {MainWindow.BGVIEW};")
		self.prcontentview.setObjectName("prcontentview")
		self.userWidget = QtWidgets.QWidget(self.contentview)
		self.userWidget.setGeometry(QtCore.QRect(40, 360, 1091, 271))
		self.userWidget.setObjectName("widget_2")
		self.LTitle_3 = QtWidgets.QLabel(self.userWidget)
		self.LTitle_3.setGeometry(QtCore.QRect(20, 20, 141, 21))
		self.LTitle_3.setStyleSheet("font: 75 13pt \"Arial Black\";\n"
"color: #000000;")
		self.LTitle_3.setObjectName("LTitle_3")
		self.btnAddUser = QtWidgets.QPushButton(self.userWidget)
		self.btnAddUser.setGeometry(QtCore.QRect(20, 80, 121, 31))
		if MainWindow.LEVEL == 2:
			self.btnAddUser.setEnabled(False)
#         self.btnAddUser.setStyleSheet("font: 75 12pt \"Arial Black\";\n"
# "color: #000;\n"
# "text-align: left;")
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(":/newPrefix/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.btnAddUser.setIcon(icon5)
		self.btnAddUser.setIconSize(QtCore.QSize(13, 13))
		self.btnAddUser.setObjectName("btnAddUser")
		# self.btnAddUser.setStyleSheet("text-align: left;")
		self.tableWidget = QtWidgets.QTableWidget(self.userWidget)
		self.tableWidget.setGeometry(QtCore.QRect(240, 40, 831, 221))
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(4)
		users = MainWindow.db.select('users', select=['username', 'level', 'lastlogin'])
		header = self.tableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
		self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("#"))
		self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
		self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Level"))
		self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Last Login"))
		self.tableWidget.verticalHeader().setVisible(False)
		self.tableWidget.setRowCount(len(users))
		if MainWindow.LEVEL == 1:
			self.tableWidget.doubleClicked.connect(self.editUser)
		self.tableWidget.setRowCount(len(users))
		# add table items
		for row, user in enumerate(users):
			self.tableWidget.setItem(row, 0, QTableWidgetItem(str(row+1)))
			self.tableWidget.setItem(row, 1, QTableWidgetItem(user['username']))
			self.tableWidget.setItem(row, 2, QTableWidgetItem('Full' if int(user['level']) == 1 else 'Read'))
			tm = time.strftime('%d.%m.%Y, %H:%M', time.localtime(int(user['lastlogin'])))
			self.tableWidget.setItem(row, 3, QTableWidgetItem(str(tm)))

		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		MainWindow.setTabOrder(self.btnDashboard, self.btnUser)
		MainWindow.setTabOrder(self.btnUser, self.btnUserProfile)
		MainWindow.setTabOrder(self.btnUserProfile, self.btnSettings)
		MainWindow.setTabOrder(self.btnSettings, self.btnLog)

	def editUser(self):
		row 		= self.tableWidget.currentItem().row()
		username 	= self.tableWidget.item(row, 1).text()

		user = self.MainWindow.db.select('users', where={'username' : username})
		if len(user) > 0:
			self.MainWindow.editUser(user[0])


	def changeTheme(self, btn, activetheme ):
		if btn.isChecked() == True:
			self.themeChange = activetheme
			self.prtop.setStyleSheet(f"background: {self.THEME[activetheme]['BGTOP']};border: 1px solid #000;")
			self.prsidebar.setStyleSheet(f"background: {self.THEME[activetheme]['BGSIDEBAR']};border: 1px solid #000;")
			self.prcontentview.setStyleSheet(f"background: {self.THEME[activetheme]['BGVIEW']};border: 1px solid #000;")

	def applyThemeChange(self, MainWindow):
		if MainWindow.activeTheme != self.themeChange:
			restart = QMessageBox.question(MainWindow, "Apply", "Are you sure to apply theme changes?", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
			if restart == QMessageBox.Yes:
				with open("theme.tmhm", "w") as themewrite:
					themewrite.write(self.themeChange)
					themewrite.close()
				MainWindow.defineTheme(self.themeChange)
				MainWindow.settings()


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | SETTINGS"))
		self.label_5.setText(_translate("MainWindow", "Login As : "))
		self.label_6.setText(_translate("MainWindow", "Router Name : "))
		self.btnDashboard.setText(_translate("MainWindow", "DASHBOARD"))
		self.btnUser.setText(_translate("MainWindow", "USER"))
		self.btnUserProfile.setText(_translate("MainWindow", "USER PROFILE"))
		self.btnActiveUser.setText(_translate("MainWindow", "ACTIVE USER"))
		self.btnSettings.setText(_translate("MainWindow", "SETTINGS"))
		self.btnLog.setText(_translate("MainWindow", "LOG"))
		self.LTitle.setText(_translate("MainWindow", "SETTINGS"))
		self.LTitle_2.setText(_translate("MainWindow", "THEME"))
		self.rbtnBlue.setText(_translate("MainWindow", "Blue(Default)"))
		self.rbtnDark.setText(_translate("MainWindow", "Dark"))
		# self.rbtnGrey.setText(_translate("MainWindow", "Grey"))
		self.rbtnMaroon.setText(_translate("MainWindow", "Maroon"))
		self.rbtnGreen.setText(_translate("MainWindow", "Green"))
		self.btnApply.setText(_translate("MainWindow", "Apply"))
		self.LTitle_3.setText(_translate("MainWindow", "LOGIN USER"))
		self.btnAddUser.setText(_translate("MainWindow", "Add User"))





if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
