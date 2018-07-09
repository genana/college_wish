# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\srcdata\pyqt\college_wish\Help.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(631, 411)
        Dialog.setMaximumSize(QtCore.QSize(633, 411))
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "关于软件"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">软件简介：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    本软件是一款查询类软件，用于查询全国高校在<span style=\" font-weight:600;\">黑龙江省</span>的招生情况，包含全国近<span style=\" font-weight:600;\">2800</span>所高校，各录取批次(暂时不包含体育类和艺术类)共计<span style=\" font-weight:600;\">13</span>个学科，<span style=\" font-weight:600;\">61</span>个大学专业类，近<span style=\" font-weight:600;\">500</span>个大学专业的招生情况，可查询 &lt;<span style=\" font-weight:600;\">地区-学校-院校代码-学校类别-录取批次-考生类别-学校分数线-学科门类-专业-专业最低分-专业最低位次-专业最高分-专业最高位次-招生人数</span>&gt;<span style=\" font-weight:600;\"> </span>共计14个字段的信息(注意，招生人数字段为0，表示此条信息的该字段信息不详，并非表示招生人数确实为0)，还可以针对某一字段进行<span style=\" font-weight:600;\">模糊搜索</span>，<span style=\" font-weight:600;\">排序</span>等操作，有效辅助广大考生进行高考志愿选取工作。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14pt; font-weight:600; color:#333333; background-color:#ffffff;\">软件操作说明：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-size:11pt; font-weight:600;\">精确查询</span>：此操作根据用户设定的字段条件进行相关信息的精确查询，系统根据用户指定的条件字段，实现字段完全匹配查询。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-size:11pt; font-weight:600;\">模糊查询</span>：此操作根据用户设定的字段条件进行相关信息的模糊查询，系统根据用户指定的条件字段，实现字段部分匹配查询。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   <span style=\" font-size:10pt;\"> </span><span style=\" font-size:11pt; font-weight:600;\">清空条件</span>：此操作将用户之前设定的各字段条件清零，否则将在用户上一次查询所设定条件的基础上进行查询。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-size:11pt; font-weight:600;\">排序</span>：此操作根据查询结果的各字段内容进行排序(升序或降序)，点击表单栏对应字段的表头即可实现排序操作。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">开发者邮箱</span>：<span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12pt; font-style:italic; color:#333333;\">isfanhy@gmail.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

