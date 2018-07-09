#coding=utf-8

### 导包
import sqlite3
import utils.logger as logger


"""
多条件查询数据库：
    筛选条件设置： 条件类型均为list
    1：地区    （必选，单选）area: (all), "北京", "黑龙江"等
    2：录取批次    （必选，单选）batch: (all), "提前批", "本科一批"等
    *3：学校类别    （必选，多选）sch_level: (all), '985.0', '211.0', '双一流', '其它'
    4：考生类别    （必选，单选）st_cat: ("理科"),"文科"
    *5：学科        （必选，多选）major_cat: (all), "工科"等
    
    6：年份        （必填，手动填入）year: 2017等
    
    7：学校名称    （选填，手动填入）school: "北京大学"等
    8：专业        （选填，手动填入）major: "计算机科学与技术"等
    9：考生分数    （选填，手动填入）st_score: 555等
    10：考生位次    （选填，手动填入）st_rank: 10133等


    多条件dict:
    {'AREA': area, 'SCHOOL': school, 'SCH_LEVEL': ,'BATCH': batch,
    'ST_CAT': st_cat:, 'SCORE_LINE': st_score:, 'MAJOR_CAT': major_cat:,
    'MAJOR': major:, 'SCORE_MIN': st_score, 'RANK_MIN': st_rank}


"""

def select_sqls(cond_dict, table_name, c):
    
    sqls=[]
    try:
        if table_name=='所有':
            res = c.execute("select name from sqlite_master where type='table' order by name;")
            table_list =  res.fetchall()
        else:
            table_list=[(table_name,)]
        
        for table_name in table_list:
            
            sub_str = ""
            sub_sql=[]
            for item_key in cond_dict.keys():
                item_values = cond_dict.get(item_key)
                l2 = len(item_values)
                
                if (l2>0): # 值：非空list
                    for value in item_values:
                        if isinstance(value, int):
                            if item_key=='RANK_MIN':
                                sub_str += item_key +' > '+ str(value)
                            else:
                                sub_str += item_key +' < '+ str(value)
                                    
                            l2=l2-1
                            if l2>0:
                                sub_str+=' or '
                        elif isinstance(value, str):
                            sub_str += item_key +' is '+ '\'' + str(value) +'\''
                            l2=l2-1
                            if l2>0:
                                sub_str+=' or '
                    sub_sql.append(sub_str)
                    sub_str=""
                else:
                    continue
            
            sub_str = ""                    
            lens = len(sub_sql)        
            for i in range(lens):
                if i<lens-1:
                    sub_str += '('+sub_sql[i]+') and '
                else:
                    sub_str += '('+sub_sql[i]+')'
        
            print(sub_str)
                
            sql = "SELECT * FROM " + table_name[0] + " where " + sub_str +' ;';
            sqls.append(sql)
    except:
        logger.logger().exception("query_db:select_sqls")
    finally:
        return sqls

            
def query_db(db_file, table_name, cond_dict):
    res_list = []
    try:
        conn = sqlite3.connect(db_file)
        conn.text_factory = str
        c = conn.cursor()
        
        sqls = select_sqls(cond_dict, table_name, c)
    
        for sql_stat in sqls:
            cursor = c.execute(sql_stat)
            res_list +=  cursor.fetchall()
            
        print(len(res_list))
        
        cursor.close()
        
    except:
        logger.logger().exception("query_db:select_sqls")
    finally:
        return res_list




if __name__ == '__main__':
        
    area = ['黑龙江']
    school = []
    sch_level = []
    batch = []
    st_cat = []
    st_score = []
    major_cat = ['工学', '理学']
    major = []
    st_rank = []
    
    
    cond_dict = {'SCHOOL': school, 'SCH_LEVEL': sch_level,
                 'BATCH': batch,'ST_CAT': st_cat, 'SCORE_LINE': st_score, 
                 'MAJOR_CAT': major_cat, 'MAJOR': major, 'SCORE_MIN': st_score, 
                 'RANK_MIN': st_rank}

    db_file = '../data/db/2017.db'.decode('utf-8')
    print(cond_dict)



