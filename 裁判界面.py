'''实现功能
1.根据裁判编号查找自己报名信息
2.根据组别产生运动员秩序册
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import * 
import tkinter
import sqlite3      #导入sqlite3
import os
path = os.getcwd()  # 返回当前工作目录

#***************************************************************************************#
#添加功能：生成秩序册
#***************************************************************************************#

def pp():
    EditText.insert(1.0,find2())
def find2(event=None):
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
    cur = conn.cursor()           # 创建游标，以便获得查询对象。
    cur.execute("SELECT * from caipan WHERE id IS "+e4.get())
    conn.commit()
    data = cur.fetchall()
    if data:
        #return ("您已报名成功，报名信息为：", "\r\n", data, "\r\n")
        return ("*"*70,"您已报名成功，裁判编号为:",data[0][0],",您的姓名为:",data[0][1],",所在组别为:",data[0][2],"。\n")
    else:
        return ("*"*70,e4.get(),"未成功报名，请联系管理员进行上报。\n")

def pp2():
    EditText2.insert(1.0,baobiao())
def baobiao(event=None):
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
    cur = conn.cursor()           # 创建游标，以便获得查询对象。
    cur.execute("SELECT * from yundongyuan WHERE zubie IS "+"'"+e5.get()+"'")
    conn.commit()
    data2 = cur.fetchall()
    if data2:
        return(e5.get(),"组运动员信息秩序册：","\r\n", data2, "\r\n")
    else:
        return("无此项目运动员信息，请检查输入组别")



    

top = tkinter.Tk()  # 创建窗口对象的背景色
top.title("裁判信息查询")
e4 = StringVar()
ll3 = Label(top, text="请输入你的裁判编号：",font=("华文行楷"), fg="blue")
ll3.pack()
entry4 = Entry(top, validate='key', textvariable=e4, width=50)  # 自己输入语句
entry4.pack()

EditText = tk.Text(top,width=70,height=10)
btn_test=tk.Button(top, text="结果显示按钮", command =pp,width=15, height=2)

btn_test.place( x=1050,y=60)
EditText.pack()
########################################################

e5 = StringVar()
ll4 = Label(top, text="请输入运动组别,生成秩序册：",font=("华文行楷"), fg="blue")
ll4.pack()
entry5 = Entry(top, validate='key', textvariable=e5, width=50)  # 自己输入语句
entry5.pack()

EditText2 = tk.Text(top,width=40,height=10)
btn_test2=tk.Button(top, text="结果显示按钮", command =pp2,width=15, height=2)

btn_test2.place( x=1000,y=240)
EditText2.pack()

creater = tkinter.Label(top, text='作者：马荣皓')
creater.pack()

top.mainloop()  # 进入消息循环
