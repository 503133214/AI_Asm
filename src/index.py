__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

import tkinter as tk

root = tk.Tk()  # 生成主窗口
root.title("Face classroom check-in system")  # 窗体名称
root.geometry("490x390")  # 指定窗体大小

label = tk.Label(root, text="Welcome to use the face classroom check-in system")
name_key = tk.Entry(root, show=None, font=('Arial', 14))

name = str  # 全局变量


def get_name():
    global name
    name = name_key.get()
    print(name)  # 打印名字以检查是否正确获取


button1 = tk.Button(root, text="Name", command=get_name)
button1.place(x=390, y=0)
name_key.pack()
label.pack()

root.mainloop()
