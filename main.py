BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

screen = Tk()
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


try:
    words = pandas.read_csv("./data/to_learn.csv")
except:
    words = pandas.read_csv("./data/french_words.csv")  

words_dict = words.to_dict(orient='records')
current_word = {}

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_image = PhotoImage(file=".\images\card_front.png")
back_card = PhotoImage(file=".\images\card_back.png")
canva_card = canvas.create_image(400, 263, image=card_image)
card_title = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


def next_card():
    global current_word, flip_time
    screen.after_cancel(flip_time)
    current_word = random.choice(words_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    canvas.itemconfig(canva_card, image=card_image)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_word["French"])
    flip_time = screen.after(3000, flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(canva_card, image=back_card)

def is_known():    
    words_dict.remove(current_word)
    data = pandas.DataFrame(words_dict)
    data.to_csv("./data/to_learn.csv", index=False)
    next_card()
    print(len(words_dict))


flip_time = screen.after(3000, flip_card)

known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, borderwidth=3, highlightthickness=0, command=is_known)
known_button.grid(row=1,column=1)

unknown_image = PhotoImage(file="./images\wrong.png")
unknown_button = Button(image=unknown_image, borderwidth=3, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

screen.mainloop()

