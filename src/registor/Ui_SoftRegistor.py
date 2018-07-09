# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\srcdata\pyqt\college_wish\SoftRegistor.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 222)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_mac = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_mac.setObjectName("label_mac")
        self.gridLayout.addWidget(self.label_mac, 0, 1, 1, 1)
        self.lineEdit_mac = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_mac.setEnabled(True)
        self.lineEdit_mac.setObjectName("lineEdit_mac")
        self.gridLayout.addWidget(self.lineEdit_mac, 0, 2, 1, 1)
        self.textBrowser_key = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_key.setObjectName("textBrowser_key")
        self.gridLayout.addWidget(self.textBrowser_key, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 170, 141, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "软件注册机"))
        self.label.setText(_translate("MainWindow", "激活码:"))
        self.label_mac.setText(_translate("MainWindow", "机器码:"))
        self.pushButton.setText(_translate("MainWindow", "生成激活码"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

