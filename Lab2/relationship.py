import pymysql

# 序列与神、源质的属于关系
class belongGStoSeq:
    def Init(db, cursor, belong_name, name1, name2):
        cursor.execute("drop table if exists " + belong_name)
        sql = """create table """+ belong_name +""" (
                name1 varchar(30),
                name2 varchar(30),
                FOREIGN KEY (name1) REFERENCES """+name1+"""(name)
                FOREIGN KEY (name2) REFERENCES """+name2+"""(name))"""
        cursor.execute(sql)
        db.commit()
        return belong_name

    def InsertSlient(db, cursor, belong_name, name1, name2):
        sql = "insert into "+ belong_name +"(name1, name2) value(\'" + name1 + "\', \'" + name2 + "\');"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Update(db, cursor, belong_name):
        name1 = input("需更改信息的name1：")
        sql = "UPDATE "+ belong_name +" "
        name2 = input("请输入新的name2：")
        sql = sql + "set name2 = \'" + name2 + "\' "
        sql = sql + "WHERE name1 = \'" + name1 + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(belong_name + "已更新name1为" + name1 + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def Select(db, cursor, belong_name):
        sql = "select name2 from "+ belong_name +" where name1 = "
        name1 = input("途径序号：")
        sql = sql + "\'" + name1 + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            print(belong_name + "中途径序号为" + name1 + "的名称:")
            data = cursor.fetchall()
            for item in data:
                print(item["name2"])
        except:
            print("Error in \"" + sql + "\"")
            pass

# 塔罗会与序列的属于关系
class belongSeqtoT:
    def Init(db, cursor, belong_name, name1, name2):
        cursor.execute("drop table if exists " + belong_name)
        sql = """create table """+ belong_name +""" (
                name1 varchar(30),
                name2 varchar(30),
                FOREIGN KEY (name1) REFERENCES """+name1+"""(name)
                FOREIGN KEY (name2) REFERENCES """+name2+"""(codename))"""
        cursor.execute(sql)
        db.commit()
        return belong_name

    def InsertSlient(db, cursor, belong_name, name1, name2):
        sql = "insert into "+ belong_name +"(name1, name2) value(\'" + name1 + "\', \'" + name2 + "\');"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Update(db, cursor, belong_name):
        name1 = input("需更改信息的name1：")
        sql = "UPDATE "+ belong_name +" "
        name2 = input("请输入新的name2：")
        sql = sql + "set name2 = \'" + name2 + "\' "
        sql = sql + "WHERE name1 = \'" + name1 + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(belong_name + "已更新name1为" + name1 + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def Selectname(db, cursor, belong_name):
        sql = "select name2 from "+ belong_name +" where name1 = "
        name1 = input("途径序号：")
        sql = sql + "\'" + name1 + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            print(belong_name + "中途径序号为" + name1 + "的名称:")
            data = cursor.fetchall()
            for item in data:
                print(item["name2"])
        except:
            print("Error in \"" + sql + "\"")
            pass

# 序列与序列的转换关系
class transformStoS:
    def Init(db, cursor, belong_name, name1, name2):
        cursor.execute("drop table if exists " + belong_name)
        sql = """create table """+ belong_name +""" (
                name1 varchar(30),
                name2 varchar(30),
                FOREIGN KEY (name1) REFERENCES """+name1+"""(name)
                FOREIGN KEY (name2) REFERENCES """+name2+"""(name))"""
        cursor.execute(sql)
        db.commit()
        return belong_name

    def InsertSlient(db, cursor, belong_name, name1, name2):
        sql = "insert into "+ belong_name +"(name1, name2) value(\'" + name1 + "\', \'" + name2 + "\');"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Update(db, cursor, belong_name):
        name1 = input("需更改信息的name1：")
        sql = "UPDATE "+ belong_name +" "
        name2 = input("请输入新的name2：")
        sql = sql + "set name2 = \'" + name2 + "\' "
        sql = sql + "WHERE name1 = \'" + name1 + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(belong_name + "已更新name1为" + name1 + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def Select(db, cursor, belong_name):
        sql = "select name2 from "+ belong_name +" where name1 = "
        name1 = input("途径序号：")
        sql = sql + "\'" + name1 + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            print(belong_name + "中途径序号为" + name1 + "的名称:")
            data = cursor.fetchall()
            for item in data:
                print(item["name2"])
        except:
            print("Error in \"" + sql + "\"")
            pass