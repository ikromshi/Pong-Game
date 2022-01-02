from turtle import Turtle


class Ball(Turtle):
    """This class is responsible for keeping the ball move at all times"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x_move = 0.1
        self.y_move = 0.1
        self.move_ball()
        self.checker = 1

    def change_color(self, counter):
        """Changes the color of the ball each time it hits a wall"""
        self.checker += counter
        if self.checker % 3 == 0:
            self.color("blue")
        elif self.checker % 2 == 0:
            self.color("white")
        else:
            self.color("black")

    def move_ball(self):
        """Keeps moving the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Changes the y-direction of the ball if it gets too high or too low"""
        self.y_move *= -1

    def bounce_x(self):
        """Changes the x-direction of the ball each time it hits a paddle"""
        self.x_move *= -1

    def reset_position(self):
        """Spawns the ball from the middle if a player misses i"""
        self.goto(0, 0)
        self.bounce_x()
