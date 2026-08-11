from turtle import Turtle

class Score(Turtle):

    def __init__(self):

        super().__init__()

        self.color("white")

        self.penup()

        self.score=0

        self.high=0

        self.hideturtle()

        self.goto(0,350)

    def update_score(self):

        self.clear()

        self.write(f"Score:{self.score}",align="left",font=("Arival",20,"normal"))
        
    def increment(self):

        self.score+=1

        self.update_score()

    def game_over(self):

        self.color("white")

        self.penup()

        self.hideturtle()

        self.goto(0,0)

        self.write("Game Over",align="center",font=("Arival",30,"normal"))       