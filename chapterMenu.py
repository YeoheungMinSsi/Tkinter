from idlelib import window
from tkinter import *
from math import *

windows = Tk()
windows.title("지홍이에요")
windows.geometry("600x600")

def close():
    windows.quit()
    windows.destroy()

menubar = Menu(windows)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="하위 메뉴 1-1")
menu1.add_command(label="하위 메뉴 1-2")
menu1.add_separator()  #메뉴 선택 아래에 선을 긋는 것
menu1.add_command(label="하위 메뉴 1-3", command=close)
menubar.add_cascade(label="상위 메뉴 1", menu=menu1)

menu2 = Menu(menubar, tearoff=0, selectcolor="red")
menu2.add_command(label="하위 메뉴 2-1", state="disable")
menu2.add_command(label="하위 메뉴 2-2")
menu2.add_command(label="하위 메뉴 2-3")
menubar.add_cascade(label="상위 메뉴 2", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="하위 메뉴 3-1")
menu3.add_command(label="하위 메뉴 3-2")
menubar.add_cascade(label="상위 메뉴 3", menu=menu3)

windows.config(menu=menubar)  #윈도우 창에 메뉴 등록

windows.mainloop()

print("Window Close")