# This is a sample Python desktop game.
###main is graphics ui game.py is game logic
# https://softuni.bg/trainings/resources/video/54536/video-12-october-2020-jordan-jambazov-python-advanced-september-2020/3013
###

import turtle
import game
import time

STAMP_SIZE = 20
sleep_time = 0.01

game = game.Game()
screen = turtle.Screen()
screen._root.resizable(False, False)
screen.title("Pong")
screen.bgcolor('black')
screen.setup(game.width, game.height)
# screen.mainloop() # refresh update screen from turtle events
screen.tracer(0) # stop this update

# pose the ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

# pose the paddle A
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(game.paddle_height / STAMP_SIZE, game.paddle_width / STAMP_SIZE)
paddle_a.penup()

# pose the paddle B
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(game.paddle_height / STAMP_SIZE, game.paddle_width / STAMP_SIZE)
paddle_b.penup()


# Text
text = turtle.Turtle()
text.color('white')
text.penup()
text.goto(0, game.height / 2 - 50)
text.hideturtle()


def player_a_up():
    game.paddle_a_up()


def player_a_down():
    game.paddle_a_down()


def player_b_up():
    game.paddle_b_up()


def player_b_down():
    game.paddle_b_down()


# Focus on screen to collect events from keyboard events
screen.listen()
screen.onkeypress(player_a_up, 'w')
screen.onkeypress(player_a_down, 's')
screen.onkeypress(player_b_up, 'Up')
screen.onkeypress(player_b_down, 'Down')

prev_points_a = None
prev_points_b = None

while True:
    game.tick()
    ball.goto(game.ball_pos())
    paddle_a.goto(game.paddle_a_pos)
    paddle_b.goto(game.paddle_b_pos)
    if prev_points_a != game.points_a or prev_points_b != game.points_b:
        text.clear()
        text.write(f'Player A: {game.points_a}  -  Player B: {game.points_b}', align='center', font=('Courier', 12, 'normal'))
        prev_points_a = game.points_a
        prev_points_b = game.points_b
    # Text Game over at the end of the game
    if game.game_over:
        finished = turtle.Turtle()
        finished.penup()
        finished.color('red')
        finished.goto(0, 0)
        finished.hideturtle()
        finished.write("Game over!", align='center', font=('Courier', 20, 'normal'))
        finished.showturtle()
        already_finished = True
    screen.update()
    time.sleep(0.01)






