import tkinter as tk
from get_tags import *# Да, это дурная практика, но мой проект очень маленький, а потому ничего страшного не произойдёт.
from get_paths_without_asinc import *
from change_tags import *

FOCUS = ["<FocusIn>", "<FocusOut>"]
TEXTS = ['Что искать в исполнителях?', 
        'Что искать в названиях песен?', 
        'Что искать в альбомах?', 
        'Заменить на:', 
        'Искать в исполнителях', 
        'Искать в названии', 
        'Искать в альбомах',
        'Очистить',
        'Текущая директория',
        'Выбрать папку',
        'Найти и вывести файлы с проблемами',
        'Запустить исправитель']


window = tk.Tk()
window.title('CYM2')
window.geometry("600x400")


top_1 = tk.Frame(window, height=100, width=600)

top_left_1 = tk.Frame(top_1, height=100, width=180)
top_left_1_0 = tk.Frame(top_left_1, bg="yellow")
top_left_1_1 = tk.Frame(top_left_1, bg="magenta")


top_right_1 = tk.Frame(top_1, height=100, width=180)
top_right_1_0 = tk.Frame(top_right_1, bg="green")
top_right_1_1 = tk.Frame(top_right_1, bg="blue")


top_2 = tk.Frame(window, height=100, width=300)
top_2_left = tk.Frame(top_2, bg="yellow")
top_2_right = tk.Frame(top_2)


top_3 = tk.Frame(window, height=100, width=300)
top_3_left = tk.Frame(top_3)
top_3_right = tk.Frame(top_3, bg="green")


top_4 = tk.Frame(window, height=100, width=300, bg="black")
top_4_right = tk.Frame(top_4)


top_5 = tk.Frame(window, height=100, width=300, bg="red")
top_5_left = tk.Frame(top_5)
top_5_right = tk.Frame(top_5)


def remove_text(entry):
    entry.delete(0, "end")


def return_text(entry):
    entry.insert(0, "Введите текст")


# Левая половина
author_entry = tk.Entry(top_left_1_0, width=30)
author_entry.insert(0, TEXTS[0])
author_entry.bind(FOCUS[0], lambda event: (remove_text(author_entry)))
author_entry.bind(FOCUS[1], lambda event: (return_text(author_entry)))


title_entry = tk.Entry(top_2_left, width=30)
title_entry.insert(0, TEXTS[1])
title_entry.bind(FOCUS[0], lambda event: (remove_text(title_entry)))
title_entry.bind(FOCUS[1], lambda event: (return_text(title_entry)))


album_entry = tk.Entry(top_3_left, width=30)
album_entry.insert(0, TEXTS[2])
album_entry.bind(FOCUS[0], lambda event: (remove_text(album_entry)))
album_entry.bind(FOCUS[1], lambda event: (return_text(album_entry)))

# Правая половина
author_change = tk.Entry(top_right_1_0, width=15)
author_change.insert(0, TEXTS[3])
author_change.bind(FOCUS[0], lambda event: (remove_text(author_change)))
author_change.bind(FOCUS[1], lambda event: (return_text(author_change)))


title_change = tk.Entry(top_2_right, width=15)
title_change.insert(0, TEXTS[3])
title_change.bind(FOCUS[0], lambda event: (remove_text(title_change)))
title_change.bind(FOCUS[1], lambda event: (return_text(title_change)))


album_change = tk.Entry(top_3_right, width=15)
album_change.insert(0, TEXTS[3])
album_change.bind(FOCUS[0], lambda event: (remove_text(album_change)))
album_change.bind(FOCUS[1], lambda event: (return_text(album_change)))


def print_selection():
    print(1)

check_autor_var = tk.IntVar()
check_title_var = tk.IntVar()
check_album_var = tk.IntVar()
clear_1_var = tk.IntVar()
clear_2_var = tk.IntVar()
clear_3_var = tk.IntVar()
check_autor = tk.Checkbutton(top_left_1_1, text=TEXTS[4], variable=check_autor_var, onvalue=1, offvalue=0, command=print_selection)
check_title = tk.Checkbutton(top_2_left, text=TEXTS[5], variable=check_title_var, onvalue=1, offvalue=0, command=print_selection)
check_album = tk.Checkbutton(top_3_left, text=TEXTS[6], variable=check_album_var, onvalue=1, offvalue=0, command=print_selection)
clear_1 = tk.Checkbutton(top_right_1_1, text=TEXTS[7], variable=clear_1_var, onvalue=1, offvalue=0, command=print_selection)
clear_2 = tk.Checkbutton(top_2_right, text=TEXTS[7], variable=clear_2_var, onvalue=1, offvalue=0, command=print_selection)
clear_3 = tk.Checkbutton(top_3_right, text=TEXTS[7], variable=clear_3_var, onvalue=1, offvalue=0, command=print_selection)


top_1.pack(side='top', fill='x', expand=True)
top_left_1.pack(side='left', fill='both', expand=True) # ОНИ СТАРАЮТСЯ ОТОБРАЗИТЬСЯ ПОБЛИЖЕ К ЦЕНТРУ
top_right_1.pack(side='left', fill='both', expand=True)

top_left_1_0.pack(side='top', fill='both', expand=True)
top_left_1_1.pack(side='top', fill='both', expand=True)


top_2.pack(side='top', fill='both', expand=True)
top_2_left.pack(side='left', fill='both', expand=True)
top_2_right.pack(side='left', fill='both', expand=True)
top_right_1_0.pack(side='top', fill='both', expand=True)
top_right_1_1.pack(side='top', fill='both', expand=True)


top_3.pack(side='top', fill='both', expand=True)
top_3_left.pack(side='left', fill='both', expand=True)
top_3_right.pack(side='right', fill='both', expand=True)


top_4.pack(side='top', fill='both', expand=True)
top_4_right.pack()


top_5.pack(side='top', fill='both', expand=True)
top_5_left.pack()
top_5_right.pack()


author_entry.pack(side='top', anchor='nw', padx=60)
check_autor.pack(side='top', anchor='nw', padx=60)


title_entry.pack(side='top', anchor='nw', padx=60)
check_title.pack(side='top', anchor='nw', padx=60)


album_entry.pack(side='top', anchor='nw', padx=60)
check_album.pack(side='top', anchor='nw', padx=60)


author_change.pack(side='top', anchor='w')
clear_1.pack(side='top', anchor='w')


title_change.pack(side='top', anchor='w')
clear_2.pack(side='top', anchor='w')


album_change.pack(side='top', anchor='w')
clear_3.pack(side='top', anchor='w')


window.mainloop()