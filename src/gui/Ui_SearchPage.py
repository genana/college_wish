# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\srcdata\pyqt\college_wish\SearchPage.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QRegExp, QRegExpValidator
from gui import ico_rc



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 697)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/logo3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(11, 2, 11, 2)
        self.gridLayout.setSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(13, 44, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 75 14pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_6.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout_6.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_6.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setSpacing(7)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setMinimumSize(QtCore.QSize(50, 27))
        self.label_9.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_year = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        self.lineEdit_year.setMinimumSize(QtCore.QSize(99, 27))
        self.lineEdit_year.setStyleSheet("font: 11pt \"Arial\";")
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_year)
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setMinimumSize(QtCore.QSize(50, 27))
        self.label_11.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_sch = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_sch.sizePolicy().hasHeightForWidth())
        self.lineEdit_sch.setSizePolicy(sizePolicy)
        self.lineEdit_sch.setMinimumSize(QtCore.QSize(99, 27))
        self.lineEdit_sch.setStyleSheet("font: 11pt \"Arial\";")
        self.lineEdit_sch.setObjectName("lineEdit_sch")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sch)
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setMinimumSize(QtCore.QSize(50, 27))
        self.label_12.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_score = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_score.sizePolicy().hasHeightForWidth())
        self.lineEdit_score.setSizePolicy(sizePolicy)
        self.lineEdit_score.setMinimumSize(QtCore.QSize(99, 27))
        self.lineEdit_score.setStyleSheet("font: 11pt \"Arial\";")
        self.lineEdit_score.setInputMask("")
        self.lineEdit_score.setObjectName("lineEdit_score")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_score)
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setMinimumSize(QtCore.QSize(50, 27))
        self.label_13.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_rank = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_rank.sizePolicy().hasHeightForWidth())
        self.lineEdit_rank.setSizePolicy(sizePolicy)
        self.lineEdit_rank.setMinimumSize(QtCore.QSize(99, 27))
        self.lineEdit_rank.setStyleSheet("font: 11pt \"Arial\";")
        self.lineEdit_rank.setInputMask("")
        self.lineEdit_rank.setObjectName("lineEdit_rank")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_rank)
        self.gridLayout_2.addLayout(self.formLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_sch_level = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_sch_level.setStyleSheet("font: 75 11pt \"Arial\";")
        self.pushButton_sch_level.setObjectName("pushButton_sch_level")
        self.horizontalLayout_7.addWidget(self.pushButton_sch_level)
        self.pushButton_major_cat = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_major_cat.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_major_cat.setFont(font)
        self.pushButton_major_cat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_major_cat.setAutoFillBackground(False)
        self.pushButton_major_cat.setStyleSheet("font: 75 11pt \"Arial\";")
        self.pushButton_major_cat.setObjectName("pushButton_major_cat")
        self.horizontalLayout_7.addWidget(self.pushButton_major_cat)
        self.pushButton_major = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_major.setStyleSheet("font: 75 11pt \"Arial\";")
        self.pushButton_major.setObjectName("pushButton_major")
        self.horizontalLayout_7.addWidget(self.pushButton_major)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_14.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.comboBox_area = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_area.sizePolicy().hasHeightForWidth())
        self.comboBox_area.setSizePolicy(sizePolicy)
        self.comboBox_area.setMinimumSize(QtCore.QSize(99, 27))
        self.comboBox_area.setStyleSheet("font: 11pt \"Arial\";")
        self.comboBox_area.setObjectName("comboBox_area")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_area)
        self.comboBox_batch = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_batch.sizePolicy().hasHeightForWidth())
        self.comboBox_batch.setSizePolicy(sizePolicy)
        self.comboBox_batch.setStyleSheet("font: 11pt \"Arial\";")
        self.comboBox_batch.setObjectName("comboBox_batch")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_batch)
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.comboBox_st_cat = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_st_cat.sizePolicy().hasHeightForWidth())
        self.comboBox_st_cat.setSizePolicy(sizePolicy)
        self.comboBox_st_cat.setMinimumSize(QtCore.QSize(1, 0))
        self.comboBox_st_cat.setStyleSheet("font: 11pt \"Arial\";")
        self.comboBox_st_cat.setObjectName("comboBox_st_cat")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_st_cat)
        self.label_16 = QtWidgets.QLabel(self.centralWidget)
        self.label_16.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setMinimumSize(QtCore.QSize(99, 27))
        self.label.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_major = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_major.setMinimumSize(QtCore.QSize(99, 27))
        self.lineEdit_major.setObjectName("lineEdit_major")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_major)
        self.gridLayout_2.addLayout(self.formLayout, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_search = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        self.pushButton_search.setMinimumSize(QtCore.QSize(122, 33))
        self.pushButton_search.setMaximumSize(QtCore.QSize(16777215, 47))
        self.pushButton_search.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 14pt \"Arial\";")
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout_2.addWidget(self.pushButton_search)
        self.pushButton_search_fuzzy = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_search_fuzzy.sizePolicy().hasHeightForWidth())
        self.pushButton_search_fuzzy.setSizePolicy(sizePolicy)
        self.pushButton_search_fuzzy.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_search_fuzzy.setMaximumSize(QtCore.QSize(16777215, 47))
        self.pushButton_search_fuzzy.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 14pt \"Arial\";")
        self.pushButton_search_fuzzy.setObjectName("pushButton_search_fuzzy")
        self.verticalLayout_2.addWidget(self.pushButton_search_fuzzy)
        self.pushButton_clear_cdt = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clear_cdt.sizePolicy().hasHeightForWidth())
        self.pushButton_clear_cdt.setSizePolicy(sizePolicy)
        self.pushButton_clear_cdt.setMaximumSize(QtCore.QSize(16777215, 47))
        self.pushButton_clear_cdt.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: rgb(170, 255, 255);")
        self.pushButton_clear_cdt.setObjectName("pushButton_clear_cdt")
        self.verticalLayout_2.addWidget(self.pushButton_clear_cdt)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 44, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(232, 232))
        self.graphicsView.setMaximumSize(QtCore.QSize(232, 232))
        self.graphicsView.setStyleSheet("border-image: url(:/ico/logo2.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 3, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 997, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menuBar)
        self.action_createDB = QtWidgets.QAction(MainWindow)
        self.action_createDB.setObjectName("action_createDB")
        self.action_activate = QtWidgets.QAction(MainWindow)
        self.action_activate.setObjectName("action_activate")
        self.action_softactivate = QtWidgets.QAction(MainWindow)
        self.action_softactivate.setObjectName("action_softactivate")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_selectDB_2 = QtWidgets.QAction(MainWindow)
        self.action_selectDB_2.setEnabled(False)
        self.action_selectDB_2.setObjectName("action_selectDB_2")
        self.menu_2.addAction(self.action_createDB)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_selectDB_2)
        self.menu_3.addAction(self.action_softactivate)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_about)
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


