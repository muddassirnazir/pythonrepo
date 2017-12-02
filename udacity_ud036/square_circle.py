import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("yellow")

    for i in range(1, 37):
        count = 0
        while(count < 4):
            brad.forward(100)
            brad.right(90)
            count = count + 1
        brad.right(10)

    window.exitonclick()

draw_shapes()
