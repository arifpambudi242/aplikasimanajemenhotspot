# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../laporan/Rancangan/ui/MainWindow-userprofile.ui'
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
        self.router = MainWindow.send
        MainWindow.setObjectName("MainWindow")
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
        self.LRouterName.setObjectName("LRouterName")
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
        # self.contentview.setStyleSheet("background-color: #3d3d3d;")
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
        self.btnAddUserProfile = QtWidgets.QPushButton(self.contentview)
        self.btnAddUserProfile.setGeometry(QtCore.QRect(40, 80, 171, 31))
        self.btnAddUserProfile.clicked.connect(MainWindow.addHotspotUserProfile)
#         self.btnAddUserProfile.setStyleSheet("font: 75 12pt \"Arial Black\";\n"
# "color: #000;\n"
# "text-align: left;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnAddUserProfile.setIcon(icon5)
        self.btnAddUserProfile.setIconSize(QtCore.QSize(13, 13))
        self.btnAddUserProfile.setObjectName("btnAddUserProfile")
        if MainWindow.RLEVEL == 'read':
            self.btnAddUserProfile.setEnabled(False)
        self.cmbActionOnSelected = QtWidgets.QComboBox(self.contentview)
        self.cmbActionOnSelected.setGeometry(QtCore.QRect(40, 140, 181, 31))
#         self.cmbActionOnSelected.setStyleSheet("color: #000;\n"
# "font: 75 10pt \"Arial Black\";\n"
# "text-align: right;")
        self.cmbActionOnSelected.setObjectName("cmbActionOnSelected")
        if MainWindow.RLEVEL == 'read':
            self.cmbActionOnSelected.setEnabled(False)
        self.cmbActionOnSelected.addItem("")
        self.cmbActionOnSelected.addItem("")
        self.profiles = MainWindow.send('/ip/hotspot/user/profile/print')
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.defineTable()
        self.cmbActionOnSelected.currentIndexChanged.connect(lambda: self.actionOnSelected(self.cmbActionOnSelected))

    def defineTable(self):
        self.tblUserProfile = QtWidgets.QTableWidget(self.contentview)
        self.tblUserProfile.setGeometry(QtCore.QRect(40, 190, 1081, 461))
        self.tblUserProfile.setObjectName("tblUserProfile")
        self.tblUserProfile.setStyleSheet(f'background: {self.MainWindow.BGVIEW}')
        self.tblUserProfile.setColumnCount(4)
        if self.MainWindow.RLEVEL == 'full':
            self.tblUserProfile.doubleClicked.connect(self.editProfile)
        self.tblUserProfile.setRowCount(len(self.profiles))
        header = self.tblUserProfile.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        # hide vertical header
        self.tblUserProfile.verticalHeader().setVisible(False)
        # set table multiselection
        self.tblUserProfile.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tblUserProfile.setHorizontalHeaderItem(0, QTableWidgetItem("#"))
        self.tblUserProfile.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.tblUserProfile.setHorizontalHeaderItem(2, QTableWidgetItem("Shared Users"))
        self.tblUserProfile.setHorizontalHeaderItem(3, QTableWidgetItem("Rate Limit"))
        for i, profile in enumerate(self.profiles):
            self.tblUserProfile.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.tblUserProfile.setItem(i, 1, QTableWidgetItem(profile['name']))
            if 'shared-users' in profile:
                self.tblUserProfile.setItem(i, 2, QTableWidgetItem(profile['shared-users']))
            else:
                self.tblUserProfile.setItem(i, 2, QTableWidgetItem("-"))
            self.tblUserProfile.setItem(i, 3, QTableWidgetItem(profile['rate-limit'] if 'rate-limit' in profile else '-'))

    def editProfile(self):
        # unselect all row
        for item in self.tblUserProfile.selectedItems():
            item.setSelected(False)

        row         = self.tblUserProfile.currentItem().row()
        name        = self.tblUserProfile.item(row, 1).text()
        profiles    = self.router(f'/ip/hotspot/user/profile/print\n\
            ?name={name}')
        if profiles != None:
            if len(profiles):
                self.MainWindow.editHotspotUserProfile(profiles[0])

    def itemchecked(self):
        items = []
        for item in (self.tblUserProfile.selectedItems()):
            getname = self.tblUserProfile.item(item.row(), 1).text()
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
                delete = QMessageBox.question(self.centralwidget, 'delete', f'are you sure to delete?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
                if delete == QMessageBox.Yes:
                    for item in items:
                        comm = f'/ip/hotspot/user/profile/remove\n=numbers={item}'
                        self.router(comm)
                    self.MainWindow.log.message(f'hotspot user profile {", ".join(items)} was deleted')
                self.MainWindow.userProfile()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIKHOTMAN | USER PROFILE"))
        self.label_5.setText(_translate("MainWindow", "Login As : "))
        self.label_6.setText(_translate("MainWindow", "Router Name : "))
        self.btnDashboard.setText(_translate("MainWindow", "DASHBOARD"))
        self.btnUser.setText(_translate("MainWindow", "USER"))
        self.btnUserProfile.setText(_translate("MainWindow", "USER PROFILE"))
        self.btnActiveUser.setText(_translate("MainWindow", "ACTIVE USER"))
        self.btnSettings.setText(_translate("MainWindow", "SETTINGS"))
        self.btnLog.setText(_translate("MainWindow", "LOG"))
        self.LTitle.setText(_translate("MainWindow", "USER PROFILE"))
        self.btnAddUserProfile.setText(_translate("MainWindow", "Add User Profile"))
        self.cmbActionOnSelected.setItemText(0, _translate("MainWindow", "Action on Selected"))
        self.cmbActionOnSelected.setItemText(1, _translate("MainWindow", "delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
