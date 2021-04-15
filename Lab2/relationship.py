import pymysql

# 序列与神、源质的属于关系
class belongGStoSeq:
    def Init(db, cursor, belong_name, name1, name2):
        cursor.execute("drop table if exists " + belong_name)
        sql = """create table """+ belong_name +""" (
                name1 varchar(30),
                name2 varchar(30),
                foreign key (name1) references """+name1+"""(name),
                foreign key (name2) references """+name2+"""(name));"""
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
    
    def Display(db, cursor, belong_name):
        sql = "select * from "+ belong_name
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

# 塔罗会与序列的属于关系
class belongSeqtoT:
    def Init(db, cursor, belong_name, codename, name):
        cursor.execute("drop table if exists " + belong_name)
        sql = """create table """+ belong_name +""" (
                codename varchar(30),
                name varchar(30),
                foreign key (name) references """+name+""" (name),
                foreign key (codename) references """+codename+""" (codename))"""
        cursor.execute(sql)
        db.commit()
        return belong_name

    def InsertSlient(db, cursor, belong_name, codename, name):
        sql = "insert into "+ belong_name +"(codename, name) value(\'" + codename + "\', \'" + name + "\');"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def Display(db, cursor, belong_name):
        sql = "select * from "+ belong_name
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

# 序列与序列的转换关系
class transformStoS:
    def Init(db, cursor, transform_name, name1, name2):
        cursor.execute("drop table if exists " + transform_name)
        sql = """create table """+ transform_name +""" (
                name1 varchar(30),
                name2 varchar(30),
                foreign key (name1) references """+name1+""" (name),
                foreign key (name2) references """+name2+""" (name))"""
        cursor.execute(sql)
        db.commit()
        return transform_name

    def InsertSlient(db, cursor, transform_name, name1, name2):
        sql = "insert into "+ transform_name +"(name1, name2) value(\'" + name1 + "\', \'" + name2 + "\');"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()
    
    def Display(db, cursor, transform_name):
        sql = "select * from "+ transform_name
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