from tkinter import *
from math import *

windows = Tk()
windows.title("지홍이에요")
windows.geometry("600x600")

listbox = Listbox(windows, selectmode='extended', height=0)

listbox.insert(0, '1번')
listbox.insert(1, '2번')
listbox.insert(2, '3번')
listbox.insert(3, '4번')
listbox.insert(4, '5번')
listbox.insert(5, '6번')

listbox.delete(2, 3)  #(first, last) first 자리부터 last자리까지 삭제함

listbox.pack()

windows.mainloop()