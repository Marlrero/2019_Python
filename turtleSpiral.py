import turtle

turtle.shape("turtle")

size = 20
for i in range(30):
    size = size + 3
    turtle.forward(size)
    turtle.right(24)

turtle.mainloop()