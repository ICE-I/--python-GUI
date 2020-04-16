'''实现功能
1.根据报名编号查询自己信息
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import * 
import tkinter
import sqlite3      #导入sqlite3
import os
path = os.getcwd()  # 返回当前工作目录



def ydyp():
    EditText.insert(1.0,find3())
def find3(event=None):
    conn = sqlite3.connect(path+'\运动会.db')  # 如果数据库已经存在，则连接数据库；如果数据库不存在，则先创建数据库，再连接该数据库。
    cur = conn.cursor()           # 创建游标，以便获得查询对象。
    cur.execute("SELECT * from yundongyuan WHERE haoma IS "+e5.get())
    conn.commit()
    data = cur.fetchall()
    if data:
        #return ("您已报名成功，信息为：","\r\n",data,"\r\n")
        return ("*"*89,"您已报名成功，裁判编号信息为:",data[0][0],",您的姓名为:",data[0][1],",运动员号码为:",data[0][2],",所在组别为:",data[0][3],"\n")
    else:
        return ("*"*89,e5.get(),"未成功报名，请联系班长进行年级上报.\n")


top = tkinter.Tk()  # 创建窗口对象的背景色
top.title("运动员信息查询")
e5 = StringVar()
ll3 = Label(top, text="请输入你的运动员号码：",font=("华文行楷"), fg="blue")
ll3.pack()
entry4 = Entry(top, validate='key', textvariable=e5, width=50)  # 自己输入语句
entry4.pack()

EditText = Text(top,width=88,height=10)
btn_test=Button(top, text="结果显示按钮", command =ydyp,width=15, height=2)

btn_test.place( x=1100,y=60)
EditText.pack()

creater = tkinter.Label(top, text='作者：马荣皓')
creater.pack()

top.mainloop()  # 进入消息循环
