from tkinter import *

window = Tk()

# 키보드 이벤트는 현재 키보드 포커스를 소유하고 있는 위젯으로 보내짐!
# focus_set 메소드로 원하는 위젯으로 포커스 이동 가능

def key(event):
    print(repr(event.char), "가 눌렀습니다.") # repr은 문자코드를 문자열로 변환하는 함수임

def mouse(event):
    frame.focus_set() # 포커스 설정
    print(event.x, event.y, "에서 마우스 이벤트 발생")

frame = Frame(window, width=100, height=100)
frame.bind("<Key>", key) # 키 이벤트에 대해 key 바인딩
frame.bind("<Button-1>", mouse)
frame.pack()

window.mainloop()