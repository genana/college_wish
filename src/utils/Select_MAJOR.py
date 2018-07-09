# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from gui.Ui_Select_MAJOR import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.states=[]
        self.paras=[['计算机科学与技术', '软件工程', '网络工程', '物联网工程'],
        ['经济学', '财政学', '国民经济管理', '资源与环境经济学', '经济统计学'],
        ['土木工程', '道路桥梁与渡河工程', '建筑环境与能源应用工程', '建筑电气与智能化', '铁道工程'],
        ['材料科学与工程', '冶金工程', '高分子材料与工程', '金属材料工程', '无机非金属材料工程'],
        ['机械工程', '机械设计制造及其自动化', '材料成型及控制工程', '工业设计', '车辆工程'],
        ['电气工程及其自动化', '智能电网信息工程', '电气工程与智能控制', '光源与照明'],
        ['金融学', '保险学', '金融数学', '投资学', '金融工程'],
        ['通信工程', '电子信息工程', '电子科学与技术', '微电子科学与工程', '信息工程'],
        ['建筑学', '城乡规划', '风景园林', '历史建筑保护工程'],
        ['采矿工程', '石油工程', '矿物加工工程', '油气储运工程', '海洋油气工程'],
        ['航空航天工程', '飞行器设计与工程', '飞行器制造工程', '飞行器动力工程', '飞行器适航技术'],
        ['自动化', '轨道交通信号与控制'],
        ['工商管理', '会计学', '财务管理', '审计学', '资产评估'],
        ['艺术设计学', '视觉传达设计', '产品设计', '数字媒体艺术', '服装与服饰设计'],
        ['旅游管理', '酒店管理', '会展经济与管理', '旅游管理与服务教育'],
        ['数学与应用数学', '信息与计算科学', '数学'],
        ['物理学', '应用物理学', '核物理', '物理'],
        ['应用化学', '化学生物学', '分子科学与工程', '化学'],
        ['生物科学', '生物技术', '生物信息学', '生态学', '生物'],
        ['历史学', '世界史', '考古学', '文物保护技术', '历史'],
        ['汉语言文学', '汉语言', '汉语国际教育', '古典文献学', '语言文学'],
        ['英语', '俄语', '法语', '德语', '西班牙语', '阿拉伯语']
        ]
        
  
    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        for k, item in enumerate(self.paras):
            m=getattr(self,"checkBox%d"%(k+1))
            if m.isChecked():
               print("checkBox%d"%(k+1))
               self.states.extend(item)
        self.close()
    
    # 重设CheckStates
    def reset_check(self):
        for k, item in enumerate(self.paras):
            m=getattr(self,"checkBox%d"%(k+1))
            m.setCheckState(0) 
        
    
    @pyqtSlot()
    def on_pushButton_cancel_clicked(self):
        """
        Slot documentation goes here.
        """
        self.close()
