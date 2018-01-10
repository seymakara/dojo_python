import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(0)
    brad.color("pink")

    """draws four flowers"""
    for x in range (4):
        for i in range(36):
            brad.forward(100)
            brad.left(175)
        brad.forward(200)
        brad.right(90)

    window.exitonclick()

draw_art()