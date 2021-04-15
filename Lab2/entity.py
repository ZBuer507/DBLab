import pymysql

# 序列
class sequence:
    def Init(db, cursor, sequence_name):
        cursor.execute("set foreign_key_checks = 0")
        cursor.execute("drop table if exists " + sequence_name)
        sql = """create table """+ sequence_name +""" (
                road varchar(2) not null,
                name varchar(30) not null,
                primary key (name))"""
        cursor.execute(sql)
        cursor.execute("set foreign_key_checks = 1")
        db.commit()
        return sequence_name

    def Insert(db, cursor, sequence_name):
        sql = "insert into "+ sequence_name +"(road, name) "
        road = input("road:")
        name = input("name:")
        if road == "" or name == "":
            print("输入为空")
            return
        sql2 = "select count(*) from "+sequence_name+" where road = \'" + road + "\'"
        cursor.execute(sql2)
        flag = cursor.fetchall()
        if flag[0]["count(*)"] > 0:
            print(road + "重复")
            return
        
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
        name = input("需更改信息的name：")
        sql = "update "+ sequence_name +" "
        road = input("请输入新的road：")
        if road == "":
            print("输入为空")
            return
        sql2 = "select count(*) from "+sequence_name+" where name = \'" + name + "\'"
        cursor.execute(sql2)
        flag = cursor.fetchall()
        if flag[0]["count(*)"] == 0:
            print(name + "不存在")
            return
        sql = sql + "set road = \'" + road + "\' "
        sql = sql + "where name = \'" + name + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(sequence_name + "已更新road为" + road + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Delete(db, cursor, sequence_name):
        sql = "delete from "+ sequence_name +" where name = "
        name = input("要删除的name：")
        if name == "":
            print("输入为空")
            return
        sql2 = "select count(*) from "+sequence_name+" where name = \'" + name + "\'"
        cursor.execute(sql2)
        flag = cursor.fetchall()
        if flag[0]["count(*)"] == 0:
            print(name + "不存在")
            return
        sql = sql + "\'" + name + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(sequence_name + "已删除name为" + name + "的信息")
        except:
            print(name + "存在外键约束,无法删除,建议自己添加一个属性再删除")
            db.rollback()
    
    def Display(db, cursor, sequence_name):
        sql = "select * from "+ sequence_name
        cursor.execute(sql)
        data = cursor.fetchall()
        for item1 in data:
            for item2 in item1:
                if len(item1[item2]) >= 4:
                    print(item1[item2],end="\t")
                else:
                    print(item1[item2],end="\t\t")
            print()
        print()

# 神（天使，圣者）
# 源质
class godorsource:
    def Init(db, cursor, godorsource_name):
        cursor.execute(" set foreign_key_checks = 0")
        cursor.execute("drop table if exists " + godorsource_name)
        sql = """create table """+ godorsource_name +""" (
                name varchar(30) not null,
                PRIMARY KEY (name))"""
        cursor.execute(sql)
        cursor.execute(" set foreign_key_checks = 1")
        db.commit()
        return godorsource_name

    def Insert(db, cursor, godorsource_name):
        sql = "insert into "+ godorsource_name +"(name) "
        name = input("name:")
        if name == "":
            print("输入为空")
            return
        sql2 = "select count(*) from "+godorsource_name+" where name = \'" + name + "\'"
        cursor.execute(sql2)
        flag = cursor.fetchall()
        if flag[0]["count(*)"] > 0:
            print(name + "重复")
            return
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
        sql = "delete from "+ godorsource_name +" where name = "
        name = input("要删除的name：")
        if name == "":
            print("输入为空")
            return
        sql2 = "select count(*) from "+godorsource_name+" where name = \'" + name + "\'"
        cursor.execute(sql2)
        flag = cursor.fetchall()
        if flag[0]["count(*)"] == 0:
            print(name + "不存在")
            return
        sql = sql + "\'" + name + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(godorsource_name + "已删除name为" + name + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def Display(db, cursor, godorsource_name):
        sql = "select * from "+ godorsource_name
        cursor.execute(sql)
        data = cursor.fetchall()
        for item1 in data:
            for item2 in item1:
                if len(item1[item2]) >= 4:
                    print(item1[item2],end="\t")
                else:
                    print(item1[item2],end="\t\t")
            print()
        print()

# 塔罗会
class tarot_club:
    def Init(db, cursor, tarot_club_name):
        cursor.execute(" set foreign_key_checks = 0")
        cursor.execute("drop table if exists " + tarot_club_name)
        sql = """create table """+ tarot_club_name +""" (
                codename varchar(30) not null,
                name varchar(30) not null,
                PRIMARY KEY (codename))"""
        cursor.execute(sql)
        cursor.execute(" set foreign_key_checks = 1")
        db.commit()
        return tarot_club_name

    def Insert(db, cursor, tarot_club_name):
        sql = "insert into "+ tarot_club_name +"(codename, name) "
        codename = input("codename:")
        name = input("name:")
        if codename == "" or name == "":
            print("输入为空")
            return
        sql2 = "select count(*) from "+tarot_club_name+" where codename=\'" + codename + "\'"
        cursor.execute(sql2)
        flag = cursor.fetchall()
        if flag[0]["count(*)"] > 0:
            print(codename + "重复")
            return
        
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
        sql = "update "+ tarot_club_name +" "
        name = input("请输入新的name：")
        if codename == "":
            print("输入为空")
            return
        sql2 = "select count(*) from "+tarot_club+" where codename = \'" + codename + "\'"
        cursor.execute(sql2)
        flag = cursor.fetchall()
        if flag[0]["count(*)"] == 0:
            print(codename + "不存在")
            return
        sql = sql + "set name = \'" + name + "\' "
        sql = sql + "where codename = \'" + codename + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(tarot_club_name + "已更新codename为" + codename + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()

    def Delete(db, cursor, tarot_club_name):
        sql = "delete from "+ tarot_club_name +" where codename = "
        codename = input("要删除的codename：")
        if codename == "":
            print("输入为空")
            return
        sql2 = "select count(*) from "+tarot_club+" where codename = \'" + codename + "\'"
        cursor.execute(sql2)
        flag = cursor.fetchall()
        if flag[0]["count(*)"] == 0:
            print(codename + "不存在")
            return
        sql = sql + "\'" + codename + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print(tarot_club_name + "已删除codename为" + codename + "的信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def Display(db, cursor, tarot_club_name):
        sql = "select * from "+ tarot_club_name
        cursor.execute(sql)
        data = cursor.fetchall()
        for item1 in data:
            for item2 in item1:
                if len(item1[item2]) >= 4:
                    print(item1[item2],end="\t")
                else:
                    print(item1[item2],end="\t\t")
            print()
        print()