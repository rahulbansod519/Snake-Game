from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.write(f"Score = {self.score}", False, align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", False, align="center", font=('Arial', 20, 'normal'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_board()

