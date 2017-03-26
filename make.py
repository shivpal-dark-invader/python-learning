import turtle

def make():
    window = turtle.getscreen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("blue")

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    al = turtle.Turtle()

    al.shape("turtle")
    al.color("yellow")

    al.circle(100)

   # window.onscreenclick(exit)

make()
    
