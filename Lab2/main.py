import pymysql
from Lab2.entity import *


# 查询直接领导为usersex的用户编号
def Select1(cursor):
    sql = "SELECT username FROM user e1 WHERE e1.address = (SELECT username FROM user e2 WHERE e2.usersex = "
    usersex = input("直接领导姓名：")
    sql = sql + "\"" + usersex + "\");"
    print(sql)
    try:
        cursor.execute(sql)
        print("直接领导为" + usersex + "的用户编号:")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 在user表新增记录1条记录；
def Insert(db, cursor):
    sql = "insert into user(username, name, usersex, birthday, email, address, password) "
    username = input("用户名(邮箱，不可修改)：")
    name = input("姓名：")
    usersex = input("性别：")
    birthday = input("出生日期：")
    email = input("电子邮箱(可多个)：")
    address = input("通讯地址：")
    password = input("用户密码：")
    sql = sql + "value(\'" + username + "\', \'" + name + "\', \'" + usersex + "\', \'" + birthday + "\', " + email + ", \'" + address + "\', \'" + password + "\');"
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("已提交名为" + username + "的用户信息")
    except:
        print("Error in \"" + sql + "\"")
        db.rollback()


# 更新用户信息
def Update(db, cursor):
    running = True
    username = input("需更改信息的用户名：")
    print("--------------------------------")
    print("请选择需要修改的基本信息：\n"
          "1.姓名\n"
          "2.性别\n"
          "3.出生日期\n"
          "4.电子邮箱\n"
          "5.通讯地址\n"
          "6.用户密码\n"
          "7.退出")
    print("--------------------------------")
    choose = input()
    while running:
        sql = "UPDATE user "
        if choose == "1":
            usersex = input("请输入新的姓名：")
            sql = sql + "set usersex = \'" + usersex + "\' "
            break
        elif choose == "2":
            birthday = input("请输入新的性别：")
            sql = sql + "set birthday = \'" + birthday + "\' "
            break
        elif choose == "3":
            email = input("请输入新的出生日期：")
            sql = sql + "set email = " + email + " "
            break
        elif choose == "4":
            address = input("请输入新的电子邮箱：")
            sql = sql + "set address = \'" + address + "\' "
            break
        elif choose == "5":
            password = input("请输入新的通讯地址：")
            sql = sql + "set password = \'" + password + "\' "
            break
        elif choose == "6":
            password = input("请输入新的用户密码：")
            sql = sql + "set password = \'" + password + "\' "
            break
        elif choose == "7":
            running = False
        else:
            continue
    if running == True:
        sql = sql + "WHERE username = \'" + username + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print("已更新编号为" + username + "的用户信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()


# 删除用户记录
def Delete(db, cursor):
    sql = "DELETE FROM user WHERE username = "
    username = input("要删除的用户编号：")
    sql = sql + "\'" + username + "\';"
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("已删除编号为" + username + "的用户信息")
    except:
        print("Error in \"" + sql + "\"")
        db.rollback()


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
    running = True
    runningSub = True
    while running:
        print("--------------------------------")
        print("1.查询\n2.增添\n3.更新\n4.删除\n5.退出")
        print("--------------------------------")
        chooseFunction = input()
        if chooseFunction == "1":
            while runningSub:
                print("-----------------------------------------------------------------------------")
                print("1.查询直接领导为usersex的用户编号\n"
                      "2.查询项目所在地为PLOCATION的部门名称\n"
                      "3.查询参与PNAME项目的所有工作人员的名字和居住地址\n"
                      "4.查询部门领导居住地在birthday且工资不低于email元的用户姓名和居住地\n"
                      "5.查询没有参加项目编号为PNO的项目的用户姓名\n"
                      "6.查询部门领导工作日期在MGRSTARTDATE之后的部门名\n"
                      "7.查询总工作量大于HOURS小时的项目名称\n"
                      "8.查询用户平均工作时间低于HOURS的项目名称\n"
                      "9.查询至少参与了N个项目并且工作总时间超过HOURS小时的用户名字\n"
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
