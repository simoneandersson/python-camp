import turtle

betty = turtle.Turtle()

# for r in range(2):
    # A
    # betty.forward(100)
    # betty.right(90)
    # betty.forward(100)
    # betty.right(90)

    # B
    # betty.forward(30)
    # betty.right(90)
    # betty.forward(100)
    # betty.right(90)

betty.fillcolor("yellow")
betty.begin_fill()
for r in range(4):

    # C
    betty.forward(50)
    betty.right(45)
    betty.forward(50)
    betty.right(45)

betty.end_fill()

turtle.done()