import pymysql
import sys
#把工作区临时添加到系统路径，以使用自定义模块
sys.path.append("D:\计算机\WORKS\DB")
from Lab2.entity import *

def main():
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='507520',
                        port=3306,
                        database="LordofMysteries",
                        cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()

    god_name = "预言家"
    sequence.Init(db, cursor, god_name)
    sequence.Insert(db, cursor, god_name)
    sequence.Insert(db, cursor, god_name)
    sequence.SelectName(db, cursor, god_name)
    db.close()

main()
