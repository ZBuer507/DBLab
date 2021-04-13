import pymysql

# 序列
class sequence:
    def Init(db, cursor, sequence_name):
        cursor.execute("drop table if exists " + sequence_name)
        sql = """create table """+ sequence_name +""" (
                road varchar(2),
                name varchar(30),
                PRIMARY KEY (road))"""
        cursor.execute(sql)
        db.commit()
        return sequence_name

    def Insert(db, cursor, sequence_name):
        sql = "insert into "+ sequence_name +"(road, name) "
        road = input("road:")
        name = input("name:")
        sql = sql + "value(\'" + road + "\', \'" + name + "\');"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(sequence_name + "序列已提交名为" + name + "的序列信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Update(db, cursor, sequence_name):
        road = input("需更改信息的road：")
        sql = "UPDATE "+ sequence_name +" "
        name = input("请输入新的name：")
        sql = sql + "set name = \'" + name + "\' "
        sql = sql + "WHERE road = \'" + road + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(sequence_name + "序列已更新road为" + road + "的信息")
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
            print(sequence_name + "序列已删除road为" + road + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def SelectName(db, cursor, sequence_name):
        sql = "select name from "+ sequence_name +" where road = "
        road = input("途径序号：")
        sql = sql + "\'" + road + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            print(sequence_name + "中途径序号为" + road + "的名称:")
            data = cursor.fetchall()
            print(data[0]["name"])
        except:
            print("Error in \"" + sql + "\"")
            pass