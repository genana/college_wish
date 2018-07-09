# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\srcdata\pyqt\college_wish\soft_activate.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(288, 192)
        Dialog.setMinimumSize(QtCore.QSize(288, 192))
        Dialog.setMaximumSize(QtCore.QSize(290, 199))
        Dialog.setSizeGripEnabled(True)
        self.pushButton_softactivate = QtWidgets.QPushButton(Dialog)
        self.pushButton_softactivate.setEnabled(True)
        self.pushButton_softactivate.setGeometry(QtCore.QRect(130, 150, 141, 31))
        self.pushButton_softactivate.setObjectName("pushButton_softactivate")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 133))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.lineEdit_mac = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_mac.setEnabled(True)
        self.lineEdit_mac.setObjectName("lineEdit_mac")
        self.gridLayout.addWidget(self.lineEdit_mac, 0, 2, 1, 1)
        self.label_mac = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_mac.setObjectName("label_mac")
        self.gridLayout.addWidget(self.label_mac, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "软件激活"))
        self.pushButton_softactivate.setText(_translate("Dialog", "激活"))
        self.label.setText(_translate("Dialog", "激活码:"))
        self.label_mac.setText(_translate("Dialog", "机器码:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

