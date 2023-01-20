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
        'Текущая директория:\n',
        'пока не выбрана',
        'Выбрать папку',
        'Найти и вывести файлы с проблемами',
        'Запустить исправитель']


window = tk.Tk()
window.title('CYM2')
window.geometry("500x400")


top_1 = tk.Frame(window)
top_1_0 = tk.Frame(top_1)
top_1_1 = tk.Frame(top_1)


top_2 = tk.Frame(window)
top_2_0 = tk.Frame(top_2)
top_2_1 = tk.Frame(top_2)


top_3 = tk.Frame(window)
top_3_0 = tk.Frame(top_3)
top_3_1 = tk.Frame(top_3)


divider = tk.Frame(window, height=85, bg="black")


top_4 = tk.Frame(window)
top_4_right = tk.Frame(top_4)


top_5 = tk.Frame(window)
top_5_0 = tk.Frame(top_5)
top_5_1 = tk.Frame(top_5)


def remove_text(entry):
    counter = 0
    if not counter:
        entry.delete(0, "end")
        counter = 1


# Search etries.
artist_entry = tk.Entry(top_1_0, width=30)
artist_entry.insert(0, TEXTS[0])
artist_entry.bind(FOCUS[0], lambda event: (remove_text(artist_entry)))

title_entry = tk.Entry(top_2_0, width=30)
title_entry.insert(0, TEXTS[1])
title_entry.bind(FOCUS[0], lambda event: (remove_text(title_entry)))

album_entry = tk.Entry(top_3_0, width=30)
album_entry.insert(0, TEXTS[2])
album_entry.bind(FOCUS[0], lambda event: (remove_text(album_entry)))

# Replace etries.
artist_change = tk.Entry(top_1_0, width=15)
artist_change.insert(0, TEXTS[3])
artist_change.bind(FOCUS[0], lambda event: (remove_text(artist_change)))

title_change = tk.Entry(top_2_0, width=15)
title_change.insert(0, TEXTS[3])
title_change.bind(FOCUS[0], lambda event: (remove_text(title_change)))

album_change = tk.Entry(top_3_0, width=15)
album_change.insert(0, TEXTS[3])
album_change.bind(FOCUS[0], lambda event: (remove_text(album_change)))


def print_selection(var, name):
    if var.get():
        name.config(state="disabled")
        print("disabled")
    elif not var.get():
        name.config(state="normal")
        print("normal")

check_artist_var = tk.IntVar()
check_title_var = tk.IntVar()
check_album_var = tk.IntVar()
clear_artist_var = tk.IntVar()
clear_title_var = tk.IntVar()
clear_album_var = tk.IntVar()

check_artist = tk.Checkbutton(top_1_1, text=TEXTS[4], variable=check_artist_var, onvalue=0, offvalue=1, command=lambda: (print_selection(check_artist_var, artist_entry)))
check_title = tk.Checkbutton(top_2_1, text=TEXTS[5], variable=check_title_var, onvalue=0, offvalue=1, command=lambda: (print_selection(check_title_var, title_entry)))
check_album = tk.Checkbutton(top_3_1, text=TEXTS[6], variable=check_album_var, onvalue=0, offvalue=1, command=lambda: (print_selection(check_album_var, album_entry)))
clear_artist = tk.Checkbutton(top_1_1, text=TEXTS[7], variable=clear_artist_var, onvalue=1, offvalue=0, command=lambda: (print_selection(clear_artist_var, artist_change)))
clear_title = tk.Checkbutton(top_2_1, text=TEXTS[7], variable=clear_title_var, onvalue=1, offvalue=0, command=lambda: (print_selection(clear_title_var, title_change)))
clear_album = tk.Checkbutton(top_3_1, text=TEXTS[7], variable=clear_album_var, onvalue=1, offvalue=0, command=lambda: (print_selection(clear_album_var, album_change)))



current_path = tk.Label(top_4, text=TEXTS[8]+TEXTS[9], borderwidth=2, relief='groove')
pick_path = tk.Button(top_4, text=TEXTS[10])
show_files = tk.Button(top_5, text=TEXTS[11])
change_metadata = tk.Button(top_5, text=TEXTS[12], width=20)


top_1.pack(side='top', fill='x', expand=True)
top_1_0.pack(side='top', fill='x')
top_1_1.pack(side='top', fill='x')


top_2.pack(side='top', fill='x', expand=True)
top_2_0.pack(side='top', fill='x')
top_2_1.pack(side='top', fill='x')


top_3.pack(side='top', fill='x', expand=True)
top_3_0.pack(side='top', fill='x')
top_3_1.pack(side='top', fill='x')


divider.pack(fill='x')


top_5.pack(side='bottom', fill='x', expand=True)
top_5_0.pack()
top_5_1.pack()


top_4.pack(side='bottom', fill='x', expand=True)
top_4_right.pack()


artist_entry.pack(side='left', padx=30)
check_artist.pack(side='left', padx=30)

title_entry.pack(side='left', padx=30)
check_title.pack(side='left', padx=30)

album_entry.pack(side='left', padx=30)
check_album.pack(side='left', padx=30)


artist_change.pack(side='right', padx=[0, 50])
clear_artist.pack(side='right', padx=[0, 50])

title_change.pack(side='right', padx=[0, 50])
clear_title.pack(side='right', padx=[0, 50])

album_change.pack(side='right', padx=[0, 50])
clear_album.pack(side='right', padx=[0, 50])

current_path.pack(side='left', padx=30, pady=[30, 0])
pick_path.pack(side='right', padx=[0, 50], pady=[30, 0])
show_files.pack(side='left', padx=30, pady=[0, 20])
change_metadata.pack(side='right', padx=[0, 50], pady=[0, 20])


window.mainloop()