
import turtle as tt
SHAPE = "square"
COLOR = "olive"

class Paddle (tt.Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)


    def go_up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def go_down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)