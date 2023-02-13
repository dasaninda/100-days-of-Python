
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "lightgreen"
YELLOW = "lemonchiffon"
FONT_NAME = "verdana"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_reset = None 

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_reset)
    canvas.itemconfig(timer, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    window.after_cancel(check_marks)
    global reps
    reps = 0
   

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title.config(text="Break", font=(FONT_NAME, 30, "bold"), fg="indianred", bg=YELLOW)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title.config(text="Break", font=(FONT_NAME, 30, "bold"), fg="red", bg=YELLOW)
    else:
        countdown(work_sec)
        title.config(text="Work", font=(FONT_NAME, 30, "bold"), fg="darkslategray", bg=YELLOW)
        
    countdown()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_reset
        timer_reset= window.after(1000, countdown, count-1)
    else :
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark = "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=80,pady=50, bg=YELLOW)


canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_image= PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image= tomato_image)
timer = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column=2, row=2)


title =Label(text= "Timer", font=(FONT_NAME, 30, "bold"), fg="teal", bg=YELLOW)
title.grid(column=2, row=1)

start_button = Button(text="Start", bg="darkseagreen", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", bg="lightcoral", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks= Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "normal"))
check_marks.grid(column = 2, row= 4)


window.mainloop()
