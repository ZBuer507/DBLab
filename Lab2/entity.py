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
            print(sequence_name + "已提交名为" + name + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    def InsertSlient(db, cursor, sequence_name, road, name):
        sql = "insert into "+ sequence_name +"(road, name) value(\'" + road + "\', \'" + name + "\');"
        try:
            cursor.execute(sql)
            db.commit()
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
            print(sequence_name + "已更新road为" + road + "的信息")
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
            print(sequence_name + "已删除road为" + road + "的信息")
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
            for item in data:
                print(item["name"])
        except:
            print("Error in \"" + sql + "\"")
            pass

# 神（天使，圣者）
# 源质
class godorsource:
    def Init(db, cursor, godorsource_name):
        cursor.execute("drop table if exists " + godorsource_name)
        sql = """create table """+ godorsource_name +""" (
                name varchar(30),
                PRIMARY KEY (name))"""
        cursor.execute(sql)
        db.commit()
        return godorsource_name

    def Insert(db, cursor, godorsource_name):
        sql = "insert into "+ godorsource_name +"(name) "
        name = input("name:")
        sql = sql + "value(\'" + name + "\');"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(godorsource_name + "已提交名为" + name + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    def InsertSlient(db, cursor, godorsource_name, name):
        sql = "insert into "+ godorsource_name +"(name) value(\'" + name + "\');"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Delete(db, cursor, godorsource_name):
        sql = "DELETE FROM "+ godorsource_name +" WHERE name = "
        name = input("要删除的name：")
        sql = sql + "\'" + name + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(godorsource_name + "已删除name为" + name + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def Select(db, cursor, godorsource_name):
        sql = "select name from "+ godorsource_name
        print(sql)
        try:
            cursor.execute(sql)
            print(godorsource_name + "中的name:")
            data = cursor.fetchall()
            for item in data:
                print(item["name"])
        except:
            print("Error in \"" + sql + "\"")
            pass

# 塔罗会
class tarot_club:
    def Init(db, cursor, tarot_club_name):
        cursor.execute("drop table if exists " + tarot_club_name)
        sql = """create table """+ tarot_club_name +""" (
                codename varchar(30),
                name varchar(30),
                PRIMARY KEY (codename))"""
        cursor.execute(sql)
        db.commit()
        return tarot_club_name

    def Insert(db, cursor, tarot_club_name):
        sql = "insert into "+ tarot_club_name +"(codename, name) "
        codename = input("codename:")
        name = input("name:")
        sql = sql + "value(\'" + codename + "\', \'" + name + "\');"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(tarot_club_name + "已提交名为" + name + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    def InsertSlient(db, cursor, tarot_club_name, codename, name):
        sql = "insert into "+ tarot_club_name +"(codename, name) value(\'" + codename + "\', \'" + name + "\');"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Update(db, cursor, tarot_club_name):
        codename = input("需更改信息的codename：")
        sql = "UPDATE "+ tarot_club_name +" "
        name = input("请输入新的name：")
        sql = sql + "set name = \'" + name + "\' "
        sql = sql + "WHERE codename = \'" + codename + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(tarot_club_name + "已更新codename为" + codename + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Delete(db, cursor, tarot_club_name):
        sql = "DELETE FROM "+ tarot_club_name +" WHERE codename = "
        codename = input("要删除的codename：")
        sql = sql + "\'" + codename + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(tarot_club_name + "已删除codename为" + codename + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def SelectName(db, cursor, tarot_club_name):
        sql = "select name from "+ tarot_club_name +" where codename = "
        codename = input("途径序号：")
        sql = sql + "\'" + codename + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            print(tarot_club_name + "中途径序号为" + codename + "的名称:")
            data = cursor.fetchall()
            for item in data:
                print(item["name"])
        except:
            print("Error in \"" + sql + "\"")
            pass