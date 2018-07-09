# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\srcdata\pyqt\college_wish\Login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gui import ico_rc



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(319, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(301, 230))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/logo3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(297, 77))
        self.graphicsView.setMaximumSize(QtCore.QSize(297, 77))
        self.graphicsView.setStyleSheet("border-image: url(:/ico/logo1.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(7, 7, 7, 7)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setStyleSheet("font: 12pt \"黑体\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(50, 31))
        self.lineEdit_username.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_username)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setStyleSheet("font: 12pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_pw = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_pw.setMinimumSize(QtCore.QSize(50, 31))
        self.lineEdit_pw.setObjectName("lineEdit_pw")
        self.lineEdit_pw.setEchoMode(QtWidgets.QLineEdit.Password)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pw)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 27, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_register = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout.addWidget(self.pushButton_register)
        self.pushButton_login = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        spacerItem1 = QtWidgets.QSpacerItem(40, 27, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登陆系统"))
        self.label.setText(_translate("MainWindow", "用户名:"))
        self.lineEdit_username.setPlaceholderText(_translate("MainWindow", "请输入用户名"))
        self.label_2.setText(_translate("MainWindow", "密码:"))
        self.lineEdit_pw.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.pushButton_register.setText(_translate("MainWindow", "注册"))
        self.pushButton_login.setText(_translate("MainWindow", "登陆"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

