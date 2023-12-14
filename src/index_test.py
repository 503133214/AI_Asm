__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

import tkinter as tk  # Import Tkinter 
import tkinter.messagebox
from read_data import read_name_list
import read_camera as rc
import face_collect as fc
import os
import pick_face as pf
import train_model as tm

# Step 1: Instantiate the object and create the window window
window = tk.Tk()

# Step 2: Name the window's visualization
window.title('Face check-in system')

# Step 3: Set the size of the window (length * width)
window.geometry('400x300')  # The multiplication here is the small x

# Step 4: Load the wellcome image
canvas = tk.Canvas(window, width=400, height=135, bg='white')
image_file = tk.PhotoImage(file='../img/bg1.png')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='Wellcome', font=('Arial', 16)).pack()

# Step 5, User information
tk.Label(window, text='Name:', font=('Arial', 14)).place(x=10, y=170)

# Step 6, user login input box entries
# Name
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=175)

# Retrieve an existing list of names
name_list = read_name_list('../img/picTest')


# Step 8: Define the user login function
def usr_login():
    # Get the usr_name entered by the user
    usr_name = var_usr_name.get()

    # If the username matches the one in the file, you will be logged in successfully and a popup window how are you? with your username will appear.
    if usr_name in name_list:
        camera = rc.Camera_reader()
        result = camera.build_camera()
        if result == usr_name:
            tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tkinter.messagebox.showerror(message='Error, your face does not match your name!')
    else:  # If find that the username does not exist
        is_sign_up = tkinter.messagebox.askyesno('Welcome!', 'You have not sign up yet. Sign up now?')
        # TipNeed to register a new user
        if is_sign_up:
            display_sign_up()


# Step 9: Define the user registration function
def display_sign_up():
    def sign_up():
        # The information we entered when we registered
        nn = new_name.get()

        # If the username is already in our list, Error, The user has already signed up!
        if nn in name_list:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')

        # Finally, if there are no errors in the input, the information entered in the registration will be recorded in the file, and prompted to register successfully Welcome!
        else:
            directory = "../img/source"
            if not os.path.exists(directory + os.sep + nn):
                os.makedirs(directory + os.sep + nn)
            fc.take_photo(directory + os.sep + nn)
            name_list.append(nn)
            destination = "../img/picTest"
            pf.readPicSaveFace_Path(directory, destination, '.jpg', '.JPG', '.png', '.PNG')
            tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # Destroy the window.
            window_sign_up.destroy()

    def train():
        tm.train()
        tkinter.messagebox.showinfo('Welcome', 'You have successfully trained!')
        window_sign_up.destroy()
    # Define windows that are long on windows
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()  # Assigns the entered registration name to the variable
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # Place `User name:` at coordinates (10,10).
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # Create an `entry` with a registered name and a variable `new_name`.
    entry_new_name.place(x=130, y=10)  # `entry` is placed at coordinates (150,10).

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_up)
    btn_comfirm_sign_up.place(x=80, y=120)

    btn_comfirm_train = tk.Button(window_sign_up, text='Train', command=train)
    btn_comfirm_train.place(x=210, y=120)


# Step 7,login and sign up botton
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=60, y=240)
btn_sign_up = tk.Button(window, text='Sign up', command=display_sign_up)
btn_sign_up.place(x=200, y=240)

# Step 10, main window cyclic display
window.mainloop()
