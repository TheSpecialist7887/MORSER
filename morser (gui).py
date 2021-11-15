import tkinter as tk
from tkinter import Label, ttk
import tkinter.font as tkFont
from tkinter.constants import END
from tkinter.messagebox import showerror
win=tk.Tk()
win.title("MORSER")
win.geometry("577x525")
win.resizable(False,False)

"""DICTIONARY"""
MORSE_CODE_DICT = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
    '\n':'\n',
    '.':'|'
}


"""FUNCTIONS"""
def encryptor():
    output.configure(state='normal')
    output.clipboard_clear()
    text=msg.get("1.0",'end-1c')
    text=text.upper()
    output.delete("1.0","end")
    encrypted_text = ""
    try:
        for letters in text:
            if letters != " ":
                encrypted_text += MORSE_CODE_DICT[letters] + " "
            else:
                encrypted_text += " "
        show_output(encrypted_text)
        copy_text = encrypted_text.rstrip(encrypted_text[-1])
        win.clipboard_append(copy_text)
        Label(win,text="Output copied to clipboard!!").grid(row=6,column=1)
    except KeyError:
        showerror("Error", message="Only Alphabets (A-Z) and Numbers (0-9) allowed")
        msg.focus()


def decryptor():
    output.configure(state='normal')
    output.clipboard_clear()
    text=msg.get("1.0",'end-1c')
    output.delete("1.0","end")
    text += " "
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    morse = ""
    normal= ""
    try:
        for letters in text:
            if letters != " ":
                morse += letters
                space_found = 0
            else:
                space_found += 1
                if space_found == 2:
                    normal += " "
                else:
                    normal = normal + key_list[val_list.index(morse)]
                    morse = ""
        show_output(normal)
        msg.focus()
    except ValueError:
        showerror("Error", message="Only Dots [.] and Dashes [-] allowed")
        msg.focus()
    

def show_output(result):
    output.insert(END, result)
    output.configure(state='disabled')
    
def delete():
   msg.delete("1.0","end")
   msg.focus()




"""GUI STUFF""" 
win.style = ttk.Style()
title = tkFont.Font(family="Calibri", size=18,)
btn=tkFont.Font(family="cambria", size=11)
sign=tkFont.Font(family="century gothic", size=10)
box=tkFont.Font(family="Helvetica", size=15)
Label(win,text="Welcome to Morser!",font=title).grid(row=0,column=0,columnspan=3,pady=5)  #WELCOME TEXT

Label(win,text=" ").grid(row=1,column=0)

msg=tk.Text(win,width=50,height=5,background= "white",font=box,bd=3) #INPUT BOX
msg.grid(row=2,column=0,columnspan=3,padx=10,pady=10)
msg.focus() 

Label(win,text=" ").grid(row=3,column=0) #SEPARATOR   

enc=tk.Button(win,text="ENCRYPT", command=encryptor,width=20,height=2,fg='blue',font=btn,bd=5) #ENCRYPT BTN
enc.grid(row=4,column=0,padx=5)

dec=tk.Button(win,text="DECRYPT", command=decryptor,width=20,height=2,fg='green',font=btn,bd=5) #DECRYPT BTN
dec.grid(row=4,column=2,padx=5)

d=tk.Button(win, text= "CLEAR INPUT",command=delete,width=20,height=2,fg='red',font=btn,bd=5) #DELETE BTN
d.grid(row=4,column=1,padx=5)


Label(win,text=" ").grid(row=6,column=1)

output=tk.Text(win, width = 50, height =5,background = "white",bd=3,font=box,state='disabled') #OUTPUT BOX
output.grid(row=7,column=0,columnspan=3,padx=10,pady=10)

Label(win,text=" ").grid(row=8,column=0)

Label(win, text="Developed by Ayan Saha \nv1.1.0, 2021", font=sign).grid(row=9,column=0,columnspan=3) #SIGNATURE


""" MASTER LOOP """
win.mainloop()