# turtle을 이용한 cos 그래프 그리기

import math
import turtle

t = turtle.Turtle()

#x축 그리기
t.pendown()
for x in range(360): #360까지 그림
    t.goto(x, 0)
t.penup()

#y축 그리기
t.pendown()
for y in range((int)(math.cos(math.radians(0)) * 100)): #cos 그래프는 0도에서 최댓값
    t.goto(0, y)
t.penup()

#y축을 그리면, cos 그래프의 45도 최댓값까지 터틀이 찍으므로 그대로 이어서 그릴 수 있음!

t.pendown() #터틀 객체의 펜을 내림
for angle in range(360): # sin 그래프는 각도에 따라 변함
    y = math.cos(math.radians(angle)) # sin 값을 계산

    scaledX = angle # x축의 좌표값을 각도로 함
    scaledY = y * 100 #y축의 좌표값을 sin 값으로 함 (단, 표현하기에 작으므로 100을 곱함)
    t.goto(scaledX, scaledY) #터틀 객체를 좌표로 이동함

t.penup() #터틀 객체의 펜을 올림

turtle.mainloop()