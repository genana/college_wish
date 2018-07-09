#coding=utf-8

# 导包
import xlrd
import sqlite3
import os
import glob
import traceback
import utils.logger as logger

"""
数据库生成模块
模块简介：
    根据Excel工作薄生成数据库文件。

每个workbook下包含多个sheet，每个sheet第一行包含以下字段信息：
    "地区","学校","院校代码","学校类别","录取批次","考生类别","学校分数线",
    "学科门类","专业","专业最低分","专业最低位次","专业最高分","专业最高位次","招生人数"
    对应SQL字段名称：
    "AREA", "SCHOOL", "SCH_CODE", "SCH_LEVEL", "BATCH", "ST_CAT", "SCORELINE",
    "MAJOR_CAT", "MAJOR","SCORE_MIN","RANK_MIN","SCORE_MAX","RANK_MAX","ENROL_NUM"  
    
数据库设计：
    数据库：years - 年份数据
    子表1-31：area_name - 地区院校数据
        字段信息：
        "地区","学校","院校代码","学校类别","录取批次","考生类别","学校分数线",
        "学科门类","专业","专业最低分","专业最低位次","专业最高分","专业最高位次","招生人数"

"""

# reload(sys)
# sys.setdefaultencoding('utf-8')


def seg_db(conn, table_name, sheet_label):
    try:
        c = conn.cursor()
        
        # 获取sheet中的AREA列表
        # 去重复，创建地区子表
        sql_unique = "SELECT DISTINCT AREA FROM {0};".format(table_name)
        cursor = c.execute(sql_unique)
        area_list =  cursor.fetchall()
    
        # 按指定AREA查询记录    
        for area in area_list:
            sql =  "SELECT * FROM {0} WHERE AREA is '{1}' ;".format(table_name, area[0])
            cursor = c.execute(sql)
            res_list =  cursor.fetchall()
            
            # 将指定AREA对应记录写入对应子表
            sub_write_db(sheet_label, res_list, conn, area[0])
    except:
        logger.logger().exception('')
        

# 将行数据写入db文件
def write_db(sheet_label, sheet_cont, conn):
    """
    Write xls data to .db files.
    Params:
        sheet_label - A list, 包含本sheet的表头标签
        sheet_cont - A list, 包含本sheet的内容（行数据）
        conn - 目标数据库链接
    """
    try:
        conn.text_factory = str
        c = conn.cursor()
        
        # 创建tmp表 
        table_name = 'tmp'
        
        c.execute('''CREATE TABLE IF NOT EXISTS {0}
               (
               AREA        TEXT    DEFAULT '无',
               SCHOOL      TEXT    DEFAULT '无',
               SCH_CODE    INT         DEFAULT -1,
               SCH_LEVEL   TEXT     DEFAULT '无',
               BATCH       TEXT    DEFAULT '无',
               ST_CAT      TEXT      DEFAULT '无',
               SCORE_LINE  REAL     DEFAULT -1,
               MAJOR_CAT   TEXT DEFAULT '无',
               MAJOR       TEXT DEFAULT '无',
               SCORE_MIN   REAL    DEFAULT -1,
               RANK_MIN    INT     DEFAULT -1,
               SCORE_MAX   REAL    DEFAULT -1,
               RANK_MAX    INT     DEFAULT -1,
               ENROL_NUM   INT     DEFAULT -1, 
               PRIMARY KEY(SCH_CODE, MAJOR, ST_CAT, BATCH)
               );'''.format(table_name))
    
        # 生成占位符
        place_str = ''
        l = len(sheet_label)
        for i in range(l):
            place_str = place_str+'?'
            if i<(l-1):
                place_str = place_str+','
        # 创建查询语句         
        sql =  "REPLACE INTO {0} VALUES ({1})".format(table_name, place_str)             
        
        # 批量插入行数据
        c.executemany(sql, sheet_cont)        
        conn.commit()
        
        # 按地区分割子表
        seg_db(conn, table_name, sheet_label)
        
        # 删除tmp表
        c.execute("DROP TABLE {0}".format(table_name))
        conn.commit()
        
        # 清理删除后的文件空间
        c.execute("VACUUM")
        return 1
    except:
        logger.logger().exception('')
        return 0

    
