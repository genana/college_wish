# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

from gui.Ui_Select_SCH_LEVEL import Ui_Dialog


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
        
        # 注意：.0取决于Excel源文件的单元格格式
        self.paras=['985','211','双一流','其它']
        self.states=[]
        
    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        for i in range(len(self.paras)):
             m=getattr(self,"checkBox_%d"%i)
             if m.isChecked():
                self.states.append(self.paras[i] )        
        self.close()
        
    # 重设CheckStates
    def reset_check(self):
        for i in range(len(self.paras)):
             m=getattr(self,"checkBox_%d"%i)
             m.setCheckState(0) 
    
    @pyqtSlot()
    def on_pushButton_cancel_clicked(self):
        """
        Slot documentation goes here.
        """
        self.close()
