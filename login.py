from tkinter import *
from tkinter import Tk
from tkinter import messagebox
#credentials
credentials = ['balaji', '12345']
def check_password():
    name = e_name.get()
    password = str(e_password.get())

    if name == 'admin' and password == 'admin':
        messagebox.showinfo('Login', 'Welcome Admin!')

    elif name == credentials[0] and password == credentials[1]:
        messagebox.showinfo('Login', 'Welcome Back ' + credentials[0])
    else:
        messagebox.showwarning('Error', 'Check Username or Password')





def check_password():
    name = e_name.get()
    password = str(e_password.get())

    if name == 'admin' and password == 'admin':
        messagebox.showinfo('Login', 'Welcome Admin!')

    elif name == credentials[0] and password == credentials[1]:
        messagebox.showinfo('Login', 'Welcome Back ' + credentials[0])

        for widget in frame_down.winfo_children():
            widget.destroy()

        for widget in frame_down.winfo_children():
            widget.destroy()
        
        new_window()
    else:
        messagebox.showwarning('Error', 'Invalid username or password')

def new_window():

    username = Label(frame_down, text="username *", height=1, anchor=NW, bg=co1, fg=co2, font=('Poppins 12'))
    username.place(x=10, y=10)

    username = Label(frame_down, text="welcome " + credentials[0], height=1, anchor=NW, bg=co1, fg=co2, font=('Poppins 12'))
    username.place(x=10, y=10)
#colors
co1 = "white"
co2 = "black"
co3 = "#6074FF"

window = Tk()
window.title("work")



# frames
frame_up = Frame(window, width=310, height=50, bg=co1)
frame_up.grid(row=0, column=0)

frame_down = Frame(window, width=310, height=300, bg=co1)
frame_down.grid(row=1, column=0)
# frame_up widgets

heading = Label(frame_up, text = "LOGIN", bg = co1, font=('Poppins 23'))
heading.place(x=5, y=5)

line = Label(frame_up, width=40, text="", height=1, bg=co3, anchor=NW)
line.place(x=10, y=45)

# frame_down widgets

username = Label(frame_down, text="username *", height=1, anchor=NW, bg=co1, fg=co2, font=('Poppins 12'))
username.place(x=10, y=10)

e_name = Entry(frame_down, width=25, justify='left', font=("", 15), highlightthickness=1)
e_name.place(x=14, y=48)

password = Label(frame_down, text="password *", height=1, anchor=NW, bg=co1, fg=co2, font=('Poppins 12'))
password.place(x=10, y=95)

e_password = Entry(frame_down, width=25, justify='left',show = '*', font=("", 15), highlightthickness=1)
e_password.place(x=14, y=130)

#button

button_confirm = Button(frame_down, text="Login", bg=co3, fg=co1, width=39, height=2, font=("Ivy 9 bold"))
button_confirm.place(x=15, y=180)

#button

button_confirm = Button(frame_down, text="Login", bg=co3, fg=co1, width=39, height=2, font=("Ivy 9 bold"), command=check_password)
button_confirm.place(x=15, y=180)


window.geometry('310x300')

window.configure(bg=co1)

window.mainloop()