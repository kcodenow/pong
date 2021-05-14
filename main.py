from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Arcade Pong')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
s_board = ScoreBoard()

screen.listen()
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')

game_is_live = True
while game_is_live:
	time.sleep(ball.ball_speed)
	screen.update()
	ball.move()

	# collide with top/btm wall
	if ball.ycor()>280 or ball.ycor()<-280:
		ball.bounce_y()

	# detect paddle condition
	if((ball.distance(r_paddle) < 50 and ball.xcor() > 320) 
		or (ball.distance(l_paddle) < 50 and ball.xcor() < -320)):
		ball.bounce_x()
		if(ball.ball_speed > 0):
			ball.ball_speed *=0.9

	# detect misses
	if(ball.xcor() > 340):
		s_board.l_point()
		ball.reset_pos()
	if(ball.xcor() < -340):
		s_board.r_point()
		ball.reset_pos()

screen.exitonclick()