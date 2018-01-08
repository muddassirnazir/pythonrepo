import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("yellow")
    count = 0
    while(count < 4):
        brad.forward(100)
        brad.right(90)
        count = count + 1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    maggie = turtle.Turtle()
    maggie.shape("arrow")
    maggie.color("green")
    count = 0
    while (count < 3):
        maggie.back(60)
        maggie.left(120)
        count = count + 1

draw_shapes()
