import tkinter as tk

windows = tk.Tk()

windows.title("지홍이에요")
windows.geometry("300x300")
windows.resizable(False, False) #크기를 수정하려고 만든다면 True로 수정하면 됨

label = tk.Label(windows, text="안녕하세요.") # 위젯 내용 설정
label.pack()  # 위젯 설정

windows.mainloop()