import pymysql
import sys
#把工作区临时添加到系统路径，以使用自定义模块
sys.path.append("D:\计算机\WORKS\DB")
from Lab2.entity import *
from Lab2.relationship import *

# 用来存储类型为sequence的表的名字
global sequenceName
sequenceName = []
# 用来存储类型为tarot_club的表的名字
global tarrotClubName
tarotClub = []
# 用来存储类型为godorsource的表的名字
global sourceName
sourceName = []
# 用来存储属于关系(belongGStoSeq, belongSeqtoT)的表的名字
global relaBelongName
relaBelongName = []
# 用来存储转换关系(transformStoS)的表的名字
global relaTranformName
relaTranformName = []

# 连接查询，分组查询
def groupTarotBySequence(db, cursor):
    data = []
    for item1 in tarotClub:
        for item2 in relaBelongName:
            if item2[1] == '2':
                sql = """select """ + item2[0] +""".name, group_concat("""+item1+""".codename)
                        from """+item1+""" 
                        inner join """ + item2[0] +"""
                        on """+item1+""".codename =  """ + item2[0] +""".codename
                        group by """ + item2[0] +""".name"""
                cursor.execute(sql)
                print(sql)
                data += cursor.fetchall()
    print("序列名\t代号")
    for item1 in data:
        for item2 in item1:
            if len(item1[item2]) >= 4:
                print(item1[item2],end="\t")
            else:
                print(item1[item2],end="\t\t")
        print()
    print()

# 分组查询
def searchTarotAndSequence(db, cursor):
    data = []
    for item1 in tarotClub:
        for item2 in relaBelongName:
            if item2[1] == '2':
                sql = """select """+item1+""".codename, """+item1+""".name, """ + item2[0] +""".name
                        from """+item1+""" 
                        inner join """ + item2[0] +"""
                        on """+item1+""".codename =  """ + item2[0] +""".codename"""
                cursor.execute(sql)
                print(sql)
                data += cursor.fetchall()
    print("代号\t姓名\t序列名")
    for item1 in data:
        for item2 in item1:
            if len(item1[item2]) >= 4:
                print(item1[item2],end="\t")
            else:
                print(item1[item2],end="\t\t")
        print()
    print()

# 查询
def searchSourceAndSequence(db, cursor):
    data = []
    for item1 in sequenceName:
        for item2 in relaBelongName:
            if item2[1] == '1':
                sql = """select """+item1+""".road, """+item1+""".name, """ + item2[0] + """.name1
                        from """+item1+""", """ + item2[0] + """
                        where """+item1+""".name = """ + item2[0] + """.name2"""
                cursor.execute(sql)
                print(sql)
                data += cursor.fetchall()
    print("序列\t\t序列名\t\t源质")
    for item1 in data:
        for item2 in item1:
            if len(item1[item2]) >= 4:
                print(item1[item2],end="\t")
            else:
                print(item1[item2],end="\t\t")
        print()
    print()

# 从视图中查询
def searchGodInTarot(db, cursor):
    data = []
    for item1 in sequenceName:
        for item2 in tarotClub:
            for item3 in relaBelongName:
                if item3[1] == "2":
                    sql = """select * from """+item1+item2+item3[0]
                    cursor.execute(sql)
                    print(sql)
                    data += cursor.fetchall()
    print("序列\t\t序列名\t\t代号\t\t姓名")
    for item1 in data:
        for item2 in item1:
            if len(item1[item2]) >= 4:
                print(item1[item2],end="\t")
            else:
                print(item1[item2],end="\t\t")
        print()
    print()

# 建立视图
def viewGodInTarot(db, cursor):
    for item1 in sequenceName:
        for item2 in tarotClub:
            for item3 in relaBelongName:
                if item3[1] == "2":
                    cursor.execute("drop view if exists "+item1+item2+item3[0])
                    sql = """create view """+item1+item2+item3[0]+"""(road, roadname, codename, name)
                            as select """+item1+""".road, """+item1+""".name, """ + item2 + """.codename, """ + item2 + """.name
                            from """+item1+""", """ + item2 + """, """ + item3[0] + """
                            where """+item1+""".name = """ + item3[0] + """.name 
                                and """+item2+""".codename = """ + item3[0] + """.codename
                                and """+item1+""".road in (
                                    select road
                                    from """ + item1 + """
                                    where """ + item1 + """.road < 5)"""
                    cursor.execute(sql)
                    print(sql)

