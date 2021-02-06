import sys

from PyQt5 import QtCore, QtWidgets, QtGui, uic
from qasync import QEventLoop, asyncSlot
from hosts import Hosts

class Config:
    name: str = "shit"
    ip: str = "192.168.0.175"
    mirror: str = "192.168.0.175" # unused
    hosts: Hosts = None

    def __init__(self):
        self.hosts = Hosts.fromFile(self.ip, self.mirror)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("res/qt.ui", self)

        
        self.__get_shit__()
        self.__init__style__()
        self.__update_buttons__()

        # binding
        self.btnConnect.clicked.connect(self.connectButtonClicked)

    def connectButtonClicked(self, *args):
        if not self.config.hosts.is_connected:
            self.config.hosts.connect()
        else:
            self.config.hosts.disconnect()


        self.__update_buttons__()


        
    def __init__style__(self):
        # title
        self.setWindowTitle(f"Server switcher for {self.config.name}")

        # bg
        self.setStyleSheet(
            """
            background-image: url(res/img/uragirarete.png);
            background-repeat: no-repeat;
            background-position: center;
            """
            )

        # ip input thing
        self.ipInput.setText(f"<p align='center'>{self.config.ip}</p>")

        
    def __update_buttons__(self):
        # update button styling and shit
        self.btnConnect.setText(f'Switch to {self.connect_to}')

        # i tried to use css[state] stuff for cleaner code but it doesnt work
        # so yea use this instead...
        self.btnConnect.setStyleSheet(
            f"""
            color: #fff;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            margin: 10px 0 3px;
            padding: 10px 20px;
            background-color: {'#29b;' if not self.config.hosts.is_connected else '#b17;'}
            """)
        


    @property
    def connect_to(self):
        return self.config.name if not self.config.hosts.is_connected else "Bancho"


    def __get_shit__(self):
        self.ipInput = self.findChild(QtWidgets.QTextEdit, 'inputIp')
        self.btnConnect = self.findChild(QtWidgets.QPushButton, 'btnConnect')
        self.btnInstall = self.findChild(QtWidgets.QPushButton, 'btnInstall')

        self.config = Config()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    tiddies = Main()
    tiddies.show()

    sys.exit(app.exec_())
