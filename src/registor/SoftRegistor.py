# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.Qt import QMessageBox



from registor.Ui_SoftRegistor import Ui_MainWindow 
from registor.logger import logger


from registor import set_config


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
        self.MAC = ''
        
        
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            self.MAC = self.lineEdit_mac.text()
            if self.MAC=='':
                QMessageBox.warning(self,  "提示", "请输入机器码！")
            else:
                ENCRY = set_config.encode('ncKZwpx0woLClw==', self.MAC+"X84W-Q8KC-JWP8-6F7R")        
                self.textBrowser_key.setText(ENCRY)
            
        except:
            logger().exception('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    



