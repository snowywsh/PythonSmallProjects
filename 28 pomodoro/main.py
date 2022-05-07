
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
# use colorhunt.co for color combinations
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
SILVER = "#C0C0C0"
THISTLE = "#D8BFD8"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = .2
LONG_BREAK_MIN = .2
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def clickReset():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    title.config(text="Timer", fg=SILVER)
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def clickStart():
    global reps, timer
    if timer:
        window.after_cancel(timer)  # avoid countdown mess up on multiple click of start
    reps += 1
    print(reps)
    workSeconds = int(WORK_MIN * 60 -1)
    shortBreakSeconds = int(SHORT_BREAK_MIN * 60 -1)
    longBreakSeconds = int(LONG_BREAK_MIN * 60 -1)

    if reps % 8 == 0:
        countDown(longBreakSeconds)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countDown(shortBreakSeconds)
        title.config(text="Break", fg=PINK)
    else:
        countDown(workSeconds)
        title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    mins, seconds = count // 60, count % 60
    if mins < 10:
        mins = f"0{mins}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timerText, text=f"{mins}:{seconds}")
    if count > 0:  # cannot use while here, cause trouble
        global timer
        timer = window.after(1000, countDown, count-1)
    else:
        clickStart()
        phase = (reps % 8) // 2 if reps % 8 > 0 else 4
        check.config(text="✔" * phase)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



# canvas.pack()

# title
title = Label(text="Timer", font=(FONT_NAME, 43, "bold"), fg=SILVER, bg=YELLOW, highlightthickness=0)
title.grid(column=1, row=0)


# button
start = Button(text="Start", highlightthickness=0, command=clickStart)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightthickness=0, command=clickReset)
reset.grid(column=2, row=2)

# check marks
check = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
check.grid(column=1, row=3)




window.mainloop()