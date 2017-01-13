# -*- coding:utf-8 -*-

import sys
from PySide.QtCore import *
from PySide.QtGui import *


class SystemTrayMenu(QMenu):
	def __init__(self, *args, **kwargs):
		super(SystemTrayMenu, self).__init__(*args, **kwargs)
		self.addAction('quit').triggered.connect(self.quitApp)

	def quitApp(self):
		qApp.quit()


class AppSystemTray(QSystemTrayIcon):
	def __init__(self, *args, **kwargs):
		super(AppSystemTray, self).__init__(*args, **kwargs)
		self.setIcon(QIcon('app.ico'))
		self.setContextMenu(SystemTrayMenu())


class App(QApplication):
	def __init__(self, *args, **kwargs):
		super(App, self).__init__(*args, **kwargs)

	def winEventFilter(self, *args, **kwargs):
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)

	tray = AppSystemTray()
	tray.show()

	app.exec_()
