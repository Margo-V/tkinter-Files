from tkinter import *

root = Tk()

def open_file():
    name = e.get()
    text_file = open(name)
    t.delete(1.0, END)
    t.insert(1.0, text_file.read())

def save_file():
    name = e.get()
    file = open(name, 'x')
    file.write(t.get(1.0, END))
    t.delete(1.0, END)


frame1 = Frame()
frame1.pack(pady=10)
e = Entry(frame1, width=60)

e.pack(side=LEFT)

b_open = Button(frame1, text="Открыть", width=20, command=open_file)
b_save = Button(frame1, text="Сохранить", width=20, command=save_file)
b_open.pack(side=LEFT)
b_save.pack(side=LEFT)

frame2 = Frame()
frame2.pack()
t = Text(frame2, width=70, height=10, wrap=WORD)
t.pack(side=LEFT, expand=1, fill=X)

scroll = Scrollbar(frame2, command=t.yview)
scroll.pack(side=LEFT, fill=Y)

t.config(yscrollcommand=scroll.set)

root.mainloop()