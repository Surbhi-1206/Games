# Surbhi Saraogi & Sleeping Akshat Mathur
# 14/02/2020
# Copyright

import turtle
import os

game_window = turtle.Screen()
game_window.title("Ping Pong by @Surbhi-1206")
game_window.bgcolor("black")
game_window.setup(width=800, height=600)
game_window.tracer(0)

# Score calculation
score_A = 0
score_B = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.color("red")

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.color("red")

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
game_window.onkey(paddle_a_up, "s")
game_window.onkey(paddle_a_down, "z")
game_window.onkey(paddle_b_up, "Up")
game_window.onkey(paddle_b_down, "Down")
game_window.listen()

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

while True:
    game_window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        os.system("afplay Basso.aiff&")
        pen.write("Player A: {}   Player B: {}".format(score_A, score_B), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        os.system("afplay Basso.aiff&")
        pen.write("Player A: {}   Player B: {}".format(score_A, score_B), align="center",
                  font=("Courier", 24, "normal"))

    if (330 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        os.system("afplay Pop.aiff&")

    if (-330 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        os.system("afplay Pop.aiff&")




