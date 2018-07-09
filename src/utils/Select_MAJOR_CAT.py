# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot


from gui.Ui_Select_MAJOR_CAT import Ui_Dialog

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
        self.states=[]
        self.paras=['理学','工学','哲学','经济学', 
                          '法学','教育学','文学','历史学', 
                          '农学','医学','管理学','艺术学', ]
        

        
  
    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        for i in range(len(self.paras)):
             m=getattr(self,"checkBox_%d"%i)
             if m.isChecked():
                print("checkBox_%d"%i)
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
