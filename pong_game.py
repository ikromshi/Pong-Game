from scoreboard import Scoreboard
from paddle import Paddle
from turtle import Screen
from ball import Ball
import game_art as gm
import keyboard
import random

# Printing the introduction
print(gm.art)
print("WELCOME TO THE GAME OF PONG\n\n The rules are simple:\n"
      "* To move the paddles up and down, players should press the keys \"w\", \"s\" and the arrows \"UP\", \"DOWN\","
      "respectively \n"
      "* To quit the game press the \"Esc\" key")

name1 = input("\nEnter the first player's name (they will play on the left): ")
name2 = input("Enter the second player's name (they will play on the right): ")
print(f"THE GAME IS ON! SWITCH THE WINDOWS\n\n\t\t{gm.luck}\n\n")

# Running the screen and displaying the players on it
screen = Screen()
scoreboard = Scoreboard(name1, name2)


def colors():
    """Changes the background color every time the ball hits a wall"""

    colors_list = ["#458B74", "#9C661F", "#A52A2A", "#EEC591", 	"#CDC9A5", "#EEA2AD",
                   "#458B00", "#FF7256", "#9932CC", "#8FBC8F", "#EEB422", 	"#607B8B",
                   "#8470FF", "#CDCD00"]
    rand_color = random.choice(colors_list)
    return rand_color


# Setting up the screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game by Ikrom Numonov")
screen.tracer(0)

# Positioning the paddles
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
l_paddle.color("blue")
r_paddle.color("blue")

# Connecting keys to "UP", "DOWN" functions
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

# Setting up the ball
ball = Ball()
ball.color("white")
game_is_on = True

# Makes sure the game doesn't start before the player is ready
while not keyboard.is_pressed("enter"):
    scoreboard.write_start()
scoreboard.update_scores()

while game_is_on:
    screen.update()
    ball.move_ball()

    # Detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        ball.change_color(1)
        random_color = colors()
        screen.bgcolor(random_color)

    # Detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        ball.change_color(1)

    # Detect collision with the left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.change_color(1)

    # Detects if the ball goes out of bounds Right Player
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detects if the ball goes out of bounds Left Player
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

    if keyboard.is_pressed("escape"):
        game_is_on = False

# Clears the screen and displays the last page
screen.clear()
screen.bgcolor("black")
scoreboard.game_end(name1, name2)

# Creates an input asking if the user wishes to see their history
letter = screen.textinput(title="PLAYER HISTORY", prompt="Enter \"h\" to view your history, or click on the cancel button")
if letter == "h":
    scoreboard.read_file()

# Exits the program when user clicks on the window
screen.exitonclick()
print(f"\n\n{gm.game_over}")
