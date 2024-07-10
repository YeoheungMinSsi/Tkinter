from tkinter import *
from math import *

windows = Tk()

windows.title("지홍이에요")

def getText():
    label.config(text = "Input : " + entry.get())
    entry.delete(0, len(entry.get()))


# entry = tk.Entry(windows) #tk.Entry(윈도우창, 기입창의 속성(매개변수) )
entry = Entry(windows)
entry.pack()

button = Button(windows, text="클릭", command=getText)
button.pack()

label = Label(windows, text="Input : ")
label.pack()

windows.mainloop()