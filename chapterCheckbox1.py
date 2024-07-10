from tkinter import *
from math import *

windows = Tk()
windows.title("지홍이에요")
windows.geometry("600x600")

def flash():
    checkbutton1.flash()

CheckVariety1 = IntVar()
CheckVariety2 = IntVar()
CheckVariety3 = IntVar()

checkbutton1 = Checkbutton(windows, text = "0", variable=CheckVariety1, activebackground='blue')
checkbutton2 = Checkbutton(windows, text = "♬", variable=CheckVariety2)
checkbutton3 = Checkbutton(windows, text = "△", variable=CheckVariety3)

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

windows.mainloop()