from tkinter import *
from math import *

windows = Tk()

windows.title("지홍이에요")
windows.geometry("300x300+100+100")
windows.resizable(False, False) #크기를 수정하려고 만든다면 True로 수정하면 됨

def calc():
    label.config(text="결과="+str(eval(entry.get())))

# entry = tk.Entry(windows) #tk.Entry(윈도우창, 기입창의 속성(매개변수) )
entry = Entry(windows)
entry.pack()

button = Button(windows, text="클릭", command=calc)
button.pack()

label = Label(windows)
label.pack()

windows.mainloop()