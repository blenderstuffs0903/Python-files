from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color('coral')
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight())
my_screen.exitonclick()
