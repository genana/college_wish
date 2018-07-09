# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\srcdata\pyqt\college_wish\Select_MAJOR_CAT.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 170)
        Dialog.setMinimumSize(QtCore.QSize(410, 170))
        Dialog.setMaximumSize(QtCore.QSize(410, 170))
        Dialog.setModal(True)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout.addWidget(self.checkBox_1, 0, 1, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 1, 3, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 1, 2, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 2, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 3, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 2, 1, 1)
        self.checkBox_0 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_0.setObjectName("checkBox_0")
        self.gridLayout.addWidget(self.checkBox_0, 0, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 2, 1, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 2, 3, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 2, 2, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 1, 1, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(260, 130, 93, 28))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(60, 130, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择学科"))
        self.checkBox_4.setText(_translate("Dialog", "法学"))
        self.checkBox_1.setText(_translate("Dialog", "工学"))
        self.checkBox_7.setText(_translate("Dialog", "历史学"))
        self.checkBox_6.setText(_translate("Dialog", "文学"))
        self.checkBox_8.setText(_translate("Dialog", "农学"))
        self.checkBox_3.setText(_translate("Dialog", "经济学"))
        self.checkBox_2.setText(_translate("Dialog", "哲学"))
        self.checkBox_0.setText(_translate("Dialog", "理学"))
        self.checkBox_9.setText(_translate("Dialog", "医学"))
        self.checkBox_11.setText(_translate("Dialog", "艺术学"))
        self.checkBox_10.setText(_translate("Dialog", "管理学"))
        self.checkBox_5.setText(_translate("Dialog", "教育学"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
        self.pushButton_ok.setText(_translate("Dialog", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

