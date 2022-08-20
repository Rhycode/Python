import turtle as tu
screen = tu.Screen()
screen.setup(500, 600, startx=0, starty=100)
t = tu.Turtle()
tu.bgcolor('black')
tu.color('yellow')
tu.speed(11)
tu.right(45)

for i in range(150):
    tu.circle(25)
    if 7 < i < 62:
        tu.left(5)
    if 80 < i < 133:
        tu.right(5)
    if i < 80:
        tu.forward(10)
    else:
        tu.forward(5)

tu.done()

