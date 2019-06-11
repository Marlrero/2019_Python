from tkinter import *

def singleLeftButton(event):
    print("한번 왼쪽으로 클릭")

def doubleLeftButton(event):
    print("두번 왼쪽으로 클릭")

def motion(event):
    print("마우스 위치: (%s %s)" % (event.x, event.y))

btn = Button(None, text="마우스 클릭")
btn.pack()

btn.bind("<Button-1>", singleLeftButton)
btn.bind("<Double-1>", doubleLeftButton)
btn.bind("<Motion>", motion)

btn.mainloop() # 버튼에 대한 메인 루프를 설정