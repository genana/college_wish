# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\srcdata\pyqt\college_wish\Create_DB.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(311, 172)
        Dialog.setModal(True)
        self.pushButton_select_xls = QtWidgets.QPushButton(Dialog)
        self.pushButton_select_xls.setGeometry(QtCore.QRect(20, 20, 121, 51))
        self.pushButton_select_xls.setObjectName("pushButton_select_xls")
        self.pushButton_create_db = QtWidgets.QPushButton(Dialog)
        self.pushButton_create_db.setGeometry(QtCore.QRect(150, 20, 121, 51))
        self.pushButton_create_db.setObjectName("pushButton_create_db")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "生成数据库"))
        self.pushButton_select_xls.setText(_translate("Dialog", "请选择xls文件"))
        self.pushButton_create_db.setText(_translate("Dialog", "生成数据库"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

