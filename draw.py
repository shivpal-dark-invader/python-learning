import turtle

def draw_sq():
    window = turtle.getscreen()
    window.bgcolor("red")
    tortuga = turtle.Turtle()

    tortuga.shape("turtle")
    tortuga.color("yellow")
    #tortuga.speed("1")
    
    tortuga.forward(100)
    tortuga.right(90)

    tortuga.forward(100)
    tortuga.right(90)

    tortuga.forward(100)
    tortuga.right(90)

    tortuga.forward(100)
    tortuga.right(90)

    ang = turtle.Turtle()
    ang.shape("turtle")
    ang.color("blue")
    #ang.speed(1)

    ang.circle(100)

    #exitonscreenclick()

draw_sq()
    
