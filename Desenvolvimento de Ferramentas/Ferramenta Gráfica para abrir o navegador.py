import webbrowser
from tkinter import *

raiz = Tk( )
raiz.title('Abrir Browser')
raiz.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

def chatGPT():
    webbrowser.open('https://chatgpt.com/')

def moodle():
    webbrowser.open('https://www.moodle.fsa.br/')

meu_google = Button(raiz, text = 'Abrir o Google', command = google).pack(pady = 20)
meu_chatGPT = Button(raiz, text = 'Abrir o chatGPT', command = chatGPT).pack(pady = 20)
meu_moodle = Button(raiz, text = 'Abrir o Moodle', command = moodle).pack(pady = 20)
raiz.mainloop()