def sub_write_db(sheet_label, sheet_cont, conn, table_name):
    """
    将area数据写到子表中
    Params:
        sheet_label - A list, 包含本sheet的表头标签
        sheet_cont - A list, 包含本sheet的内容（行数据）
        conn - 目标数据库链接
    """
    try:
        conn.text_factory = str
        c = conn.cursor()
        
        # 创建表 
        print("创建: ",table_name)
        c.execute('''CREATE TABLE IF NOT EXISTS {0}
               (
               AREA        TEXT    DEFAULT '无',
               SCHOOL      TEXT    DEFAULT '无',
               SCH_CODE    INT         DEFAULT -1,
               SCH_LEVEL   TEXT     DEFAULT '无',
               BATCH       TEXT    DEFAULT '无',
               ST_CAT      TEXT      DEFAULT '无',
               SCORE_LINE  REAL     DEFAULT -1,
               MAJOR_CAT   TEXT DEFAULT '无',
               MAJOR       TEXT DEFAULT '无',
               SCORE_MIN   REAL    DEFAULT -1,
               RANK_MIN    INT     DEFAULT -1,
               SCORE_MAX   REAL    DEFAULT -1,
               RANK_MAX    INT     DEFAULT -1,
               ENROL_NUM   INT     DEFAULT -1, 
               PRIMARY KEY(SCH_CODE, MAJOR, ST_CAT, BATCH)
               );'''.format(table_name))
    
        # 生成占位符
        place_str = ''
        l = len(sheet_label)
        for i in range(l):
            place_str = place_str+'?'
            if i<(l-1):
                place_str = place_str+','
        # 创建查询语句         
        sql =  "REPLACE INTO {0} VALUES ({1})".format(table_name, place_str)             
        
        # 批量插入行数据
        c.executemany(sql, sheet_cont);        
        conn.commit()
    except:
        logger.logger().exception('')
        

def read_xls(xls_name):
    """
    读取xls文件，获取各sheet的内容
    """
    sheet_labels = []
    sheet_conts = []
    sheet_names = []
        
    try:
        xlrd.Book.encoding = "utf-8"
        workbook = xlrd.open_workbook(filename=xls_name)
        
        # 工作薄中的所有sheet名称
        names = workbook.sheet_names()
        # 工作薄中的所有sheet对象
        sheets = workbook.sheets()
        
        # 遍历xls中的每一个sheet
        for i in range(len(names)):
            nrows =  sheets[i].nrows
            #若是空表，则跳过
            if nrows == 0:
                continue
            # sheet名
            sheet_name = names[i] 
            
            sheet_names.append(sheet_name)
            
            # sheet标签：获取第一行        
            sheet_label = sheets[i].row_values(0)
            
            # 当前sheet内容
            sheet_cont=[]
            
            for j in range(1,nrows):
                row_data = sheets[i].row_values(j)
                # 空行跳过
                if len(row_data[0])==0:
                    continue
                sheet_cont.append(row_data)
            sheet_conts.append(sheet_cont)
            sheet_labels.append(sheet_label)
    except:
        logger.logger().exception('')
    finally:    
        return sheet_names, sheet_labels, sheet_conts    
        

def xls2db(xls_name, db_path):
    
    try:
        sheet_names, sheet_labels, sheet_conts = read_xls(xls_name)
        
        for i in range(len(sheet_conts)):
            db_file = db_path+ '/' + sheet_names[i] +'.db';
            print(db_file)
            
            conn = sqlite3.connect(db_file)
            
            state = write_db(sheet_labels[i], sheet_conts[i], conn)
        conn.close()
        if not state:
            if os.path.isfile(db_file):
                os.remove(db_file)
                print(db_file + " was removed!")
        return state
    except:
        logger.logger().exception('')
        return 0
        


if __name__ == '__main__':
    
    
    xls_name = '../data/all_wen.xls'
    
    db_path = './database/de'
    

    
    print(xls2db(xls_name, db_path))
    
#     seg_db(db_file)



