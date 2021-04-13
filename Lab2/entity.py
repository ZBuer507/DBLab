import pymysql

# 序列
class sequence:
    def Init(db, cursor, sequence_name):
        cursor.execute("drop table if exists " + sequence_name)
        sql = """create table """+ sequence_name +""" (
                road INT UNSIGNED,
                name char(30))
                PRIMARY KEY road"""
        cursor.execute(sql)
        db.commit()
        return sequence_name

    def Insert(db, cursor, sequence_name):
        sql = "insert into "+ sequence_name +"(road, name) "
        road = int(input("road:").split())
        name = input("name")
        sql = sql + "value(\'" + road + "\', \'" + name + "\');"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print("已提交名为" + name + "的序列信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Update(db, cursor, sequence_name):
        running = True
        road = input("需更改信息的road：")
        print("请选择需要修改的基本信息：\n"
            "1.road\n"
            "2.name\n"
            "3.退出\n")
        choose = input()
        while running:
            sql = "UPDATE "+ sequence_name +" "
            if choose == "1":
                road = int(input("请输入新的road：").split())
                sql = sql + "set road = \'" + road + "\' "
                break
            elif choose == "2":
                name = input("请输入新的name：")
                sql = sql + "set name = \'" + name + "\' "
                break
            elif choose == "3":
                running = False
            else:
                continue
        if running == True:
            sql = sql + "WHERE road = \'" + road + "\';"
            print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                print("已更新编号为" + road + "的用户信息")
            except:
                print("Error in \"" + sql + "\"")
                db.rollback()

    def Delete(db, cursor, sequence_name):
        sql = "DELETE FROM "+ sequence_name +" WHERE road = "
        road = input("要删除的road：")
        sql = sql + "\'" + road + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print("已删除编号为" + road + "的用户信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()