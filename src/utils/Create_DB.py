# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

from utils.cipher_xls2db import *



from gui.Ui_Create_DB import Ui_Dialog
from PyQt5.Qt import QMessageBox, QFileDialog

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.xlsFile = ''
        self.db_path = ''
        
    
    # 选择xls文件
    @pyqtSlot()
    def on_pushButton_select_xls_clicked(self):
        """
        Slot documentation goes here.
        """
        print('on_pushButton_select_xls_clicked')
        self.xlsFile  = QFileDialog.getOpenFileName(self,  u"选取文件",  "./",  "Excel Files (*.xls;*.xlsx)")[0] 
        print(self.xlsFile)
        
        
    
    # 创建数据库
    @pyqtSlot()
    def on_pushButton_create_db_clicked(self):
        """
        Slot documentation goes here.
        """        
        # 先判断Excel文件是否已经指定
        if self.xlsFile=='':
            QMessageBox.warning(self,  u"提示", u"请先选择Excel文件")
            
        else:
            print(self.xlsFile)
            
            # 指定数据库存放位置
            db_path=QFileDialog.getExistingDirectory(self, u"请选择数据库存放位置", "./")  
            self.db_path = db_path
            print(self.db_path)
            
            # 调用接口生成数据库
            state = xls2db(self.xlsFile, self.db_path)
            
            if state:
                QMessageBox.information(self, u"提示", u"生成数据库成功！")
            else:
                QMessageBox.information(self, u"提示", u"生成数据库失败，请检查Excel文件！")
                
            

        
        
        
        
        
        
    
