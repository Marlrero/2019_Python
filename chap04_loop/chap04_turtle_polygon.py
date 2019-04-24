import turtle

polygon = turtle.Turtle()

num_sides = 6 # 육각형의 변의 개수
side_length = 70 # 한 변의 길이
angle = 360.0 / num_sides # 육각형의 내각

for i in range(num_sides):
    polygon.forward(side_length) # 한 변의 길이만큼 전진!
    polygon.right(angle) # 각도 변경!

turtle.mainloop()