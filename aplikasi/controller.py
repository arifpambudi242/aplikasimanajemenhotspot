
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from loginpage import Ui_MainWindow as Login
from adduser import Ui_MainWindow as AddUser
from edituser import Ui_MainWindow as EditUser
from remoterouter import Ui_MainWindow as RemoteRouter
from mainMenuDashboard import Ui_MainWindow as Dashboard
from mainMenuUser import Ui_MainWindow as User
from addhotspotuser import Ui_MainWindow as AddHotspotUser
from edithotspotuser import Ui_MainWindow as EditHotspotUser
from mainMenuUserProfile import Ui_MainWindow as UserProfile
from addhotspotuserprofile import Ui_MainWindow as AddHotspotUserProfile
from edithotspotuserprofile import Ui_MainWindow as EditHotspotUserProfile
from mainmenuactiveuser import Ui_MainWindow as ActiveUser
from mainMenuSettings import Ui_MainWindow as Settings
from mainMenuLog import Ui_MainWindow as Log
from theme import THEME
from routeros_api import Api
from time import sleep
from dbhandler import DbHandler
from log import log


def run():
    app = QApplication(sys.argv)
    app.setApplicationName('MIKHOTMAN')
    controller = Controller()
    controller.show()
    sys.exit(app.exec())


class Controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.THEME      = THEME
        self.HOST       = None
        self.USER       = None
        self.RUSER      = None
        self.TUSER      = None
        self.ARSITECTURE= None
        self.VERSION    = None
        self.LLEVEL     = None
        self.TACTIVEUSER= None
        self.LEVEL      = 1
        self.RLEVEL     = None
        self.PASSWORD   = None
        self.ROUTERNAME = None
        self.router     = None
        self.db         = DbHandler('mhm.db')
        self.log        = log
        self.defineTheme()
        # pintas

        # self.remote('192.168.43.25', 'wr', 'wr')
        # sleep(1)
        # self.activeUser()

        if len(self.db.select('users')) > 0:
            self.login()
        else:
            self.login()
            self.addUser()

    def remote(self, host, user, password):
        self.HOST   = host
        self.RUSER  = user
        try:
            self.router = Api(host, user=user,password=password)
            if not self.checkConnection():
                QMessageBox.warning(self, "Invalid Connection", f"Invalid Connection to Router \nhost : {host}\nuser : {user}\nplease try again or edit if you made a mistake to host, user or password!")
                self.log.message(f'trying to remote router by host {host} username {user}')
                self.remoteRouter()
            else:
                self.defineRouterAttribute()
                self.log.message(f'Connected to router by host {host} username {user}')
                self.dashboard()
        except Exception as e:
                QMessageBox.warning(self, "Invalid Connection", f"Invalid Connection to Router \nhost : {host}\nuser : {user}\nplease try again or edit if you made a mistake to host, user or password!")

    def checkConnection(self):
        if self.router != None:
            if not self.router.is_alive():
                QMessageBox.warning(self, "Invalid Connection", f"Router Disconnected!")
                self.remoteRouter()
                return False
            else:
                return True
        else:
            return False

    def send(self, command):
        if self.checkConnection():
            try:
                return self.router.talk(command)
            except Exception as e:
                print(e)

    def defineRouterAttribute(self):
        try:
            resource = self.send('/system/resource/print')[0]
            self.ROUTERNAME = self.send('/system/identity/print')[0]['name']
            self.ARSITECTURE= resource['architecture-name']
            self.VERSION    = resource['version']
            self.LLEVEL     = self.send('/system/license/print')[0]['nlevel']
            self.RLEVEL     = self.send(f'/user/print\n?name={self.RUSER}')[0]['group']
            self.TUSER      = str(len(self.send('/ip/hotspot/user/print')) - 1)
            self.TACTIVEUSER= str(len(self.send('/ip/hotspot/active/print')))

        except Exception as e:
            print(f'Error = {e}')


    def activeTheme(self):
        with open("theme.tmhm", "r") as theme:
            return theme.read().strip()

    def defineTheme(self, active=None):
        self.theme          = self.THEME[self.activeTheme() if active == None else active]
        self.BGTOP          = self.theme['BGTOP']
        self.BGSIDEBAR      = self.theme['BGSIDEBAR']
        self.BGVIEW         = self.theme['BGVIEW']

    def login(self):
        self.setGeometry(450, 150, 0, 0)
        self.showNormal()
        self.Login = Login()
        self.Login.setupUi(self)

    def remoteRouter(self):
        self.setGeometry(450, 150, 0, 0)
        self.showNormal()
        self.RemoteRouter = RemoteRouter()
        self.RemoteRouter.setupUi(self)

    def addUser(self):
        self.Dialog = QDialog()
        self.AddUser = AddUser()
        self.AddUser.setupUi(self.Dialog, self)
        self.Dialog.show()

    def editUser(self, user):
        self.Dialog = QDialog()
        self.EditUser = EditUser()
        self.EditUser.setupUi(self.Dialog, self)
        self.EditUser.defineValue(user)
        self.Dialog.show()

    def dashboard(self):
        if self.checkConnection():
            # self.setGeometry(0, 0, 0, 0)
            self.resize(1360, 712)
            self.setMinimumSize(QSize(1340, 712))
            self.setMaximumSize(QSize(1666667, 1666667))
            self.Dashboard = Dashboard()
            self.Dashboard.setupUi(self)
            self.Dashboard.top.setStyleSheet(f'background: {self.BGTOP};')
            self.Dashboard.sidebar.setStyleSheet(f'background: {self.BGSIDEBAR};')
            self.Dashboard.contentview.setStyleSheet(f'background: {self.BGVIEW};')
            self.Dashboard.btnDashboard.clicked.connect(self.dashboard)
            self.Dashboard.btnUser.clicked.connect(self.user)
            self.Dashboard.btnUserProfile.clicked.connect(self.userProfile)
            self.Dashboard.btnActiveUser.clicked.connect(self.activeUser)
            self.Dashboard.btnSettings.clicked.connect(self.settings)
            self.Dashboard.btnLog.clicked.connect(self.systemLog)

    def user(self):
        if self.checkConnection():
            # self.setGeometry(0, 0, 0, 0)
            self.resize(1360, 712)
            self.setMinimumSize(QSize(1340, 712))
            self.setMaximumSize(QSize(1666667, 1666667))
            self.User = User()
            self.User.setupUi(self)
            self.User.LLoginAs.setText(self.RUSER)
            self.User.LRouterName.setText(self.ROUTERNAME)
            self.User.top.setStyleSheet(f'background: {self.BGTOP};')
            self.User.sidebar.setStyleSheet(f'background: {self.BGSIDEBAR};')
            self.User.contentview.setStyleSheet(f'background: {self.BGVIEW};')
            self.User.btnDashboard.clicked.connect(self.dashboard)
            self.User.btnUser.clicked.connect(self.user)
            self.User.btnUserProfile.clicked.connect(self.userProfile)
            self.User.btnActiveUser.clicked.connect(self.activeUser)
            self.User.btnSettings.clicked.connect(self.settings)
            self.User.btnLog.clicked.connect(self.systemLog)
            self.User.btnAddUser.clicked.connect(self.addHotspotUser)

    def addHotspotUser(self):
        if self.checkConnection():
            self.Dialog = QDialog()
            self.AddHotspotUser = AddHotspotUser()
            self.AddHotspotUser.setupUi(self.Dialog, self)
            self.Dialog.show()

    def editHotspotUser(self, user):
        if self.checkConnection():
            self.Dialog = QDialog()# ^-------------------------
            self.EditHotspotUser = EditHotspotUser() #        |
            self.EditHotspotUser.setupUi(self.Dialog, self) # |
            self.EditHotspotUser.defineValue(user)# <----------
            self.Dialog.show()


    def userProfile(self):
        if self.checkConnection():
            # self.setGeometry(0, 0, 0, 0)
            self.resize(1360, 712)
            self.setMinimumSize(QSize(1340, 712))
            self.setMaximumSize(QSize(1666667, 1666667))
            self.UserProfile = UserProfile()
            self.UserProfile.setupUi(self)
            self.UserProfile.LLoginAs.setText(self.RUSER)
            self.UserProfile.LRouterName.setText(self.ROUTERNAME)
            self.UserProfile.top.setStyleSheet(f'background: {self.BGTOP};')
            self.UserProfile.sidebar.setStyleSheet(f'background: {self.BGSIDEBAR};')
            self.UserProfile.contentview.setStyleSheet(f'background: {self.BGVIEW};')
            self.UserProfile.btnDashboard.clicked.connect(self.dashboard)
            self.UserProfile.btnUser.clicked.connect(self.user)
            self.UserProfile.btnUserProfile.clicked.connect(self.userProfile)
            self.UserProfile.btnActiveUser.clicked.connect(self.activeUser)
            self.UserProfile.btnSettings.clicked.connect(self.settings)
            self.UserProfile.btnLog.clicked.connect(self.systemLog)

    def addHotspotUserProfile(self):
        if self.checkConnection():
            self.Dialog = QDialog()
            self.AddHotspotUserProfile = AddHotspotUserProfile()
            self.AddHotspotUserProfile.setupUi(self.Dialog, self)
            self.Dialog.show()

    def editHotspotUserProfile(self, profile):
        if self.checkConnection():
            self.Dialog = QDialog()
            self.EditHotspotUserProfile = EditHotspotUserProfile()
            self.EditHotspotUserProfile.setupUi(self.Dialog, self)
            self.EditHotspotUserProfile.defineValue(profile)
            self.Dialog.show()

    def activeUser(self):
        if self.checkConnection():
            # self.setGeometry(0, 0, 0, 0)
            self.resize(1360, 712)
            self.setMinimumSize(QSize(1340, 712))
            self.setMaximumSize(QSize(1666667, 1666667))
            self.ActiveUser = ActiveUser()
            self.ActiveUser.setupUi(self)
            self.ActiveUser.LLoginAs.setText(self.RUSER)
            self.ActiveUser.LRouterName.setText(self.ROUTERNAME)
            self.ActiveUser.top.setStyleSheet(f'background: {self.BGTOP};')
            self.ActiveUser.sidebar.setStyleSheet(f'background: {self.BGSIDEBAR};')
            self.ActiveUser.contentview.setStyleSheet(f'background: {self.BGVIEW};')
            self.ActiveUser.btnDashboard.clicked.connect(self.dashboard)
            self.ActiveUser.btnUser.clicked.connect(self.user)
            self.ActiveUser.btnUserProfile.clicked.connect(self.userProfile)
            self.ActiveUser.btnActiveUser.clicked.connect(self.activeUser)
            self.ActiveUser.btnSettings.clicked.connect(self.settings)
            self.ActiveUser.btnLog.clicked.connect(self.systemLog)


    def settings(self):
        # self.setGeometry(0, 0, 0, 0)
        self.resize(1360, 712)
        self.setMinimumSize(QSize(1340, 712))
        self.setMaximumSize(QSize(1666667, 1666667))
        self.Settings = Settings()
        self.Settings.setupUi(self)
        if self.activeTheme() == 'blue':
            self.Settings.rbtnBlue.setChecked(True)
        elif self.activeTheme() == 'dark':
            self.Settings.rbtnDark.setChecked(True)
        elif self.activeTheme() == 'maroon':
            self.Settings.rbtnMaroon.setChecked(True)
        elif self.activeTheme() == 'green':
            self.Settings.rbtnGreen.setChecked(True)


        self.Settings.LLoginAs.setText(self.RUSER)
        self.Settings.LRouterName.setText(self.ROUTERNAME)
        self.Settings.top.setStyleSheet(f'background: {self.BGTOP};')
        self.Settings.sidebar.setStyleSheet(f'background: {self.BGSIDEBAR};')
        self.Settings.contentview.setStyleSheet(f'background: {self.BGVIEW};')
        self.Settings.btnDashboard.clicked.connect(self.dashboard)
        self.Settings.btnUser.clicked.connect(self.user)
        self.Settings.btnUserProfile.clicked.connect(self.userProfile)
        self.Settings.btnActiveUser.clicked.connect(self.activeUser)
        self.Settings.btnSettings.clicked.connect(self.settings)
        self.Settings.btnLog.clicked.connect(self.systemLog)
        self.Settings.btnAddUser.clicked.connect(lambda: self.addUser())

    def systemLog(self):
        # self.setGeometry(0, 0, 0, 0)
        self.resize(1360, 712)
        self.setMinimumSize(QSize(1340, 712))
        self.setMaximumSize(QSize(1666667, 1666667))
        self.Log = Log()
        self.Log.setupUi(self)
        self.Log.LLoginAs.setText(self.RUSER)
        self.Log.LRouterName.setText(self.ROUTERNAME)
        self.Log.top.setStyleSheet(f'background: {self.BGTOP};')
        self.Log.sidebar.setStyleSheet(f'background: {self.BGSIDEBAR};')
        self.Log.contentview.setStyleSheet(f'background: {self.BGVIEW};')
        self.Log.btnDashboard.clicked.connect(self.dashboard)
        self.Log.btnUser.clicked.connect(self.user)
        self.Log.btnUserProfile.clicked.connect(self.userProfile)
        self.Log.btnActiveUser.clicked.connect(self.activeUser)
        self.Log.btnSettings.clicked.connect(self.settings)
        self.Log.btnLog.clicked.connect(self.systemLog)

    def closeEvent(self, event):
        exit = QMessageBox.question(self, 'Close', 'Are you sure?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if exit == QMessageBox.No:
            event.ignore()




if __name__ == '__main__':
    run()