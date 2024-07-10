from idlelib import window
from tkinter import *
from math import *

windows = Tk()
windows.title("지홍이에요")
windows.geometry("600x600")

menubutton = Menubutton(windows, text = "메뉴 메뉴 버튼", relief = "raised", direction = "right")
#direction은 메뉴가 나타나는 방향
menubutton.pack()

menu = Menu(menubutton, tearoff = 0)  # tearoff는 하위메뉴의 분리 기능 사용 유/무
menu.add_command(label = "하위메뉴1")
menu.add_separator()
menu.add_command(label = "하위메뉴2")
menu.add_command(label = "하위메뉴3")

menubutton["menu"] = menu

windows.mainloop()
