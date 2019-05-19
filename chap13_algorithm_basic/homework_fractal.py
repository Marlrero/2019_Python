import turtle

def drawTree(branch, t):
    if branch > 5:
        t.forward(branch)         # 전진
        t.right(20)               # 오른쪽으로 20도 회전
        drawTree(branch - 15, t)  # 가지 치기
        t.left(40)                # 왼쪽으로 40도 회전
        drawTree(branch - 15, t)  # 가지 치기
        t.right(20)               # 오른쪽으로 20도 회전
        t.backward(branch)        # 후진

def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    drawTree(100, t)
    window.exitonclick()

main()