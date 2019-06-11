# 랜덤한 사각형 그리기
from tkinter import *
import random
# 난수 관련 모듈 import

window = Tk()
canvas = Canvas(window, width=500, height=400)
canvas.pack()

color = [ "red", "orange", "yellow", "green", "blue", "violet" ]

def draw_rect():
    x = random.randint(0, 500) # [0, 500] 구간에서 난수 발생
    y = random.randint(0, 400)
    width = random.randrange(100) # [0, 100) 구간에서 난수 발생
    height = random.randrange(100)

    canvas.create_rectangle(x, y, width, height, fill=random.choice(color))
    # choice 함수는 리스트나 튜플에서 하나를 무작위로 고름

for i in range(10): # 10개의 사각형 무작위 생성
    draw_rect()

window.mainloop()