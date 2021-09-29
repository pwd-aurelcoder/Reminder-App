from tkinter import *

from tkinter import messagebox

from ttkthemes import themed_tk as tk

from tkinter import ttk

import time

icon = 'icon.ico'
resulution = '270x270'

print('Prisni nje moment.')
print('User name: \"user\"')
print('Password: \"user\"')
print('Nese deshironi ta ndryshoni hyni ne file-in e codit')
time.sleep(2)

#NESE DESHIRONI TE NDRYSHONI USERNAME DHE PASSWORD:
usrname = 'user'
passtext = 'user'

root = tk.ThemedTk()
root.get_themes()
root.set_theme('breeze')
root.title('Remind me v1.1')
root.resizable(False, False)
root.iconbitmap(icon)
root.geometry(resulution)

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)

def raise_frame(frame):
    frame.tkraise()


for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')
else:

    def log_in():
        name = user_name.get()
        password = user_password.get()
        if password == passtext:
            if name == usrname:
                messagebox.showinfo(title='Log in succesed', message='Loged in')
                raise_frame(f2)
            else:
                messagebox.showerror(title='Log in error', message='Incorrect name')
        else:
            messagebox.showerror(title='Log in error', message='Incorrect password')


    def delete():
        file = open('file.txt', 'w')
        file.write('')
        a.delete('0', END)


    def save():
        remind = reminder.get('1.0', 'end-1c')
        file = open('file.txt', 'a')
        file.write(remind + '\n')


    def load():
        global a
        raise_frame(f3)
        a = Listbox(f3, height=10, width=40, font=('calibri', 11))
        a.pack()
        with open('file.txt', 'r') as file:
            for f in file:
                a.insert(END, f.strip())

        ttk.Button(f3, text='Delete all', command=delete).pack()
        ttk.Button(f3, text='Exit', command=(root.quit)).pack()


    Label(f1).pack()
    Label(f1).pack()
    ttk.Label(f1, text='Enter your name:').pack()
    user_name = ttk.Entry(f1)
    user_name.pack()
    Label(f1).pack()
    ttk.Label(f1, text='Enter your password:').pack()
    user_password = ttk.Entry(f1, show='*')
    user_password.pack()
    Label(f1).pack()
    ttk.Button(f1, text='Log in', command=log_in, cursor='hand2').pack()
    ttk.Label(f1, text=':').pack()
    ttk.Label(f1, text='Author: Aurel Vogli').pack(side='left')
    reminder = Text(f2, font=('calibri', 15), width=27, height=8.4)
    reminder.pack()
    ttk.Button(f2, text='Save reminder', command=save).pack()
    ttk.Button(f2, text='Load reminder', command=load).pack()
    raise_frame(f1)
    root.mainloop()
