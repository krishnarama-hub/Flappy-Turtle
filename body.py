from turtle import Turtle

import random

class piller_Body:

    def __init__(self):

        self.store=[]

        self.speed=7

    def pillar_path(self):

        gap=random.randint(-130,120)

        tim=Turtle()

        tim.backward(10)

        tim.shape("square")

        tim.color("green")

        tim.penup()

        tim.shapesize(stretch_len=3,stretch_wid=20)

        tim.goto(500,360+gap)

        tim.scored=False

        self.store.append(tim)


    def pillar_move(self):

            for p in self.store:

                p.backward(self.speed)


    def increase(self):

         self.speed+=10





        