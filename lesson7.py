"""Python tkinter moduli"""
# from numpy import *
from tkinter import *

window = Tk() # Oynani hosil qilish

window.geometry('500x600') # resolution(o`lcham) berish

window.resizable(True, True) # kichraytirish yoki kattalashtirish

window.title('My GUI program') # oynaga sarlavha beruvchi atribut

window.config(background = 'grey')
def yozuv():
    Label(window, text=' Hi').place(x = 280, y = 400)
Label(window, text = 'Hi Py1', font = 15, bg = 'black', fg = 'white').place(x = 100, y = 200)
Label(window, text = 'Hello world').place(x = 350, y = 200)
Button(window, text='My button', bg = 'black', fg = 'yellow', command = yozuv).pack()
window.minsize(300, 400) # ('300x400') minimal kichrayishi
window.maxsize(700, 700) # ('700x700') maksimal kattalashishi


window.mainloop()














































