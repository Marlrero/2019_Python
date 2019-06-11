import time # 시간 관련 함수 사용
from tkinter import *

window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()

oval = canvas.create_oval(10, 100, 50, 150, fill="green")

for i in range(100):
    canvas.move(oval, 3, 0) # x좌표로 3만큼 이동
    window.update() # 화면을 다시 그리라는 의미
    time.sleep(0.05) # 0.05초 실행 지연
