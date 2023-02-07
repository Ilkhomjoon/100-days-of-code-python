from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")


to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn", index=False)
    next_card()
# ------------------------------UI------------------------------ #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Images

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="trovue", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)


next_card()

window.mainloop()
