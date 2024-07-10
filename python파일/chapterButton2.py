import tkinter as tk

windows = tk.Tk()

windows.title("지홍이에요")
windows.geometry("300x300+100+100")
windows.resizable(False, False) #크기를 수정하려고 만든다면 True로 수정하면 됨

count = 0

def countUP():
    global count
    count += 1
    label.config(text=str(count))

def countDOWN():
    global count
    count -= 1
    label.config(text=str(count))

label = tk.Label(windows, text="0", width=10, height=5, fg="red", relief="solid")# 위젯 내용 설정
label.pack()  # 위젯 설정

button1 = tk.Button(windows, overrelief="solid", width=10, command=countUP, repeatdelay=1000, repeatinterval=100)
#command : 버튼이 active 상태
button1.pack()

button2 = tk.Button(windows, overrelief='solid', width=10, command=countDOWN, repeatdelay=1000, repeatinterval=100)
button2.pack()

windows.mainloop()