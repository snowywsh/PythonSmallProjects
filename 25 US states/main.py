import turtle as tt
import pandas as pd

screen = tt.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

tt.shape(image)
df = pd.read_csv("50_states.csv")
states = df.state.to_list()

# def get_mouse_click_coor(x, y):
#     print(x, y)
# tt.onscreenclick(get_mouse_click_coor)
# tt.mainloop()

stateInput = screen.textinput(title="Guess the State", prompt="What is a state's name?").title()

guessedState = set()
turtles = []

while len(guessedState) < 50:
    if stateInput in states:
        t = tt.Turtle()
        t.hideturtle()
        t.penup()
        stateRow = df[df.state == stateInput]
        t.goto(int(stateRow.x), int(stateRow.y))
        t.write(stateInput)
        guessedState.add(stateInput)
        turtles.append(t)
        stateInput = screen.textinput(title=f"{len(guessedState)}/50 correct",
                                      prompt="What is another state's name?").title()
    elif stateInput == "Show":
        missingState = list(set(df.state.to_list()) - guessedState)
        missingDF = pd.DataFrame(missingState)
        missingDF.to_csv("states_to_learn")
        for m in missingState:
            t = tt.Turtle()
            t.hideturtle()
            t.penup()
            stateRow = df[df.state == m]
            t.goto(int(stateRow.x), int(stateRow.y))
            t.write(m)
            turtles.append(t)
        stateInput = screen.textinput(title=f"{len(guessedState)}/50 correct",
                                      prompt="What is another state's name?").title()
    elif stateInput == "Hide":
        for t in turtles:
            t.clear()
        stateInput = screen.textinput(title=f"0/50 correct",
                                      prompt="What is another state's name?").title()
        guessedState.clear()
    elif stateInput == "Exit":
        break
    else:
        stateInput = screen.textinput(title=f"{len(guessedState)}/50 correct",
                                      prompt="What is another state's name?").title()
    if len(guessedState) >= 50:
        t = tt.Turtle()
        t.hideturtle()
        t.penup()
        t.write("Great job! You completed all 50 states!")

screen.exitonclick()


