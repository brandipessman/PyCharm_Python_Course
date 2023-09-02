from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_words = pandas.read_csv("data/french_words.csv")
    to_learn = original_words.to_dict(orient="records")
else:
    to_learn = words.to_dict(orient = "records")


def pick_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card['French'], fill = "black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func = flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image = card_back)
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "white")


def is_known():
    to_learn.remove(current_card)
    words = pandas.DataFrame(to_learn)
    words.to_csv("data/words_to_learn.csv")
    pick_card()

window = Tk()
window.title("Flashcards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width = 800, height = 526)
card_front = PhotoImage(file = "images/card_front.png")
canvas_image = canvas.create_image(400, 263, image = card_front)
card_back = PhotoImage(file = "images/card_back.png")
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text = "French", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "word", font = ("Ariel", 60, "bold"))
canvas.grid(column = 0, row = 0, columnspan = 2)



###----------GUI INTERFACE----------###

wrong_img = PhotoImage(file = "images/wrong.png")
no_button = Button(image = wrong_img, highlightthickness=0, command = pick_card)
no_button.grid(row = 1, column = 0)
right_img = PhotoImage(file = "images/right.png")
yes_button = Button(image = right_img, highlightthickness=0, command = is_known)
yes_button.grid(row = 1, column = 1)

pick_card()


window.mainloop()