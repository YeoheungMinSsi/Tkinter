from tkinter import *
from math import *

windows = Tk()
windows.title("지홍이에요")
windows.geometry("600x600")

def check():
    label.config(text = "RadioVariety1 = " + str(RadioVariety1.get()) + "\n" +
                        "RadioVariety2 = " + str(RadioVariety2.get()) + "\n\n" +
                 "Total = " + str(RadioVariety1.get() + RadioVariety2.get()))

RadioVariety1 = IntVar()
RadioVariety2 = IntVar()

radio1 = Radiobutton(windows, text = "1번", value = 3, variable = RadioVariety1, command = check)
radio1.pack()

radio2 = Radiobutton(windows, text = "2번(1번)", value = 6, variable = RadioVariety1, command = check)
radio2.pack()

radio3 = Radiobutton(windows, text = "3번", value = 9, variable = RadioVariety1, command = check)
radio3.pack()

label = Label(windows, text = "None", height = 5)
label.pack()

radio4 = Radiobutton(windows, text = "4번", value = 12, variable = RadioVariety2, command = check)
radio4.pack()

radio5 = Radiobutton(windows, text = "5번", value = 15, variable = RadioVariety2, command = check)
radio5.pack()

windows.mainloop()