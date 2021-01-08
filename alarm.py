from tkinter import *
from tkinter import messagebox
import os
from time import strftime
# from playsound import playsound

def show_time():
    global clock_lbl,logged_time
    current_time = strftime("%H:%M:%S")
    clock_lbl.config(text=current_time)

    if os.path.exists(log_file):
        with open(log_file,"r") as f:
            logged_time = str(f.readline())

    if current_time == logged_time:
        messagebox.showinfo("Success Alert","Your Alarm Time is Comming..")
        # playsound("horror_howl.mp3")
        os.startfile("D://Web Development and Programming Language//Python Programs//Python Projects//Alarm Clock with GUI//horror_howl.mp3")

    clock_lbl.after(1000,show_time)


def set_alarm():
    time = inp1.get()
    time= str(time)
    if (len(time) == 0):
        messagebox.showwarning("Warning | Alarm Clock","Please enter some input in input field")

    if (len(time) > 0):
        if (":" not in time) and (":".__len__() != 2):
            messagebox.showwarning("Warning","Please use this format in time\nFormat:- 13:00:00")
        
        else:
            hour,minute,seconds = time.split(':')
            alarm_time = f"{hour}:{minute}:{seconds}"
            with open(log_file,"w+") as f:
                f.write(alarm_time)

            messagebox.showinfo("Success | Alarm Clock",f"Your Alarm is set for that Time: {hour}:{minute}:{seconds} ")
            inp1.delete(0,END)
            # inp2.delete(0,END)


if __name__ == "__main__":
    log_file = "alarm_logs.txt"
    logged_time = ""
    alarm = Tk()
    alarm.geometry("720x500+300+15")
    alarm.iconbitmap("alarm.ico")
    alarm.title("Alarm Clock | Python Project")
    alarm.minsize(720,500)
    alarm.maxsize(720,500)
    alarm.configure(background="#696969")

    clock_lbl = Label(alarm,font="sans-serif 20 bold",bg="#50525D",fg="white")
    clock_lbl.place(width=275,height=65,x=250)
    show_time()

    # Set LabelFrame
    lbl_frm = LabelFrame(alarm,bg="#50525D",bd=2,relief=SOLID)
    lbl_frm.place(width=525,height=200,x=100,y=150,bordermode=OUTSIDE)

    lbl1 = Label(lbl_frm,fg="white",text=f"  Time (Ex:12:59:59) :-  ",font="sans-serif 15 bold",bg="#50525D",relief=GROOVE)
    lbl1.place(x=30,y=30,bordermode=OUTSIDE)

    inp1 = Entry(lbl_frm,fg="black",bg="white",font="sans-serif 17 bold")
    inp1.place(x=340,y=33,width=150,height=23)

    # lbl2 = Label(lbl_frm,fg="white",text="",font="sans-serif 15 bold",bg="#50525D",relief=GROOVE)
    # lbl2.place(x=30,y=73,bordermode=OUTSIDE)

    btn1 = Button(lbl_frm,text="Set Alarm",bg="#696969",font="sans-serif 20 bold",fg="white",command=set_alarm)
    btn1.place(x=200,y=130,width=150,height=40)
    alarm.mainloop()