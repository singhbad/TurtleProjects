from turtle import Turtle, Screen

class TurtleDesign():

    # timmy_the_turtle = Turtle()
    # timmy_the_turtle.shape("turtle")
    # timmy_the_turtle.color("brown")

    def TurtleDes(Direction, Angle):
        timmy_the_turtle = Turtle()
        timmy_the_turtle.shape("turtle")
        timmy_the_turtle.color("brown")
        for times in range(4):
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(90)


Direction = input("Provide the distance you want to cover ")
Angle = input("Provide the Angle you want to turn the turtle")
TurtleDesign.TurtleDes(Direction, Angle)

















screen = Screen()
screen.exitonclick()
