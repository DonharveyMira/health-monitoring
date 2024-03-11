from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

root = Tk()
root.config(highlightthickness=0, background="#DFEEED")

window_width = 700
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.overrideredirect(True)

sensorLbl = Label(root, text="SENSOR", font=("Microsoft JhengHei", 15, "bold"), 
                 bg="#DFEEED", fg="#497687")
sensorLbl.place(relx=0.5, rely=0.2, anchor=CENTER) 

pr_label = Label(root, text="Pulse Rate", font=("Microsoft JhengHei", 11, "bold"), 
                 bg="#DFEEED", fg="#497687")
pr_label.place(relx=0.08, rely=0.45, anchor=W) 
pr_entry = Entry(root, font=("Microsoft JhengHei", 11), fg="#497687")
pr_entry.place(relx=0.3, rely=0.45, anchor=W) 
bpm_label = Label(root, text="bpm", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#DFEEED", fg="#497687")
bpm_label.place(relx=0.6, rely=0.45, anchor=CENTER) 

bt_label = Label(root, text="Body Temperature", font=("Microsoft JhengHei", 11, "bold"), 
                 bg="#DFEEED", fg="#497687")
bt_label.place(relx=0.08, rely=0.7, anchor=W) 
bt_entry = Entry(root, font=("Microsoft JhengHei", 11), fg="#497687")
bt_entry.place(relx=0.3, rely=0.7, anchor=W) 
cel_label = Label(root, text="°C", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#DFEEED", fg="#497687")
cel_label.place(relx=0.59, rely=0.7, anchor=CENTER) 

btnPulse = Button(root, text="Get Pulse Rate", bg="#497687", fg="#ffffff")
btnPulse.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnPulse.place(relx=0.8, rely=0.45, anchor=CENTER)

btnTemp = Button(root, text="Get Temperature", bg="#497687", fg="#ffffff")
btnTemp.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnTemp.place(relx=0.8, rely=0.7, anchor=CENTER)

root.resizable(False, False)
root.mainloop()
