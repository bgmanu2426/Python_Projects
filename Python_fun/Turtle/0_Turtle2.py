# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
'''import turtle #Outside_In
wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("red")
def sqrfunc(size):
	for i in range(4):
		skk.fd(size)
		skk.left(90)
		size = size-5
sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)'''

# Python program to draw
# Spiral Helix Pattern
# using Turtle Programming
'''import turtle
loadWindow = turtle.Screen()
turtle.speed(2)
for i in range(100):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)
turtle.exitonclick()'''

# Python program to draw
# Rainbow Benzene
# using Turtle Programming
'''import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)'''