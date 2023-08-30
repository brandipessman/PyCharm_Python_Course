from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
DARK = "#461959"
PURPLE = "#7a316f"
PINK = "#cd6688"
BLUE = "#aed8cc"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    label.config(text = "Get Building")
    check_marks.config(text = "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def raise_above_all(window):
    window.wm_attributes('-topmost', True)
    window.geometry("650x530")


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        raise_above_all(window)
        countdown(long_break_sec)
        label.config(text = "Re-Energize", fg = PINK)
    elif reps % 2 == 0:
        raise_above_all(window)
        countdown(short_break_sec)
        label.config(text="Break", fg=PURPLE)
    else:
        raise_above_all(window)
        countdown(work_sec)
        label.config(text = "Get Building", fg = DARK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for rep in range(math.floor(reps/2)):
            mark += "✔"
        check_marks.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Get Wrapped Up in Work")
window.config(padx = 50, pady = 50, bg = BLUE)

canvas = Canvas(width = 320, height = 320, bg = BLUE, highlightthickness = 0)
spider_img = PhotoImage(file = "agelenid2.png")
canvas.create_image(160, 160, image = spider_img)

label = Label(text="Get Building", fg=DARK, bg = BLUE, font=(FONT_NAME, 60, "bold"))
label.grid(row = 0, column = 1)

timer_text = canvas.create_text(155, 25, text = "00:00", fill = DARK, font = (FONT_NAME, 50, "bold"))
canvas.grid(row = 1, column = 1)

start_button = Button(text = "Start", bg = PINK, highlightthickness = 0, command = start_timer)
start_button.grid(row = 3, column = 0)

reset_button = Button(text = "Reset", bg = PINK, highlightthickness = 0, command = reset_timer)
reset_button.grid(row = 3, column = 2)

check_marks = Label(text = "", fg = DARK, bg = BLUE, font = (FONT_NAME, 50, "bold"))
check_marks.grid(column = 1, row = 3)


window.mainloop()