# 分组查询包含having语句
def searchGodInTaroGroupAndHaving(db, cursor):
    data = []
    for item1 in sequenceName:
        for item2 in tarotClub:
            for item3 in relaBelongName:
                if item3[1] == "2":
                    sql = """select """+item1+""".road, """+item1+""".name, """ + item2 + """.codename, """ + item2 + """.name
                            from """+item1+""", """ + item2 + """, """ + item3[0] + """
                            where """+item1+""".name = """ + item3[0] + """.name and """+item2+""".codename = """ + item3[0] + """.codename
                            group by """ + item2 + """.codename
                            having """+item1+""".road < 5"""
                    cursor.execute(sql)
                    print(sql)
                    data += cursor.fetchall()
    print("序列\t\t序列名\t\t代号\t\t姓名")
    for item1 in data:
        for item2 in item1:
            if len(item1[item2]) >= 4:
                print(item1[item2],end="\t")
            else:
                print(item1[item2],end="\t\t")
        print()
    print()

# 下面的几个establish函数都使用了自动机的思想，
# 从文件中读取数据，
# 根据输入切换state，
# 达成建立表和关系的目的
def establishRelationship(db, cursor):
    with open('Lab2/belongAndTransform.txt', "r", encoding=("utf8")) as f:
        lines = []
        while True:
            seg = f.readline()
            if not seg: break
            elif seg.strip('\n'): lines.append(seg.strip('\n'))
    state = 0
    name = ""
    name1 = ""
    name2 = ""
    name3 = ""
    name4 = ""
    length = len(lines)
    i = 0
    while True:
        if lines[i] == "#" and state == 0:
            state = 1
            #i += 1
        elif lines[i] == "#" and state == 2:
            state = 0
            #i += 1
        elif lines[i] == "1":
            i += 1
            name = lines[i]
            i += 1
            name1, name2 = lines[i].split()
            i += 1
            belongGStoSeq.Init(db, cursor, name, name1, name2)
            relaBelongName.append([name, "1"])
            while lines[i] != "#":
                name3, name4 = lines[i].split()
                belongGStoSeq.InsertSlient(db, cursor, name, name3, name4)
                i += 1
            state = 2
        elif lines[i] == "2":
            i += 1
            name = lines[i]
            i += 1
            name1, name2 = lines[i].split()
            i += 1
            belongSeqtoT.Init(db, cursor, name, name1, name2)
            relaBelongName.append([name, "2"])
            while lines[i] != "#":
                name3, name4 = lines[i].split()
                belongSeqtoT.InsertSlient(db, cursor, name, name3, name4)
                i += 1
            state = 2
        elif lines[i] == "4":
            i += 1
            name = lines[i]
            i += 1
            name1, name2 = lines[i].split()
            i += 1
            transformStoS.Init(db, cursor, name, name1, name2)
            relaTranformName.append(name)
            while lines[i] != "#":
                name3, name4 = lines[i].split()
                transformStoS.InsertSlient(db, cursor, name, name3, name4)
                i += 1
            state = 2
        i += 1
        if(i >= length):
            break

def establishTarotClub(db, cursor):
    with open('Lab2/tarot_club.txt', "r", encoding=("utf8")) as f:
        lines = []
        while True:
            seg = f.readline()
            if not seg: break
            elif seg.strip('\n'): lines.append(seg.strip('\n'))
    state = 0
    name = ""
    name1 = ""
    name2 = ""
    for line in lines:
        if line == "#" and state == 0:
            state = 1
        elif line == "#" and state == 2:
            state = 0
        elif state == 1:
            name = line
            tarot_club.Init(db, cursor, name)
            tarotClub.append(name)
            state = 2
        elif state == 2:
            name1, name2 = line.split()
            tarot_club.InsertSlient(db, cursor, name, name1, name2)
        # print(line)

def establishSequence(db, cursor):
    with open('Lab2/sequence.txt', "r", encoding=("utf8")) as f:
        lines = []
        while True:
            seg = f.readline()
            if not seg: break
            elif seg.strip('\n'): lines.append(seg.strip('\n'))
    state = 0
    name = ""
    name1 = ""
    name2 = ""
    for line in lines:
        if line == "#" and state == 0:
            state = 1
        elif line == "#" and state == 2:
            state = 0
        elif state == 1:
            name = line
            sequence.Init(db, cursor, name)
            sequenceName.append(name)
            state = 2
        elif state == 2:
            name1, name2 = line.split()
            sequence.InsertSlient(db, cursor, name, name1, name2)
        # print(line)

