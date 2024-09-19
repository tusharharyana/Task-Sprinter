from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFFF00"
FONT_NAME = "DS-Digital"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Window_BG = "#262F50"

#UI 
window = Tk()
window.title("Task Sprinter")
window.config(bg=Window_BG)

canvas = Canvas(width=540, height=360, highlightthickness=0)

robot_img = PhotoImage(file="./Assets/Robot.gif") 
canvas.create_image(270,180,image=robot_img)
clock_img = PhotoImage(file="./Assets/Clock.png") 
canvas.create_image(150,100,image=clock_img)
canvas.create_text(150,100,text="00:00",fill="red",font=(FONT_NAME, 40, "bold"))

canvas.create_text(150, 30, text="Timer", fill=GREEN,font=(FONT_NAME, 30, "bold"))

start_button = Button(canvas, text = "Start",bg="blue", fg="white")
start_button.place(x = 80, y = 300)

reset_button = Button(text = "Reset", bg="black", fg="white")
reset_button.place(x = 180, y = 300)

canvas.pack()

window.mainloop()