# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import *
from PyQt5 import QtWidgets

import os

from utils import Select_SCH_LEVEL, logger
from utils import Select_MAJOR_CAT
from utils import soft_activate
from utils import Select_MAJOR
from utils import Create_DB
from utils import soft_activate
from utils import Help
from utils import set_config
from utils.cipher_query_db import query_db 
from gui.Ui_SearchPage import Ui_MainWindow


import uuid


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        try:
            QMainWindow.__init__(self, parent)
            
            # 启动验证times和PID
            IV, key = set_config.get_IV_key()
            
            self.src_file = os.path.expanduser('~')+'/.QtsConfigs'
            
            if not os.path.isfile(self.src_file):
                set_config.init_config(self.src_file)
                
            self.pId = set_config.get_item(self.src_file,"PID", key, IV)
            MAC = uuid.UUID(int = uuid.getnode()).hex[-12:] 
            ENCRY = set_config.encode('ncKZwpx0woLClw==', MAC+"X84W-Q8KC-JWP8-6F7R")
            
            print(self.pId)
            if self.pId!= ENCRY:
                print("试用版")
                self.times = int(set_config.get_item(self.src_file,"TIMES", key, IV))
                self.times += 1
                
                self.setupUi(self)
                
                AREA = ('河南', '福建');
                self.comboBox_area.addItems(AREA)
                
                self.major=[]
                self.major_cat=[]
                self.sch_level=[]
                self.DbPath = './database/'
                
                max_times=5
                if self.times>max_times:
                    # 设置button state
                    self.pushButton_search.setEnabled(False)
                    self.pushButton_search_fuzzy.setEnabled(False)
                    
                    QMessageBox.warning(self,  "提示", "您已达到最大试用次数，请激活软件后继续使用(菜单栏-帮助-软件激活-输入激活码)。")
                else:
                    QMessageBox.warning(self,  "提示", "您现在使用的是试用版本，最大试用次数{0}次，本次为第{1}次。试用版仅可查询<河南，福建>地区的数据，激活软件后可解除所有限制！".format(max_times, self.times))
                    set_config.set_item(self.src_file, "TIMES", str(self.times), key, IV)
            else:
                print("激活版")
                self.setupUi(self)
                self.action_softactivate.setEnabled(False)
                
                AREA = ('所有', '北京', '上海', '天津', '重庆 ', 
                '黑龙江', '吉林',
                 '辽宁', '江苏', '山东', '安徽', '河北', '河南',
                 '湖北', '湖南', '江西', '陕西', '山西', '四川',
                 '青海', '海南', '广东', '贵州', '浙江', '福建',
                 '甘肃', '云南', '内蒙古', '宁夏', '新疆', '西藏', '广西');
                self.comboBox_area.addItems(AREA)
                self.comboBox_area.setCurrentIndex(1)
                
                
                
                self.major=[]
                self.major_cat=[]
                self.sch_level=[]
                self.DbPath = './database/'
                        
            
        except:
            logger.logger().exception('')
        
    
    # 指定数据库目录
    @pyqtSlot()
    def on_action_selectDB_triggered(self):
        """
        Slot documentation goes here.
        """
        try:
            print('on_action_selectDB_triggered')
            # 指定数据库存放位置
            DbPath=QFileDialog.getExistingDirectory(self, u"请选择数据库所在目录", "./")  
            self.DbPath = DbPath
            print(self.DbPath)
        except:
            logger.logger().exception('')
            
            
        
    # 激活软件
    @pyqtSlot()
    def on_action_softactivate_triggered(self):
        """
        Slot documentation goes here.
        """
        try:
            print('action_softactivate')
            dialog = soft_activate.Dialog(self, self.src_file)
            dialog.show()      
            if dialog.exec_()==0:
                print('on_action_softactivate_triggered: finish!')
        except:
            logger.logger().exception('')
    
    # 关于软件
    @pyqtSlot()
    def on_action_about_triggered(self):
        """
        Slot documentation goes here.
        """
        try:
            print('action_about')
            dialog = Help.Dialog(self)
            dialog.show()      
            if dialog.exec_()==0:
                print('action_about: finish!')
        except:
            logger.logger().exception('')
    
    
      
        
    # 创建数据库
    @pyqtSlot()
    def on_action_createDB_triggered(self):
        """
        Slot documentation goes here.
        """
        try:
            print('on_action_createDB_triggered')        
            dialog = Create_DB.Dialog(self)
            dialog.show()      
            if dialog.exec_()==0:
                print('finish!')
        except:
            logger.logger().exception('')
        
        
        
    # 选择学科类别
    @pyqtSlot()
    def on_pushButton_major_cat_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            print('on_pushButton_major_cat_clicked')
            dialog = Select_MAJOR_CAT.Dialog(self)
            dialog.show()      
            if dialog.exec_()==0:
                self.major_cat = dialog.states
        except:
            logger.logger().exception('')



    # 指定学校等级
    @pyqtSlot()
    def on_pushButton_sch_level_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            print('on_pushButton_sch_level_clicked')
            dialog = Select_SCH_LEVEL.Dialog(self)
            dialog.show()        
            if dialog.exec_()==0:
                self.sch_level = dialog.states
        except:
            logger.logger().exception('')
        
        
        
    # 按钮：选择专业
    @pyqtSlot()
    def on_pushButton_major_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            print("on_pushButton_major_clicked")
            dialog = Select_MAJOR.Dialog(self)
            dialog.show()      
            if dialog.exec_()==0:
                self.major = dialog.states
        except:
            logger.logger().exception('')
        
        
    # 清空条件   
    @pyqtSlot()
    def on_pushButton_clear_cdt_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            print("on_pushButton_clear_cdt_clicked")
            self.comboBox_area.setCurrentIndex(1)
            self.comboBox_batch.setCurrentIndex(1)
            self.comboBox_st_cat.setCurrentIndex(0)
            self.lineEdit_sch.setText("")
            self.lineEdit_score.setText('')
            self.lineEdit_rank.setText('')
            
            dialog1 = Select_MAJOR_CAT.Dialog(self)
            dialog1.reset_check()
            
            dialog2 = Select_SCH_LEVEL.Dialog(self)
            dialog2.reset_check()
            
            dialog3 = Select_MAJOR.Dialog(self)
            dialog3.reset_check()
            
            self.major=[]
            self.major_cat=[]
            self.sch_level=[]
            
            self.textBrowser.setText("")
            
            # 年份先不清理
    #         self.lineEdit_year.setText("")
            self.tableWidget.clearContents()
            
        except:
            logger.logger().exception('')
        
        
        
    # 模糊搜索按钮，条件查询记录
    @pyqtSlot()
    def on_pushButton_search_fuzzy_clicked(self):
        """
        Slot documentation goes here.
        """                
        try:
            print('on_pushButton_search_fuzzy_clicked')
            
            if self.DbPath=='':
                QMessageBox.warning(self,  "提示", "请先选择数据库")
            else:
                year, area, cond_dict = self.get_info()
                if year=='':
                    QMessageBox.warning(self,  "提示", "请先输入年份")
                else:    
                    db_file = self.DbPath+'/'+year+'.db' 
                    if os.path.exists(db_file):
                        print("exist!")
                        
                        fuzzy_str = 'like'
                        res_list = query_db(db_file, area, cond_dict, fuzzy_str)
                        if len(res_list)==0:
                            QMessageBox.warning(self,  "提示", ("未查到符合条件的数据"))
                        self.tableWidget.setSortingEnabled(False)
                        self.insert_table(res_list)
                        self.write_textBrowser(cond_dict)
                    else:                
                        QMessageBox.warning(self,  "提示", ("未查到"+year+"年的数据"))
        except:
            logger.logger().exception('')

    
        
    # 搜索按钮，条件查询记录
    @pyqtSlot()
    def on_pushButton_search_clicked(self):
        """
        Slot documentation goes here.
        """                
        try:
            print('on_pushButton_search_clicked')
    
            if self.DbPath=='':
                QMessageBox.warning(self,  "提示", "请先选择数据库")
            else:
                year, area, cond_dict = self.get_info() 
                if year=='':
                    QMessageBox.warning(self,  "提示", "请先输入年份")
                else:    
                    db_file = self.DbPath+'/'+year+'.db' 
                    if os.path.exists(db_file):
                        print("exist!")
                        exact_str = 'is'
                        res_list = query_db(db_file, area, cond_dict, exact_str)
                        if len(res_list)==0:
                            QMessageBox.warning(self,  "提示", ("未查到符合条件的数据"))
                        self.tableWidget.setSortingEnabled(False)
                        self.insert_table(res_list)
                        self.write_textBrowser(cond_dict)
                    else:                
                        QMessageBox.warning(self,  "提示", ("未查到"+year+"年的数据"))
        except:
            logger.logger().exception('')
    
    
    # 打印当前条件
    def write_textBrowser(self, cond_dict):            
        try:
            self.textBrowser.setText("")
            values = cond_dict.values()
            str1 = ""
            for v in values:
                if len(v)>0:
                    for item in v:
                        if isinstance(item, int):
                            item = str(item)
                        str1 += item
                        
                        str1 += "/"
            self.textBrowser.append(str1)
        except:
            logger.logger().exception('')     
    
                    
    # 将查询结果插入表格
    def insert_table(self, res_list):
        try:
            l1 = len(res_list) #获取总记录数
            self.tableWidget.setRowCount(l1)
    #         self.tableWidget.show()      
            for i in range(l1):
                values = res_list[i] #获取每条记录
                l2=len(values) #获取每条记录的项数
                for j in range(l2):  
                    cnt=values[j] # 获取每一项
                      
                    if j in [2, 6, 13, 12, 11, 10, 9] :  
                        item = QTableWidgetItem()
                        item.setData(Qt.DisplayRole,QVariant(cnt))  
                    else:  
                        item = QTableWidgetItem()
                        item.setText(cnt)  
                    self.tableWidget.setItem(i,j,item) 
                    del item
            del res_list
            self.tableWidget.setSortingEnabled(True)
        except:
            logger.logger().exception('')


    # 获取条件信息   
    def get_info(self):        
        '''获取用户设定的信息
        return year, area, cond_dict
        '''
        try:
            school = []
            batch=[] 
            st_cat=[]    
            st_score=[]
            st_rank=[]        
            major_tmp=[]

            year = str(self.lineEdit_year.text())
            
            area = self.comboBox_area.currentText()
            
            batch_str = self.comboBox_batch.currentText()
            if batch_str!='':
                batch=[batch_str] 
                
            st_cat_str = self.comboBox_st_cat.currentText()    
            if st_cat_str!='':
                st_cat=[st_cat_str] 
                
            school_str = self.lineEdit_sch.text()    
            if school_str!='':
                school = [school_str]     
                
            st_score_str = str(self.lineEdit_score.text())
            if st_score_str!='':
                st_score=[int(st_score_str)]
                
            st_rank_str = str(self.lineEdit_rank.text())
            if st_rank_str!='':
                st_rank=[int(st_rank_str)]        
            
            major_str = str(self.lineEdit_major.text())
            
            if major_str!='':
                major_tmp = [major_str]
            
            major_cat=self.major_cat
            
            major = self.major+major_tmp
            
            sch_level=self.sch_level
            
            cond_dict = {'SCHOOL': school, 'SCH_LEVEL': sch_level,
                     'BATCH': batch,'ST_CAT': st_cat, 'SCORE_LINE': st_score, 
                     'MAJOR_CAT': major_cat, 'MAJOR': major, 'SCORE_MIN': st_score, 
                     'RANK_MIN': st_rank}
        except:
            logger.logger().exception('')
        finally:
            return year, area, cond_dict

    
    def reset_cond_dict(self):
        try:
            cond_dict={}
            
            school = []
            sch_level=[]
            batch=[] 
            st_cat=[]    
            st_score=[]
            major_cat=[]
            st_rank=[]        
            major=[]
            
            cond_dict = {'SCHOOL': school, 'SCH_LEVEL': sch_level,
                     'BATCH': batch,'ST_CAT': st_cat, 'SCORE_LINE': st_score, 
                     'MAJOR_CAT': major_cat, 'MAJOR': major, 'SCORE_MIN': st_score, 
                     'RANK_MIN': st_rank}
        except:
            logger.logger().exception('')
        finally:
            return cond_dict


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

