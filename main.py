from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text='00:00')
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    checkmark.config(text='')
# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if(reps % 2 == 0):
        count_down(short_break_sec)
        timer_label.config(text='Short Break', fg=PINK)
    elif(reps % 8 == 0):
        count_down(long_break_sec)
        timer_label.config(text='Long Break', fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text='Working', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if(count_sec < 10):
        count_sec = f'0{count_sec}'
    if(count_min < 10):
        count_min = f'0{count_min}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if(count > 0):
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        if(reps % 2 == 0):
            checkmark.config(text='✔')
        else:
            checkmark.config(text='')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.resizable(False, False)
window.config(padx=110, pady=90, bg=YELLOW)

tomato_img = PhotoImage(file='./tomato.png')
canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.config(bg=YELLOW)
canvas.create_image(100, 105, image=tomato_img)
timer_text = canvas.create_text(
    100, 115, text=f'00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row='2', column='2')

# Timer label
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_label.config(pady='10')
timer_label.grid(row='1', column='2')

# Start button
start_button = Button(width='8', text='Start', bg='white', command=timer_start)
start_button.grid(row='3', column='1')

# Check mark label
checkmark = Label(bg=YELLOW, fg=GREEN, font=('10'))
checkmark.grid(row='3', column='2')

#  Reset button
reset_button = Button(width='8', text='Reset', bg='white', command=reset_timer)
reset_button.grid(row='3', column='3')


window.mainloop()
