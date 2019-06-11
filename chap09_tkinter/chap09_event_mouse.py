from tkinter import *

def callback(event):
    print(event.x, event.y, "에서 마우스 이벤트 발생")

window = Tk()

frame = Frame(window, width=100, height=100)
frame.bind("<Button-1>", callback) # 마우스 왼쪽 버튼을 클릭하면 callback으로 바인딩
frame.pack()

window.mainloop()