# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from gui.Ui_soft_activate import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QMessageBox

from utils import set_config
import uuid


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, src_file=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        
        self.src_file = src_file
        
        self.MAC = uuid.UUID(int = uuid.getnode()).hex[-12:] 
        self.lineEdit_mac.setText(self.MAC)
        self.IV, self.KEY = set_config.get_IV_key()        
        
        self.ENCRY = set_config.encode('ncKZwpx0woLClw==', self.MAC+"X84W-Q8KC-JWP8-6F7R")
        # wqHCk8KAwozDmsOSw5pow5nCqH97w4TCr3HClMKbwrTCg8KlwrrCncOCwofDh8KneXnCssKuwo8=
      
      
      
      
    @pyqtSlot()
    def on_pushButton_softactivate_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print('on_pushButton_softactivate_clicked')
        
        codes = self.textEdit.toPlainText()
        print(codes)
        if codes=='':
            QMessageBox.warning(self,  "提示", "请输入激活码！")
        
        if codes==self.ENCRY:
            set_config.set_item(self.src_file, "PID", codes, self.KEY, self.IV)
            QMessageBox.warning(self,  "提示", "激活成功！重启软件后生效！")

            self.close()
        else:
            QMessageBox.warning(self,  "提示", "激活失败！")
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Dialog()
    ui.show()
    sys.exit(app.exec_())


