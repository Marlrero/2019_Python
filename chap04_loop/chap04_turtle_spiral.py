# turtle 객체의 stamp 함수를 사용해 터틀의 위치를 출력

import turtle

window = turtle.Screen() #화면 객체
window.bgcolor("lightgreen") #화면 객체의 배경색

t = turtle.Turtle() #터틀 객체
t.shape("turtle") #터틀 객체 모양
t.color("blue") #터틀 객체 색상

size = 20 #초기 터틀이 나아갈 픽셀
for i in range(30): #30번 반복
    t.stamp() #터틀의 위치를 찍어보기!
    size = size + 3
    t.forward(size)
    t.right(24)

turtle.mainloop()