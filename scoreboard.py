from turtle import Turtle
FONT = ("Impact", 20, "bold")


class Scoreboard(Turtle):
    """This class is responsible for keeping track of the score adn writing text on the screen"""
    def __init__(self, player1, player2):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.name1 = player1
        self.name2 = player2
        self.update_scores()

    def write_start(self):
        """Tells the user to press Enter to start the game"""
        self.goto(0, 0)
        self.write("PRESS \"ENTER\" TO START THE GAME", align="center", font=FONT)
        self.clear()

    def update_scores(self):
        """Keeps updating the scores every time someone lets the ball through"""
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.name1}: {self.l_score}", align="center", font=FONT)
        self.goto(100, 240)
        self.write(f"{self.name2}: {self.r_score}", align="center", font=FONT)
        self.goto(210, -280)
        self.write("Press \"Esc\" to exit", font=("Impact", 15, "bold"))

    def l_point(self):
        """Calculates the score of player #1"""
        self.l_score += 1
        self.update_scores()

    def r_point(self):
        """Calculates the score of player #2"""
        self.r_score += 1
        self.update_scores()

    def game_end(self, name1, name2):
        """Prints the text and scores at the end"""
        player1 = name1
        player2 = name2
        player1_score = self.l_score
        player2_score = self.r_score
        dif = abs(player1_score - player2_score)
        self.color("white")
        self.goto(-30, -20)

        if dif <= 3:
            msg = "WOW!!! THAT WAS A CLOSE ONE!"
        else:
            msg = "THAT WAS A GREAT PLAY!!"
        self.write(f"{msg}\nPlayer Scores are:\n{player1}: {player1_score}\n"
                   f"{player2}: {player2_score}", align="center", font=FONT)
        self.goto(-270, -130)
        self.write("Press \"h\" to view history, or click here to exit", font=("Impact", 20, "bold"))
        lines = [f"{player1}: {player1_score}", f"{player2}: {player2_score}"]
        self.write_file(lines)

    def write_file(self, lines):
        my_file = open("player_history.txt", "a")
        for line in lines:
            my_file.write(f"{line}\n")
        my_file.close()

    def read_file(self):
        self.clear()
        user_map = {}
        my_file = open("player_history.txt", "r")
        all_lines = my_file.readlines()
        for line in all_lines:
            info = (line.strip()).split()
            name = info[0]
            score = info[1]
            user_map[name] = score
        y_pos = 230
        for players, scores in user_map.items():
            self.goto(0, 250)
            self.write("Player History", align="center", font=FONT)
            self.goto(-390, y_pos)
            self.write(f"{players} {scores}", align="left", font=("Impact", 15, "bold"))
            y_pos -= 30
            self.goto(210, -280)
            self.write("Click here to exit", align="center", font=("Impact", 15, "bold"))

