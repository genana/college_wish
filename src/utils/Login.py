# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import QMessageBox
from PyQt5 import  QtWidgets


import utils.SearchPage as SP
from gui.Ui_Login import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_register_clicked(self):
        """
        Slot documentation goes here.
        """
        print("on_pushButton_register_clicked")
        QMessageBox.warning(self,  "提示", ("尚未开通此功能"))
        
        
    
    @pyqtSlot()
    def on_pushButton_login_clicked(self):
        """
        Slot documentation goes here.
        """
        print("on_pushButton_login_clicked")
        username, pw = self.get_info()
        
        if 'admin'==username and 'root'==pw:
            self.close()
            self.ui = SP.MainWindow()
            self.ui.show()
            app.exec_()
        else:
            print("error")
            QMessageBox.warning(self,  "提示", ("请输入正确用户名或密码"))
        
        
    def get_info(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_pw.text()
        return username, password
        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


