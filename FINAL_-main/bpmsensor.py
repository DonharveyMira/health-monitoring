import tkinter as tk
import tkinter as ttk
import time
import serial
import threading
import continuous_threading
from tkinter import *

ser = serial.Serial('COM3',9600)
val1 = 0

index = []


def readserial():
    global val1
    ser_bytes = ser.readline()
    ser_bytes = ser_bytes.decode("utf-8")
   
    val1 = ser_bytes
    index.append(val1)
    
    if len(index) == 1:
        temp.set(index[0])
       # display1 = Label(root,text=index[0]).place(x=50,y=10)

        temp_entry = Entry(root, textvariable= temp, font=("Microsoft JhengHei", 11), 
                   fg="#497687", width=27)
        temp_entry.place(relx=0.65, rely=0.18, anchor=CENTER) 

    elif len(index) == 2:
        #display1 = tk.Label(root,text=index[0]).place(x=10,y=10)
        #display2 = tk.Label(root,text=index[1]).place(x=90,y=40)
        bpm.set(index[1])

        bpm_entry = Entry(root, textvariable= bpm, font=("Microsoft JhengHei", 11), 
                   fg="#497687", width=27)
        bpm_entry.place(relx=0.65, rely=0.4, anchor=CENTER) 

        
    if len(index) == 2:
        #print("Done")
        index.clear()
    
    time.sleep(0.5)

t1 = continuous_threading.PeriodicThread(0.5, readserial)

root = tk.Tk()
root.geometry("300x250")
temp = StringVar()
bpm = StringVar()
w = tk.Label(root,text="Hum.").place(x=10,y=10)
w1 = tk.Label(root,text="Temp.").place(x=10,y=40)
t1.start()
#t1.join()

root.mainloop()