def establishSource(db, cursor):
    with open('Lab2/source.txt', "r", encoding=("utf8")) as f:
        lines = []
        while True:
            seg = f.readline()
            if not seg: break
            elif seg.strip('\n'): lines.append(seg.strip('\n'))
    state = 0
    name = ""
    name1 = ""
    for line in lines:
        if line == "#" and state == 0:
            state = 1
        elif line == "#" and state == 2:
            state = 0
        elif state == 1:
            name = line
            godorsource.Init(db, cursor, name)
            sourceName.append(name)
            state = 2
        elif state == 2:
            name1 = line
            godorsource.InsertSlient(db, cursor, name, name1)
        # print(line)

def menu():
    flag = "0"
    while True:
        print("1.查询实体和关系\n2.综合查询\n3.插入\n4.删除\n5.修改\n6.退出\n")
        flag = input("请输入:")
        if flag == "1":
            print("1.查询实体\n2.查询关系\n3.取消\n")
            choice = input("请输入:")
            if choice == "1":
                for item in sequenceName:
                    print(item)
                    sequence.Display(db, cursor, item)
                for item in sourceName:
                    print(item)
                    godorsource.Display(db, cursor, item)
                for item in tarotClub:
                    print(item)
                    tarot_club.Display(db, cursor, item)
            elif choice == "2":
                for item in relaBelongName:
                    if item[1] == "1":
                        print(item[0])
                        belongGStoSeq.Display(db, cursor, item[0])
                    elif item[1] == "2":
                        print(item[0])
                        belongSeqtoT.Display(db, cursor, item[0])
                for item in relaTranformName:
                    print(item)
                    transformStoS.Display(db, cursor, item)
            elif choice == "3":
                pass
            else:
                print("不存在此选项")
        elif flag == "2":
            print("1.查询塔罗会各序列成员（分组查询）\n2.查询塔罗会成员序列名称（连接查询）\n3.查询各序列所属源质\n4.查询塔罗会中的神和半神（嵌套查询）\n5.查询塔罗会中的神和半神（group and having）\n6.取消\n")
            choice = input("请输入:")
            if choice == "1":
                groupTarotBySequence(db, cursor)
            elif choice == "2":
                searchTarotAndSequence(db, cursor)
            elif choice == "3":
                searchSourceAndSequence(db, cursor)
            elif choice == "4":
                searchGodInTarot(db, cursor)
            elif choice == "5":
                searchGodInTaroGroupAndHaving(db, cursor)
            elif choice == "6":
                pass
            else:
                print("不存在此选项")
        elif flag == "3":
            print("仅以"+sequenceName[0]+"为例")
            sequence.Display(db, cursor, sequenceName[0])
            sequence.Insert(db, cursor, sequenceName[0])
            sequence.Display(db, cursor, sequenceName[0])
        elif flag == "4":
            print("仅以"+sequenceName[0]+"为例")
            sequence.Display(db, cursor, sequenceName[0])
            sequence.Delete(db, cursor, sequenceName[0])
            sequence.Display(db, cursor, sequenceName[0])
        elif flag == "5":
            print("仅以"+sequenceName[0]+"为例")
            sequence.Display(db, cursor, sequenceName[0])
            sequence.Update(db, cursor, sequenceName[0])
            sequence.Display(db, cursor, sequenceName[0])
        elif flag == "6":
            print("退出程序")
            break
        else:
            flag = "0"
            print("不存在此选项,请重新输入")

if __name__ == "__main__":
    # 默认数据库已经存在
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='507520',
                        port=3306,
                        database="LordofMysteries",
                        cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    # 从文件中读取并建立数据库
    # 每次都是重新开始
    establishSource(db, cursor)
    establishSequence(db, cursor)
    establishTarotClub(db, cursor)
    establishRelationship(db, cursor)
    # 建立试图，sql语句会打印出来
    viewGodInTarot(db, cursor)
    # 菜单，进入循环
    menu()
    db.close()
