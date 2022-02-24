from tkinter import Tk, Button, Label, Text, StringVar, messagebox, Canvas, Radiobutton, BooleanVar, END, DISABLED, NORMAL
from RC4 import *

base = Tk()

base.title('RC4')
base.resizable(False, False)
base.geometry('500x400')
base.configure(background='#232426')


Canva = Canvas(base, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
Canva.place(x=0, y=335)

def gui_encrypt():
    return

def gui_decrypt():
    return

def clear():
    return

inputTextLabel = Label(base, text='Input Text')
inputTextLabel.place(x=30, y=30)
inputTextLabel.configure(background='#232426', foreground='#F2F2F2')

outputTextLabel = Label(base, text='Output Text')
outputTextLabel.place(x=30, y=230)
outputTextLabel.configure(background='#232426', foreground='#BFBFBD')

inputText = Text(base, width=25, height=3)
inputText.place(x=20, y=60)
inputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)

outputText = Text(base, width=25, height=3)
outputText.place(x=20, y=260)
outputText.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)

Encrypt = Button(base, text='Encrypt', command=lambda: gui_encrypt())
Encrypt.place(x=30, y=355)
Encrypt.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

Decript = Button(base, text='Decrypt', command=lambda: gui_decrypt())
Decript.place(x=110, y=355)
Decript.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

Clear = Button(base, text='Clear', command=lambda: clear())
Clear.place(x=410, y=355)
Clear.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

base.mainloop()