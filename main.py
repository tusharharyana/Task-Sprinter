from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFFF00"
FONT_NAME = "DS-Digital"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Window_BG = "#262F50"
reps = 0
timer = None

# Store checkmarks in a list
check_images = []


#Reset Logic
def reset_timer():
    # Cancel the running timer
    global timer
    if timer:
        window.after_cancel(timer)

    # Reset the timer text and title label
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(title_label, text="Timer")

    # Clear checkmark images
    check_images.clear()

    # Reset the reps counter
    global reps
    reps = 0


# Count down Logic
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        canvas.itemconfig(title_label, text="Long Break", fill=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        canvas.itemconfig(title_label, text="Break", fill=PINK)
        count_down(short_break_sec)
    else:
        canvas.itemconfig(title_label, text="Do karma", fill=GREEN)
        count_down(work_sec)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # After each work session (odd reps), show checkmark
        if reps % 2 != 0:
            add_checkmark(reps // 2)
        start_timer()


def add_checkmark(session_number):
    """Adds a checkmark image next to the corresponding session after work is done."""
    global check_images

    check_img = PhotoImage(file="./Assets/Check.png")
    check_images.append(check_img)  # Store the reference to avoid garbage collection

    # Position the checkmark next to the corresponding session number
    y_positions = {0: 165, 1: 195, 2: 225, 3: 250}
    if session_number in y_positions:
        canvas.create_image(90, y_positions[session_number], image=check_img)


# UI logic
window = Tk()
window.title("Task Sprinter")
window.config(bg=Window_BG)

canvas = Canvas(width=540, height=360, highlightthickness=0, bg=Window_BG)

# Robot and Clock Images
robot_img = PhotoImage(file="./Assets/Robot.gif")
canvas.create_image(270, 180, image=robot_img)
clock_img = PhotoImage(file="./Assets/Clock.png")
canvas.create_image(150, 100, image=clock_img)

# Timer Text
timer_text = canvas.create_text(150, 100, text="00:00", fill="red", font=(FONT_NAME, 40, "bold"))

# Title Label
title_label = canvas.create_text(150, 30, text="Timer", fill=GREEN, font=(FONT_NAME, 30, "bold"))


# Work Sessions Text and Placeholder for Checkmarks
canvas.create_text(165, 165, text="25 minutes", fill=GREEN, font=("Georgia", 15, "bold"))
canvas.create_text(165, 195, text="25 minutes", fill=GREEN, font=("Georgia", 15, "bold"))
canvas.create_text(165, 225, text="25 minutes", fill=GREEN, font=("Georgia", 15, "bold"))
canvas.create_text(165, 250, text="25 minutes", fill=GREEN, font=("Georgia", 15, "bold"))

# Start Button
start_button = Button(canvas, text="Start", bg="blue", fg="white", command=start_timer)
start_button.place(x=80, y=300)

# Reset Button
reset_button = Button(text="Reset", bg="black", fg="white", command = reset_timer)
reset_button.place(x=180, y=300)

canvas.pack()

window.mainloop()
