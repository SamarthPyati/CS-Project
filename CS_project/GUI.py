
from tkinter import *

# def tell():
#     print('!!!!!')

# count = 0 
# def counter():
#     global count 
#     count += 1
#     print(count)

# ---------------- Button ----------------

# root = Tk()
# root.title('GUI') 
# button1 = Button(
#                 root, 
#                 text='Button', 
#                 command=tell,
#                 font = ('Source Code Pro', 30),
#                 fg="#00FF00",
#                 bg='yellow',
#                 activebackground="blue",
#                 state=ACTIVE,
#                 # image=photo,
#                 compound='bottom'
#                 )
# def clcik():
#     print('#####')

# button2 = Button(
#                 root, 
#                 text='Button', 
#                 command=counter,
#                 font = ('Source Code Pro', 30),
#                 fg="#00FF00",
#                 bg='blue',
#                 # image=photo,
#                 activebackground="yellow",
#                 state=ACTIVE,
#                 compound='top'
#                 )

# button1.pack()
# button2.pack()

# root.mainloop()

# ---------------- Entry ----------------

window = Tk()
window.title('LOGIN')
window.geometry('400x400')

username = Entry(
    window, 
    font=("Arial",20),
    fg = 'pink',
    
)
username.pack(side=LEFT)

password = Entry(
    window, 
    font=("Arial",20),
    fg = 'blue',
    bg = 'pink',
)
password.pack(side=LEFT)


dict = {}
def submit():
    user = username.get()
    passw = password.get()
    dict[user] = passw
    print(dict)

submit_button = Button(
    window, 
    text='SUBMIT',
    command=submit,
    fg = 'pink',
    compound='right',
    height=3,
    width=10
)
submit_button.pack(side=RIGHT)



window.mainloop()