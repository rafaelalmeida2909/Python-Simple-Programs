from tkinter import *
import tkinter as tk

win = tk.Tk()
win.title('On Screen KeyBoard by Raunak')
#win.geometry("720x400")
win.config(bg="cyan")
win.iconbitmap('./Resources/Brand-Logo-Icon.ico')
win.resizable(0,0)
def select(value):
    if value == "Space":
        box.insert(INSERT,' ')
    elif value == "Enter":
        box.insert(INSERT,'\n')
    elif value == "Tab":
        box.insert(INSERT,'    ')
    elif value == "backspace":
        box.delete("1.0",END)
    else:
        box.insert(INSERT,value)
appname = Label(win,text='On Screen KeyBoard',font=("arial",20,"bold"),bg="cyan",fg='red')
appname.grid(row=0,columnspan=40)
box = Text(win,width=100,height=6,font=("arial",15),bg="white",fg='black',wrap=WORD)
box.grid(row=1,columnspan=40)
buttons = [
    '`','1','2','3','4','5','6','7','8','9','0','-','=','backspace',
    'Tab','q','w','e','r','t','y','u','i','o','p','[',']',
    'Caps Lock','a','s','d','f','g','h','j','k','l',';',"'",'Enter',
    'Shift','z','x','c','v','b','n','m',',','.','/','Shift',
    'Ctrl','fn','','alt','Space','alt','Ctrl','⇞','↑','⇟','←','↓','→'
    ]
varRow = 4
varColumn = 0
for button in buttons:
    command = lambda x = button: select(x)
    if varRow == 4:
        tk.Button(win, text=button, width=10,height=4, bg='black', fg='white', command=command).grid(row=varRow, column=varColumn)
    if varRow == 5:
        if varColumn == 0:
            tk.Button(win, text=button, width=22,height=4, bg='black', fg='white', command=command).grid(row=varRow,column=varColumn,columnspan=40, sticky=W)
        if varColumn > 0:
            tk.Button(win, text=button, width=10,height=4, bg='black', fg='white', command=command).grid(row=varRow, column=varColumn+1)
    if varRow == 6:
        if varColumn == 0:
            tk.Button(win, text=button, width=22,height=4, bg='black', fg='white', command=command).grid(row=varRow,column=varColumn,columnspan=40,sticky=W)
        if varColumn > 0:
            tk.Button(win, text=button, width=10,height=4, bg='black', fg='white', command=command).grid(row=varRow,column=varColumn+1)
    if varRow == 7:
        if varColumn == 0:
            tk.Button(win, text=button, width=22,height=4, bg='black', fg='white', command=command).grid(row=varRow,column=varColumn,columnspan=40,sticky=W)
        if varColumn > 0 and varColumn<11:
            tk.Button(win, text=button, width=10,height=4, bg='black', fg='white', command=command).grid(row=varRow,column=varColumn+1)
        if varColumn == 11:
            tk.Button(win, text=button, width=21,height=4, bg='black', fg='white', command=command).grid(row=varRow,column=varColumn+1,columnspan=40, sticky="nsew")
    if varRow == 8:
        if varColumn<4:
            tk.Button(win, text=button, width=10,height=4, bg='black', fg='white', command=command).grid(row=varRow, column=varColumn,rowspan=2,sticky="nsw")
        if varColumn == 4:
            tk.Button(win, text=button, width=56,height=4, bg='black', fg='white', command=command).grid(row=varRow, column=varColumn, columnspan=30,rowspan=2,sticky="nsw")
        if varColumn > 4 and varColumn<7:
            tk.Button(win, text=button, width=10,height=4, bg='black', fg='white', command=command).grid(row=varRow, column=varColumn+4,rowspan=2,sticky="nsw")
        if varColumn>=7:
            tk.Button(win, text=button, width=10, height=2, bg='black', fg='white', command=command).grid(row=varRow,column=varColumn + 4,sticky="nw")
    if varRow == 9:
        tk.Button(win, text=button, width=10, height=2, bg='black', fg='white', command=command).grid(row=varRow,column=varColumn,sticky="nw")

    varColumn+=1
    if varColumn>=14 and varRow==4:
        varColumn=0
        varRow+=1
    if varColumn>=13 and varRow==5:
        varColumn=0
        varRow+=1
    if varColumn>=13 and varRow==6:
        varColumn=0
        varRow+=1
    if varColumn>=12 and varRow==7:
        varColumn=0
        varRow+=1
    if varColumn == 10 and varRow==8:
        varColumn=11
        varRow+=1
mainloop()
