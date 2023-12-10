__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
from read_data import read_name_list
import read_camera as rc
import face_collect as fc
import os
import pick_face as pf
import train_model as tm

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('Face classroom check-in system by saber')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('400x300')  # 这里的乘是小x

# 第4步，加载 wellcome image
canvas = tk.Canvas(window, width=400, height=135, bg='white')
image_file = tk.PhotoImage(file='../img/bg1.png')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='Wellcome', font=('Arial', 16)).pack()

# 第5步，用户信息
tk.Label(window, text='Name:', font=('Arial', 14)).place(x=10, y=170)

# 第6步，用户登录输入框entry
# Name
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=175)

# 读取现有的姓名列表
name_list = read_name_list('../img/picTest')


# 第8步，定义用户登录功能
def usr_login():
    # 这行代码就是获取用户输入的usr_name
    usr_name = var_usr_name.get()

    # 如果用户名与文件中的匹配成功，则会登录成功，并跳出弹窗how are you? 加上你的用户名。
    if usr_name in name_list:
        camera = rc.Camera_reader()
        result = camera.build_camera()
        if result == usr_name:
            tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tkinter.messagebox.showerror(message='Error, your face does not match your name!')
    else:  # 如果发现用户名不存在
        is_sign_up = tkinter.messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
        # 提示需不需要注册新用户
        if is_sign_up:
            usr_sign_up()


# 第9步，定义用户注册功能
def usr_sign_up():
    def sign_to_Hongwei_Website():
        # 我们注册时所输入的信息
        nn = new_name.get()

        # 如果用户名已经在我们的list中，则提示Error, The user has already signed up!
        if nn in name_list:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')

        # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
        else:
            directory = "../img/source-saber"
            if not os.path.exists(directory + os.sep + nn):
                os.makedirs(directory + os.sep + nn)
            fc.take_photo(directory + os.sep + nn)
            name_list.append(nn)
            destination = "../img/picTest"
            pf.readPicSaveFace_Path(directory, destination, '.jpg', '.JPG', 'png', 'PNG')
            tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # 然后销毁窗口。
            window_sign_up.destroy()

    # def pick():
    #     directory = "../img/dataset"
    #     destination = "../img/picTest"
    #     pf.readPicSaveFace_Path(directory, destination, '.jpg', '.JPG', 'png', 'PNG')
    #     tkinter.messagebox.showinfo('Welcome', 'You have successfully picked up!')
    #     window_sign_up.destroy()
    def train():
        tm.train()
        tkinter.messagebox.showinfo('Welcome', 'You have successfully trained!')
        window_sign_up.destroy()
    # 定义长在窗口上的窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    # 下面的 sign_to_Hongwei_Website
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Hongwei_Website)
    btn_comfirm_sign_up.place(x=80, y=120)

    btn_comfirm_train = tk.Button(window_sign_up, text='Train', command=train)
    btn_comfirm_train.place(x=210, y=120)


# 第7步，login and sign up 按钮
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=60, y=240)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=200, y=240)

# 第10步，主窗口循环显示
window.mainloop()
