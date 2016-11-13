# -*- coding:utf-8 -*-

import sys
from PySide.QtCore import *
from PySide.QtGui import *


class SystemTrayMenu(QMenu):
    def __init__(self):
        super(SystemTrayMenu, self).__init__()
        self.addAction('quit').triggered.connect(self.quitApp)

    def quitApp(self):
        qApp.quit()


class AppSystemTray(QSystemTrayIcon):
    def __init__(self, *args, **kwargs):
        super(AppSystemTray, self).__init__(*args, **kwargs)
        self.setIcon(QIcon('icon.ico'))
        self.setContextMenu(SystemTrayMenu())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    tray = AppSystemTray()
    tray.show()

    app.exec_()

