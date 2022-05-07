import turtle as tt
SHAPE = "circle"
COLOR = "dark olive green"

class Ball (tt.Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.xpace = 10
        self.ypace = 10
        self.response = 0.05

    def move(self):
        newx = self.xcor() + self.xpace
        newy = self.ycor() + self.ypace
        self.goto((newx, newy))

    def bounce_y(self):
        self.ypace *= -1

    def bounce_x(self):
        self.xpace *= -1
        self.response *= 0.95

    def reset(self):
        self.goto(0, 0)
        self.response = 0.05
        self.bounce_x()



