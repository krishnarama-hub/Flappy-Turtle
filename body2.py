from turtle import Turtle

import random

class piller_Body2:

    def __init__(self):

        self.store2=[]

        self.speed2=7

    def pillar_path2(self):

        gap=random.randint(-130,120)

        tim=Turtle()

        tim.backward(10)

        tim.shape("square")

        tim.color("green")

        tim.penup()

        tim.shapesize(stretch_len=3,stretch_wid=20)

        tim.goto(500,-380+gap)

        tim.scored=False

        self.store2.append(tim)


    def pillar_move2(self):

            for p in self.store2:

                p.backward(self.speed2)

    def increase(self):

         self.speed2+=10
