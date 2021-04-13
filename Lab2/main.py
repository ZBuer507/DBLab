import pymysql
import sys
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
    cursor.execute("drop table if exists user")

    sql = """create table user (
            username char(30),
            name char(30), 
            usersex char(30), 
            birthday char(30), 
            email char(30), 
            address char(30), 
            password char(30))"""
    cursor.execute(sql)
    db.commit()
    
    sequence_name = "预言家"
    sequence.Init(db, cursor, sequence_name)
    sequence.Insert(db, cursor, sequence_name)
    db.close()

main()
"""
    while running:
        print("--------------------------------")
        print("1.查询\n2.增添\n3.更新\n4.删除\n5.退出")
        print("--------------------------------")
        chooseFunction = input()
        if chooseFunction == "1":
            while runningSub:
                print("-----------------------------------------------------------------------------")
                print("1.\n"
                      "10.退出")
                print("-----------------------------------------------------------------------------")
                chooseSubFunction = input()
                if chooseSubFunction == "1":
                    Select1(cursor)
                elif chooseSubFunction == "10":
                    runningSub = False
                else:
                    continue
        elif chooseFunction == "2":
            print("--------------------------------")
            print("在user表新增记录2条记录")
            print("--------------------------------")
            print("第一条记录：")
            Insert(db, cursor)
            print("--------------------------------")
            print("第二条记录：")
            Insert(db, cursor)
            print("--------------------------------")
        elif chooseFunction == "3":
            Update(db, cursor)
        elif chooseFunction == "4":
            Delete(db, cursor)
        elif chooseFunction == "5":
            running = False
        else:
            continue
    db.close()


main()
"""