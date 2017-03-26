import turtle

def turtle_mp1():
    count = 1

    window = turtle.getscreen()
    window.bgcolor("red")
    pointer = turtle.Turtle()

    def draw():
            

            pointer.shape("turtle")
            pointer.color("yellow")

    
            pointer.forward(100)
            pointer.right(90)
            pointer.forward(100)
            pointer.right(90)
            pointer.forward(100)
            pointer.right(90)
            pointer.forward(100)
            pointer.right(90)

           

    while(count<=36):
        draw()
        pointer.right(10)
        count = count + 1

    pointer.right(90)
    pointer.forward(300)
        

turtle_mp1()
