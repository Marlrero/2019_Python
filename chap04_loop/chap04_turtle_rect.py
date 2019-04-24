import turtle

window = turtle.Screen() #화면 객체
window.bgcolor("lightgreen") #배경색 지정

t = turtle.Turtle() #터틀 객체
t.shape("turtle") #터틀 모양
t.color("blue") #터틀 색상

colors = ["yellow", "red", "purple", "blue"]

for c in colors:
    t.color(c) #터틀 색상 변경
    t.forward(200) #픽셀만큼 전진
    t.left(90) #왼쪽으로 각도만큼 회전

turtle.mainloop()