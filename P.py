import turtle

my_turtle = turtle.Turtle()
my_turtle.pencolor("red")
def Circle(forward , turn):
    my_turtle.forward(forward)
    my_turtle.right(turn)
    my_turtle.pencolor("green")
    my_turtle.forward(forward)
    my_turtle.right(turn)
    my_turtle.pencolor("red")
    my_turtle.forward(forward)
    my_turtle.right(turn)
    my_turtle.pencolor("green")
    my_turtle.forward(forward)
    my_turtle.right(110)

for i in range(20):
        Circle(100 , 90)


def Circle1(forward , turn):
    my_turtle.pencolor("blue")
    my_turtle.forward(forward)
    my_turtle.right(turn)
    my_turtle.forward(110)
    my_turtle.right(turn)
    my_turtle.forward(forward)
    my_turtle.right(turn)
    my_turtle.forward(forward)
    my_turtle.right(110)

for i in range(20):
        Circle1(150 , 90)
