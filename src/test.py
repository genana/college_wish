import sqlite3

db_file = './utils/database/de/2016.db'

conn = sqlite3.connect(db_file)
conn.text_factory = str
c = conn.cursor()

res = c.execute("select name from sqlite_master where type='table' order by name;")
table_list =  res.fetchall()


COUNT = 0

for table_name in table_list:
    cursor = c.execute("SELECT count(*) FROM "+table_name[0])
    res = cursor.fetchall()
    print(table_name[0]," : ", res[0][0], '条')
    COUNT += res[0][0]
    
print("共计: ", COUNT, '条')
    
#     C += cursor.fetchall()


