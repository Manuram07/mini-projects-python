from tkinter import *
from tkinter import PhotoImage
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
tick=""
time=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep,tick
    win.after_cancel(time)
    canvas.itemconfig(t_t,text="00:00")
    text.config(text="Timer",fg="GREEN")
    t.config(text="")
    rep=0
    tick=""

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global rep,tick
    rep +=1
    if rep %8==0:
        count(60*LONG_BREAK_MIN)
        text.config(text="Break",fg=RED)
    elif rep %2==0:
        count(60*SHORT_BREAK_MIN)
        text.config(text="Break",fg="PINK")
    elif rep < 9:
        count(60*WORK_MIN)
        tick += "✓"
        t.config(text=tick)
        text.config(text="Work",fg="GREEN")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def count(c):
    m=int(c // 60)
    sec= int(c% 60)
    if 0 <= sec < 10:
        sec=f"0{sec}"
    if 0 <= m < 10:
        m=f"0{m}"
    canvas.itemconfig(t_t,text=f"{m}:{sec}")
    if c > 0:
        global time
        time=win.after(10,count,c-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
win=Tk()
win.title("pomodoro")
win.config(padx=100,pady=50,bg=YELLOW)
text=Label(text="Timer",fg="GREEN",bg=YELLOW,font=(FONT_NAME,50))
text.grid(column=1,row=0)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="Tomato.png")
canvas.create_image(100,112,image=tomato)
t_t=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
start=Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)
reset=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)
t=Label(fg="GREEN",bg=YELLOW,font=(FONT_NAME,20,"bold"))
t.grid(column=1,row=3)
win.mainloop()