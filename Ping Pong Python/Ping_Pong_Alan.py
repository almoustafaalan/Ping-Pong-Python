# Ping Pong using turtle
# Author: Alan 

import turtle

# --- Screen setup ---
wn = turtle.Screen()
wn.title("Ping Pong by Alan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# --- Paddle ---
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("red")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# --- Ball ---
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# --- Score ---
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: 0", align="center", font=("Courier", 18, "normal"))

# --- Paddle movement ---
def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -350:
        x = -350
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 350:
        x = 350
    paddle.setx(x)

# --- Keyboard bindings ---
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")

# --- Main game loop ---
def game_loop():
    global score
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border collision
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    elif ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy = 4
        score = 0
        score_pen.clear()
        score_pen.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))
    
    # Paddle collision
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240)
        ball.dy *= -1
        score += 1
        score_pen.clear()
        score_pen.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))
    
    wn.update()
    wn.ontimer(game_loop, 20)  # calls game_loop every 20ms

# Start the game
game_loop()
wn.mainloop()
