from turtle import Turtle

class Turtle_body1(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("turtle")

        self.color("yellow")

        self.penup()

        self.shapesize(stretch_len=1,stretch_wid=1)

        self.goto(-480,0)

    def Up(self):

        self.goto(self.xcor(),self.ycor()+40)

    def down(self):

        self.goto(self.xcor(),self.ycor()-10)