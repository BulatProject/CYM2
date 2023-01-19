import tkinter as tk
from get_tags_without_asinc import *# Да, это дурная практика, но мой проект очень маленький, а потому ничего страшного не произойдёт.
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
        'Запустить исправитель'
]

window = tk.Tk()
window.title('CYM2')
window.geometry("800x400")


top_1 = tk.Frame(window)

top_1_left = tk.Frame(top_1)
top_1_0_left = tk.Frame(top_1_left)
top_1_1_left = tk.Frame(top_1_left)

top_1_right = tk.Frame(top_1)
top_1_0_right = tk.Frame(top_1_right)
top_1_1_right = tk.Frame(top_1_right)

top_2 = tk.Frame(window)
top_2_left = tk.Frame(top_2)
top_2_right = tk.Frame(top_2)


top_3 = tk.Frame(window)
top_3_left = tk.Frame(top_3)
top_3_right = tk.Frame(top_3)


top_4 = tk.Frame(window)
top_4_right = tk.Frame(top_4)


top_5 = tk.Frame(window)
top_5_left = tk.Frame(top_5)
top_5_right = tk.Frame(top_5)


def remove_text(entry):
    entry.delete(0, "end")


def return_text(entry):
    entry.insert(0, "Введите текст")

# Левая половина
author_entry = tk.Entry(top_1_0_left)
author_entry.insert(0, TEXTS[0])
author_entry.bind(FOCUS[0], lambda event: (remove_text(author_entry)))
author_entry.bind(FOCUS[1], lambda event: (return_text(author_entry)))


title_entry = tk.Entry(top_2_left)
title_entry.insert(0, TEXTS[1])
title_entry.bind(FOCUS[0], lambda event: (remove_text(title_entry)))
title_entry.bind(FOCUS[1], lambda event: (return_text(title_entry)))


album_entry = tk.Entry(top_3_left)
album_entry.insert(0, TEXTS[2])
album_entry.bind(FOCUS[0], lambda event: (remove_text(album_entry)))
album_entry.bind(FOCUS[1], lambda event: (return_text(album_entry)))

# Правая половина
author_change = tk.Entry(top_1_0_right)
author_change.insert(0, TEXTS[3])
author_change.bind(FOCUS[0], lambda event: (remove_text(author_change)))
author_change.bind(FOCUS[1], lambda event: (return_text(author_change)))


title_change = tk.Entry(top_2_right)
title_change.insert(0, TEXTS[3])
title_change.bind(FOCUS[0], lambda event: (remove_text(title_change)))
title_change.bind(FOCUS[1], lambda event: (return_text(title_change)))


album_change = tk.Entry(top_3_right)
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
check_autor = tk.Checkbutton(top_1_1_left, text=TEXTS[4], variable=check_autor_var, onvalue=1, offvalue=0, command=print_selection)
check_title = tk.Checkbutton(top_2_left, text=TEXTS[5], variable=check_title_var, onvalue=1, offvalue=0, command=print_selection)
check_album = tk.Checkbutton(top_3_left, text=TEXTS[6], variable=check_album_var, onvalue=1, offvalue=0, command=print_selection)
clear_1 = tk.Checkbutton(top_1_1_right, text=TEXTS[7], variable=clear_1_var, onvalue=1, offvalue=0, command=print_selection)
clear_2 = tk.Checkbutton(top_2_right, text=TEXTS[7], variable=clear_2_var, onvalue=1, offvalue=0, command=print_selection)
clear_3 = tk.Checkbutton(top_3_right, text=TEXTS[7], variable=clear_3_var, onvalue=1, offvalue=0, command=print_selection)


top_1.pack()
top_1_left.pack(side='left') # JОНИ СТАРАЮТСЯ ОТОБРАЗИТЬСЯ ПОБЛИЖЕ К ЦЕНТРУ
top_1_right.pack(side='right')

top_1_0_left.pack(side='left')
top_1_1_left.pack(side='right')


top_2.pack()
top_2_left.pack(side='left')
top_2_right.pack(side='left')
top_1_0_right.pack(side='left')
top_1_1_right.pack(side='right')


top_3.pack()
top_3_left.pack(side='left')
top_3_right.pack(side='right')


top_4.pack()
top_4_right.pack()


top_5.pack()
top_5_left.pack()
top_5_right.pack()


author_entry.pack(side='top')
check_autor.pack(side='top')


title_entry.pack()
check_title.pack()


album_entry.pack()
check_album.pack()


author_change.pack(side='top')
clear_1.pack(side='top')


title_change.pack()
clear_2.pack()


album_change.pack()
clear_3.pack()


window.mainloop()