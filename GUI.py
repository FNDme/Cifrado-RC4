from tkinter import Tk, Button, Label, Text, Entry, Canvas,  END, DISABLED, NORMAL
from RC4 import *
from conversor import txt_to_bytes, bytes_to_txt

# Main window
base = Tk()
base.title('RC4')
base.resizable(False, False)
base.geometry('500x400')
base.configure(background='#232426')
# Canvas
Canva = Canvas(base, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
Canva.place(x=0, y=335)

# GUI version of encrypt and decrypt
def gui_RC4(mode):
    # Text mode
    if mode:
        input = inputText.get("1.0", END).strip()
        input = txt_to_bytes(input)

        keySeed = keySeedText.get().strip()
        keySeed = txt_to_bytes(keySeed)

        inputBytes.delete("1.0", END)
        for i in input:
            inputBytes.insert(END, str(i) + " ")
        
        keySeedBytes.delete(0, END)
        for i in keySeed:
            keySeedBytes.insert(END, str(i) + " ")

    # Bytes mode
    else:
        input = inputBytes.get("1.0", END).strip()
        input = input.split(" ")

        keySeed = keySeedBytes.get().strip()
        keySeed = keySeed.split(" ")

        for i in range(len(input)):
            input[i] = int(input[i])

        for i in range(len(keySeed)):
            keySeed[i] = int(keySeed[i])

        inputText.delete("1.0", END)
        inputText.insert(END, bytes_to_txt(input))

        keySeedText.delete(0, END)
        keySeedText.insert(END, bytes_to_txt(keySeed))

    # Encrypt
    output = RC4(keySeed, input)

    # Output
    outputText.config(state=NORMAL)
    outputText.delete("1.0", END)
    outputText.insert(END, bytes_to_txt(output))
    outputText.config(state=DISABLED)

    outputBytes.config(state=NORMAL)
    outputBytes.delete("1.0", END)
    outputBytes.insert(END, output)
    outputBytes.config(state=DISABLED)

    return

# Clear all blocks
def clear():

    inputText.delete("1.0", END)
    inputBytes.delete("1.0", END)

    keySeedText.delete(0, END)
    keySeedBytes.delete(0, END)

    outputText.config(state=NORMAL)
    outputText.delete("1.0", END)
    outputText.config(state=DISABLED)
    outputBytes.config(state=NORMAL)
    outputBytes.delete("1.0", END)
    outputBytes.config(state=DISABLED)

    return

# Labels
    # Input
inputTextLabel = Label(base, text='Input Text')
inputTextLabel.place(x=30, y=30)
inputTextLabel.configure(background='#232426', foreground='#F2F2F2')
inputBytesLabel = Label(base, text='Input Bytes')
inputBytesLabel.place(x=280, y=30)
inputBytesLabel.configure(background='#232426', foreground='#F2F2F2')
    # Key Seed
keySeedTextLabel = Label(base, text='Key Seed')
keySeedTextLabel.place(x=30, y=130)
keySeedTextLabel.configure(background='#232426', foreground='#F2F2F2')
keySeedBytesLabel = Label(base, text='Key Seed Bytes')
keySeedBytesLabel.place(x=280, y=130)
keySeedBytesLabel.configure(background='#232426', foreground='#F2F2F2')
    # Output
outputTextLabel = Label(base, text='Output Text')
outputTextLabel.place(x=30, y=200)
outputTextLabel.configure(background='#232426', foreground='#BFBFBD')
outputBytesLabel = Label(base, text='Output Bytes')
outputBytesLabel.place(x=280, y=200)
outputBytesLabel.configure(background='#232426', foreground='#BFBFBD')

# Texts
    # Input
inputText = Text(base, width=25, height=3)
inputText.place(x=20, y=60)
inputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
inputBytes = Text(base, width=25, height=3)
inputBytes.place(x=270, y=60)
inputBytes.configure(background='#04BF68', foreground='#232426', borderwidth=0)
    # Key Seed
keySeedText = Entry(base, width=33)
keySeedText.place(x=20, y=160)
keySeedText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
keySeedBytes = Entry(base, width=33)
keySeedBytes.place(x=270, y=160)
keySeedBytes.configure(background='#04BF68', foreground='#232426', borderwidth=0)
    # Output
outputText = Text(base, width=25, height=3)
outputText.place(x=20, y=230)
outputText.config(state=DISABLED, background='#155939', foreground='#BFBFBF', borderwidth=0)
outputBytes = Text(base, width=25, height=3)
outputBytes.place(x=270, y=230)
outputBytes.config(state=DISABLED, background='#155939', foreground='#BFBFBF', borderwidth=0)

# Buttons
    # Encrypt/Decrypt by text
cipherText = Button(base, text='Cipher text', command=lambda: gui_RC4(True))
cipherText.place(x=30, y=355)
cipherText.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
    # Encrypt/Decrypt by bytes
cipherBytes = Button(base, text='Cipher bytes', command=lambda: gui_RC4(False))
cipherBytes.place(x=130, y=355)
cipherBytes.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
    # Clear
Clear = Button(base, text='Clear', command=lambda: clear())
Clear.place(x=410, y=355)
Clear.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)


base.mainloop()