# 自定义begin
        # 只能输入数字
        self.lineEdit_year.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        # 只能输入数字
        self.lineEdit_score.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        # 只能输入数字
        self.lineEdit_rank.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        
        
        BATCH = ( '提前批',  '本科一批',  '本科二批',  '专科')
        ST_CAT = ( '理科', '文科')
        
        
        self.comboBox_batch.addItems(BATCH)
        self.comboBox_batch.setCurrentIndex(1)
        
        self.comboBox_st_cat.addItems(ST_CAT)
        
        # 设置表头宽度
        self.tableWidget.setColumnWidth(0,60) #地区
        self.tableWidget.setColumnWidth(1,130) #学校
        self.tableWidget.setColumnWidth(6,45) #校线
        self.tableWidget.setColumnWidth(8,140) #专业
        self.tableWidget.setColumnWidth(9,55) #最低分
        self.tableWidget.setColumnWidth(11,55) #最高分
        
        
# 自定义end







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "高考数据查询系统"))
        self.label_3.setText(_translate("MainWindow", "已选条件:"))
        self.label_9.setText(_translate("MainWindow", "年份："))
        self.label_11.setText(_translate("MainWindow", "学校："))
        self.label_12.setText(_translate("MainWindow", "分数："))
        self.lineEdit_score.setPlaceholderText(_translate("MainWindow", "请输入整数"))
        self.label_13.setText(_translate("MainWindow", "位次："))
        self.lineEdit_rank.setPlaceholderText(_translate("MainWindow", "请输入整数"))
        self.pushButton_sch_level.setText(_translate("MainWindow", "学校类别"))
        self.pushButton_major_cat.setText(_translate("MainWindow", "学科"))
        self.pushButton_major.setText(_translate("MainWindow", "热门专业"))
        self.label_14.setText(_translate("MainWindow", "学校省份："))
        self.label_15.setText(_translate("MainWindow", "录取批次："))
        self.label_16.setText(_translate("MainWindow", "考生类别："))
        self.label.setText(_translate("MainWindow", "专业关键字："))
        self.pushButton_search.setText(_translate("MainWindow", "精确查询"))
        self.pushButton_search_fuzzy.setText(_translate("MainWindow", "模糊查询"))
        self.pushButton_clear_cdt.setText(_translate("MainWindow", "清空条件"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "地区"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "学校"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "院校代码"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "学校类别"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "批次"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "考生类别"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "校线"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "学科门类"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "专业"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "最低分"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "最低位次"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "最高分"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "最高位次"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "录取人数"))
        self.menu_2.setTitle(_translate("MainWindow", "选项"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.action_createDB.setText(_translate("MainWindow", "生成数据库"))
        self.action_activate.setText(_translate("MainWindow", "软件注册"))
        self.action_softactivate.setText(_translate("MainWindow", "软件激活"))
        self.action_about.setText(_translate("MainWindow", "关于软件"))
        self.action_selectDB_2.setText(_translate("MainWindow", "选择数据库"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
