# 사각형을 여러 개 그리기
import turtle

for i in range(3): #사각형을 3개만 그림
    turtle.left(20) #사각형을 그릴 때마다 왼쪽 20도 회전

    #실제 사각형을 그리는 부분
    for i in range(4): #사각형은 4개의 변임
        turtle.forward(50) #사각형의 한 변의 길이는 50
        turtle.left(90) #사각형의 내각은 90

turtle.mainloop()