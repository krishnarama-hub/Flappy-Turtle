from turtle import Screen

from TURTLE import Turtle_body1

from body import piller_Body

from body2 import piller_Body2

from score import Score

import time

screen=Screen()

screen.tracer(0)

turtle=Turtle_body1()

pillar=piller_Body()

pillar2=piller_Body2()

score=Score()

screen.setup(1000,800)

screen.bgcolor("black")

screen.title("FLAPPY BIRD")

screen.listen()

screen.onkey(turtle.Up,"Up")

game_over=True

count1=0

count2=0

count3=0

while game_over:

    screen.update()

    time.sleep(0.1)

    score.update_score()

    turtle.down()

    pillar.pillar_move()

    for p in pillar.store:

        
        if abs(turtle.xcor() - p.xcor()) < 35:

            
            if turtle.ycor() > p.ycor() - 200:
                score.game_over()
                game_over = False

    for p in pillar2.store2:

        
        if abs(turtle.xcor() - p.xcor()) < 35:

            
            if turtle.ycor() < p.ycor() + 200:
                score.game_over()
                game_over = False



    for p in pillar.store:

        if p.xcor()<turtle.xcor() and not p.scored:

            score.increment()

            p.scored=True

    count1+=1

    count3+=1

    if count1==30:

        pillar.pillar_path()

        count1=0

    pillar2.pillar_move2()

    count2+=1

    count3+=1

    if count2==30:

        pillar2.pillar_path2()

        count2=0

    if count3==30:

        pillar.increase()

        pillar2.increase()

  

screen.exitonclick()