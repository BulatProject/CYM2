import tkinter as tk
from tkinter import filedialog as fd
import subprocess

window = tk.Tk()
window.geometry("800x800")
window.title('Testing.')


def open():
    dir =  fd.askdirectory()
    return dir

def open_txt():
    subprocess.call('D:\Обучение\Питон\Pyton_sources.txt', shell = True)# Передаём команду в консоль.

def remember(directory):
    print(directory)

def will_it_work():
    remember(open())


button_1 = tk.Button(window, text='Directory', command=will_it_work).pack()
button_1 = tk.Button(window, text='TXT', command=open_txt).pack()


window.mainloop()