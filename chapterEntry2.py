from tkinter import *
from math import *

windows = Tk()
windows.title("지홍이에요")

# entry = tk.Entry(windows) #tk.Entry(윈도우창, 기입창의 속성(매개변수) )
entry = Entry(windows)
entry.pack()

entry.insert(0, "Entry")

windows.mainloop()