# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/MainWindow-log.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.MainWindow = MainWindow
        # MainWindow.resize(1360, 712)
        # MainWindow.setMinimumSize(QtCore.QSize(1360, 712))
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
        self.btnClearLog = QtWidgets.QPushButton(self.contentview)
        self.btnClearLog.setGeometry(QtCore.QRect(40, 70, 121, 31))
        if MainWindow.LEVEL == 2:
            self.btnClearLog.setEnabled(False)
        self.btnClearLog.setObjectName("btnClearLog")
        self.btnClearLog.clicked.connect(self.clearLog)
        with open('mikhotman.log', 'r') as log:
            self.logs = log.readlines()
        self.tblSystemLog = QtWidgets.QTableWidget(self.contentview)
        self.tblSystemLog.setGeometry(QtCore.QRect(40, 110, 1091, 521))
        self.tblSystemLog.setObjectName("tblSystemLog")
        self.tblSystemLog.setStyleSheet(f"background: {MainWindow.BGVIEW}")
        self.tblSystemLog.setColumnCount(2)
        self.tblSystemLog.setRowCount(len(self.logs))
        header = self.tblSystemLog.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tblSystemLog.setHorizontalHeaderItem(0, QTableWidgetItem("#"))
        self.tblSystemLog.setHorizontalHeaderItem(1, QTableWidgetItem("Log"))
        self.tblSystemLog.verticalHeader().setVisible(False)
        if self.logs:
            for row, log in enumerate(self.logs):
                self.tblSystemLog.setItem(row, 0, QTableWidgetItem(str(row + 1)))
                self.tblSystemLog.setItem(row, 1, QTableWidgetItem(log))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clearLog(self):
        clear = QMessageBox.question(self.MainWindow, 'Clear', f'Are you sure to clear Logs?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if clear == QMessageBox.Yes:
            with open('mikhotman.log', 'w') as log:
                log.write('')
            self.MainWindow.systemLog()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | SYSTEM LOG"))
        self.label_5.setText(_translate("MainWindow", "Login As : "))
        self.label_6.setText(_translate("MainWindow", "Router Name : "))
        self.btnDashboard.setText(_translate("MainWindow", "DASHBOARD"))
        self.btnUser.setText(_translate("MainWindow", "USER"))
        self.btnUserProfile.setText(_translate("MainWindow", "USER PROFILE"))
        self.btnActiveUser.setText(_translate("MainWindow", "ACTIVE USER"))
        self.btnSettings.setText(_translate("MainWindow", "SETTINGS"))
        self.btnLog.setText(_translate("MainWindow", "LOG"))
        self.btnClearLog.setText(_translate("MainWindow", "Clear Logs"))
        self.LTitle.setText(_translate("MainWindow", "SYSTEM LOG"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
