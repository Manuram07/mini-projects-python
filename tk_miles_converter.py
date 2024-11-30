from tkinter import *
def m_2_k():
    m=float(mile.get())
    k=m*1.60934
    res.config(text=f"{k}")
win=Tk()
win.title("mile to kilo")
win.minsize(width=300,height=150)
win.config(padx=20,pady=20)
mile=Entry()
mile.grid(column=1,row=0)
miles=Label(text="Miles")
miles.grid(column=2,row=0)
equal=Label(text="is equal to ")
equal.grid(column=0,row=1)
res=Label(text="0")
res.grid(column=1,row=1)
km=Label(text="KM")
km.grid(column=2,row=1)
cal=Button(text="Calculate",command=m_2_k)
cal.grid(column=1,row=2)

win.mainloop()