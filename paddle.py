from turtle import Turtle


class Paddle(Turtle):
    """This class creates a new paddle each time it is called"""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        """Makes the paddle go up"""
        new_y = self.ycor() + 40
        self.goto(self.xcor(), y=new_y)

    def down(self):
        """Makes the paddle go down"""
        new_y = self.ycor() - 40
        self.goto(self.xcor(), y=new_y)
