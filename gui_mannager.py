#__Creator --> Patxa
import os
import json
from random import SystemRandom
from customtkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet as fn

# Módulo de generador de contraseña
class PassWord():
    def Password(Longitud):
        Aleatoria = SystemRandom()
        Caracteres = 'abcdefghijklmnopqrstuvwxyz|@#~&%$+-_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        passWord = ""
        while Longitud > 0:
            passWord = passWord + Aleatoria.choice(Caracteres)
            Longitud = Longitud - 1
        return passWord

# Módulo para archivo
class Archive():
    def openFile(fileName):
        if os.path.isfile(fileName):
            with open(fileName, 'r') as archive:
                return json.load(archive)
        else:
            return {}

    def saveFile(fileName, data):
        with open(fileName, 'w') as archive:
            json.dump(data, archive, indent=2)

# Colores
black = '#010101'
white = '#ffffff'
green = '#03ac13'
bg_color = '#1f456e'
purple = '#480945'

# Programa Central
root = CTk()
root.geometry('300x350+250+20')
root.minsize(250, 200)
root.config(bg=bg_color)
root.title('Patxa Passwords')

frame = CTkFrame(root, fg_color=bg_color)
frame.grid(column=0, row=0, sticky='nsew')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

entry1Lab = CTkLabel(frame, bg_color=bg_color, text='Nº de caracteres?')
entry1Lab.grid(columnspan=3, row=1, padx=80, pady=10)
entry1 = CTkEntry(frame)
entry1.grid(columnspan=3, row=2, padx=80, pady=10)

entry2Lab = CTkLabel(frame, bg_color=bg_color, text='Para que?')
entry2Lab.grid(columnspan=3, row=3, padx=80, pady=10)
entry2 = CTkEntry(frame)
entry2.grid(columnspan=3, row=4, padx=80, pady=10)

def btStartOnClick():
    fileName = 'Patxa.json'
    Longitud = int(entry1.get())
    App = entry2.get()
    Pass = PassWord.Password(Longitud)
    data = Archive.openFile(fileName)
    data[App] = Pass
    Archive.saveFile(fileName, data)

    messagebox.showinfo("Success", "Data saved successfully!")
    
    # Vaciar los campos CTkEntry
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')



btStart = CTkButton(frame, border_color=purple, fg_color=green, hover_color=purple, corner_radius=10, border_width=2, text='Add new Data', command=btStartOnClick)
btStart.grid(columnspan=3, row=5, padx=30, pady=15)

def showData():
    fileName = 'Patxa.json'
    data = Archive.openFile(fileName)
    messagebox.showinfo("Data", json.dumps(data, indent=2))

btSee = CTkButton(frame, border_color=purple, fg_color=green, hover_color=purple, corner_radius=10, border_width=2, text='See your data', command=showData)
btSee.grid(columnspan=3, row=6, padx=90, pady=15)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(5, weight=1)
frame.rowconfigure(6, weight=1)

root.mainloop()