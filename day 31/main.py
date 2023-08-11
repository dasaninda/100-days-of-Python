##FLASH CARD APP###

#------------CONSTANTS------------
from tkinter import *
import pandas, random
import math

BACKGROUND_COLOUR = "#B1DDC6"
FONT = "Times New Roman"


#------MAIN-----
data = pandas.read_csv("german_to_english.csv")
word_to_learn = data.to_dict(orient = "records")
current_card = {}

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_to_learn)
    canvas.itemconfig(title, text ="German")
    canvas.itemconfig(gr_word, text= current_card["German"], fill= "black")
    canvas.itemconfig(card_background, image= card_frontImage)
    flip_timer= window.after(3000, func=eng_card)
    
def eng_card():
    #English card 
    canvas.itemconfig(title, text = "English")
    canvas.itemconfig(gr_word, text =current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image= card_backImage)
    

window = Tk()
window.title("German Flashcard")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOUR)

flip_timer =window.after(3000, func=eng_card)

#German Card
canvas = Canvas(width= 800, height= 526)
card_frontImage = PhotoImage(file="card_front.png")
card_backImage = PhotoImage(file = "card_back.png")
canvas.config(bg=BACKGROUND_COLOUR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image= card_frontImage)
canvas.grid(row = 0, column = 0, columnspan = 2)

#titles
title = canvas.create_text(400, 120, text="", font=(FONT, 25, "italic", "underline"))
gr_word = canvas.create_text(400, 280, text="", font=(FONT, 40, "bold"))
#Buttons
wrong_image = PhotoImage(file= "wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
unknown_button.grid(row= 1, column = 0)

right_image = PhotoImage(file= "right.png")
correct_button = Button(image=right_image, highlightthickness=0, command=next_word)
correct_button.grid(row= 1, column = 1)

next_word()

window.mainloop()

