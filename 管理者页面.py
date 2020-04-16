'''实现功能
1.创建运动会数据库
2.分别自动导入运动员、裁判txt数据表
3.快速查找功能
4.按表名创建、删除表
5.自己输入sql语句

'''
# -*- coding: UTF-8 -*-
from tkinter import * 
import tkinter
import sqlite3      #导入sqlite3
import os
path = os.getcwd()  # 返回当前工作目录
filesy = os.listdir(path+"\yundongyuan")  # 返回指定的文件夹包含的文件或文件夹的名字的列表
filesc = os.listdir(path+"\caipan")

'''1.1 创建数据库'''
def create_database():  
    # 数据库初始化
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
'''自动导入运动员/裁判'''
def create_table_txt1():#运动员：裁判编号、姓名、编号、组别
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
    cur = conn.cursor()           # 创建游标，以便获得查询对象。
    cur.execute('create table if not exists yundongyuan (id integer  ,name varchar(20) NOT NULL ,haoma int ,zubie varchar(20) NOT NULL) ')  # execute执行sql语句，创建表
    conn.commit()  # COMMIT命令用于把事务所做的修改保存到数据库
    i = 0
    for file in filesy:
        if file.split('.')[-1] == 'txt':
            print(file.split('.')[0])
            # 使用 with 语句来创建文件对象，对象会在with语句结束时自动关闭
            with open('./yundongyuan/'+file,'r',encoding = 'UTF-8') as f: 
                next(f)  # 返回文件下一行
                for line in f:
                    b = list(line.split())
                    i += 1
                    print("插入第", i, "条数据:裁判编号：",b[0],",运动员姓名：",b[1],",运动员编号:",b[2],"运动员组别:",b[3])
                    cur.execute('insert into yundongyuan values(?,?,?,?)',(b[0],b[1],b[2],b[3]))  # ？占位符，即(i,line)
                    conn.commit() 
                      

                  
    cur.close() # 关闭游标
    conn.close() # 关闭数据库连接
    print('运动员数据写入完成！共写入',i,' 条数据')

def create_table_txt2():
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
    cur = conn.cursor()           # 创建游标，以便获得查询对象。
    cur.execute('create table if not exists caipan (id integer  ,name varchar(20) NOT NULL ,zubie varchar(20) NOT NULL ) ')  # execute执行sql语句，创建表
    conn.commit()  # COMMIT命令用于把事务所做的修改保存到数据库
    i = 0
    for file in filesc:
        if file.split('.')[-1] == 'txt':
            print(file.split('.')[0])
            # 使用 with 语句来创建文件对象，对象会在with语句结束时自动关闭
            with open('./caipan/'+file,'r',encoding = 'UTF-8') as f: 
                next(f)  # 返回文件下一行
                for line in f:
                    a = list(line.split())
                    i += 1
                    print("插入第", i, "条数据:裁判编号：",a[0],",裁判姓名：",a[1],",裁判组别:",a[2])
                    cur.execute('insert into caipan values(?,?,?)',(a[0],a[1],a[2]))  # ？占位符，即(i,line)
                    conn.commit()    
                    

                  
    cur.close() # 关闭游标
    conn.close() # 关闭数据库连接
    print('裁判数据写入完成！共写入',i,' 条数据')
    

'''2. 查找表数据'''
def find():  # 查找库有那些表，和数据
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
    cur = conn.cursor()           # 创建游标，以便获得查询对象。
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    Tables=cur.fetchall()
    print("表名：                               ",Tables)

    # 4.查询表中记录
    cur.execute("SELECT * from caipan")
    conn.commit 
    data = cur.fetchall()
    print("裁判[编号,姓名,编号]：               ",data)
    cur.execute("SELECT * from yundongyuan")
    conn.commit 
    data2 = cur.fetchall()
    print("运动员[裁判编号,姓名,编号,组别]：    ",data2)

'''3. 按表名创建表'''
def create_table(event=None):
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
    cur = conn.cursor()           # 创建游标，以便获得查询对象。
    cur.execute('create table if not exists '+e.get()+' (id integer primary key ,number varchar(20) NOT NULL ,haoma varchar(20) NOT NULL) ')  # execute执行sql语句，创建表
    conn.commit()  # COMMIT命令用于把事务所做的修改保存到数据库
    print("已创建",e.get())

'''4.按表名删除表'''
def delete_table(even=None):
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
    cur = conn.cursor()           # 创建游标，以便获得查询对象。
    cur.execute("drop table "+e2.get())
    print("已删除",e2.get())

'''用户自己输入语句'''
def usr_insert(even=None):
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
    cur = conn.cursor()           # 创建游标，以便获得查询对象。
    cur.execute(e3.get())
    data66 = cur.fetchall()
    print("结果为：",data66)
    
##############
'''基本功能一
1.创建数据库
2.(可直接导入txt文件为表) 
2.查找表数据  \/
3.按表名创建表  \/
4.按表名删除表  \/
5.自己输入数据库语句 \/
'''
##############

top = tkinter.Tk()  # 创建窗口对象的背景色
top.title("数据库报名管理系统")
CREATEDB = tkinter.Button(top, text ="创建运动会数据库", command = create_database)
CREATETB1 = tkinter.Button(top, text ="导入运动员txt数据表", command = create_table_txt1)
CREATETB2 = tkinter.Button(top, text ="导入裁判txt数据表", command = create_table_txt2)
FIND = tkinter.Button( text ="查找所有表数据", command = find)
CREATEDB.pack()  # 将小部件放置到主窗口中
CREATETB1.pack()
CREATETB2.pack()
FIND.pack()

# a按表名
e = StringVar()
ll1 = Label(top, text="请输入创建的表名：",font=("华文行楷"), fg="green")
ll1.pack()
entry = Entry(top, validate='key', textvariable=e, width=50)  # 创建
entry.pack()
entry.bind('<Return>', create_table)
#tkinter.Label(entry, text="输入框:")
e2 = StringVar()
ll2 = Label(top, text="请输入删除的表名：",font=("华文行楷"), fg="red")
ll2.pack()
entry2 = Entry(top, validate='key', textvariable=e2, width=50)  # 删除
entry2.pack()
entry2.bind('<Return>', delete_table)

e3 = StringVar()
ll3 = Label(top, text="请输入你自己的sql语句：",font=("华文行楷"), fg="blue")
ll3.pack()
entry2 = Entry(top, validate='key', textvariable=e3, width=50)  # 自己输入语句
entry2.pack()
entry2.bind('<Return>', usr_insert)


creater = tkinter.Label(top, text='作者：马荣皓')
creater.pack()

top.mainloop()  # 进入消息循环
