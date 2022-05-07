import turtle as tt
FONT = ('Arial', 24, 'normal')
ALIGNMENT = "center"
FULLPOINT = 10

class Score(tt.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('olive')
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.rightScore = 0
        self.leftScore = 0
        self.writeScore()
        self.fullPoint = FULLPOINT

    def writeScore(self):
        self.goto(-200, 260)
        self.write(self.leftScore, align=ALIGNMENT, font=FONT)
        self.goto(200, 260)
        self.write(self.rightScore, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.clear()
        self.leftScore += 1
        self.writeScore()

    def r_point(self):
        self.clear()
        self.rightScore += 1
        self.writeScore()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)