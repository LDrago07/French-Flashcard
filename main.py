from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
EN = ("Ariel", 40, "italic")
FN = ("Ariel", 60, "bold")
current_card = {}
to_learn = {}
# Reading CSV File
try:
    data = read_csv("Day 31 Capstone Project/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("Day 31 Capstone Project/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# Functions
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("Day 31 Capstone Project/words_to_learn.csv", index=False)
    next_card()
# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="Day 31 Capstone Project/images/card_back.png")
card_front = PhotoImage(file="Day 31 Capstone Project/images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=EN)
card_word = canvas.create_text(400, 263, text="word", font=FN)
canvas.grid(column=0, row=0, columnspan=2)
# Wrong Button
wrong_image = PhotoImage(file="Day 31 Capstone Project/images/wrong.png")
wrong_button = Button(width= 50, height=50, image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)
# Right Button
right_image = PhotoImage(file="Day 31 Capstone Project/images/right.png")
right_button = Button(width= 50, height=50, image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()