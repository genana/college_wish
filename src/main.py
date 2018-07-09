#coding=utf-8

from utils import SearchPage

import sys
from PyQt5 import QtWidgets


app = QtWidgets.QApplication(sys.argv)
ui = SearchPage.MainWindow()
ui.show()
sys.exit(app.exec_())











