import tkinter as tk
from tkinter import filedialog as fd
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
HELP = '''Если снять все галочки c "искать в", то проверены будут все три тега и название.
Программа будет искать следующие паттерны:
"official", "video", "/", "\\", ":", "*", "?", "<", ">", "|", "...", " ...",
" - ", "vevo", "mrsuicidesheep", "music", "alona chemerys", "aviencloud",
"vk virus bot", ".net", ".ru", ".org", ".com", "bot", "mp3", " и".
Также будет происходить проверка на наличие незакрытых скобок.
В таком режиме запустить исправитель нельзя.'''

class Commands:
    def __init__(self):
        self.entries = {artist_entry: 'Artist', title_entry: 'Title', album_entry: 'Album'}
        self.check = None

    def choose_n_show_dir(self):
        directory = fd.askdirectory()
        current_path.config(text=TEXTS[8]+directory, wraplength=250)
        self.check = Tagger(get_path(directory))

    def check_all(self):
        self.check.run_check()

    def run_check_artist(self):
        if artist_entry.get():
            self.check.run_check(self.check.check_artist, artist_entry.get())
        else:
            artist_entry.delete(0, "end")
            artist_entry.insert(0, 'Заполните поле!')

    def which_check(self):
        tags_to_check = {}
        if self.check is None:
            return current_path.config(text='Сначала выберите папку!\n')
        if check_artist_var.get() == check_title_var.get() == check_album_var.get() == 1:
            print('full')
            return self.check_all
        else:
            for each in self.entries:
                if str(each['state']) == 'disabled':
                    continue;
                elif each.get() != '' or each.get() != TEXTS[0] or each.get() != TEXTS[1] or each.get() != TEXTS[2]:
                    tags_to_check[self.entries[each]] = each.get()
                else:
                    each.delete(0, "end")
                    each.insert(0, 'Заполните или отключите поле!')
                    return None
        if not len(tags_to_check):
            return None
        return tags_to_check

    def run_checks(self):
        tags_or_func = self.which_check()
        if type(tags_or_func).__name__ == 'method':
            return tags_or_func()
        elif type(tags_or_func) is dict:
            return self.check.run_check(tags_or_func)

    def run_change(self):
        new_tags = self.which_check()
        if type(new_tags) is dict:
            change = ReTagger()
            songs_to_change, texts = self.check.run_check(new_tags, False)
            change.start_changes(songs_to_change, texts)

# command=test.run_check_...
#        functions_to_run = {'artist': artist_entry, 
#                            'title': title_entry, 
#                            'album': album_entry}

#all((self.entries[0].get(), self.entries[1].get(), self.entries[2].get())) проверка на пустоту  
#не забыть передать в run_check False


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


divider = tk.Frame(window, height=100)
help_info = tk.Label(divider, text=HELP, justify='left')

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


# Search entries.
artist_entry = tk.Entry(top_1_0, width=30)
artist_entry.insert(0, TEXTS[0])
artist_entry.bind(FOCUS[0], lambda event: (remove_text(artist_entry)))

title_entry = tk.Entry(top_2_0, width=30)
title_entry.insert(0, TEXTS[1])
title_entry.bind(FOCUS[0], lambda event: (remove_text(title_entry)))

album_entry = tk.Entry(top_3_0, width=30)
album_entry.insert(0, TEXTS[2])
album_entry.bind(FOCUS[0], lambda event: (remove_text(album_entry)))


# Replace entries.
artist_change = tk.Entry(top_1_0, width=15)
artist_change.insert(0, TEXTS[3])
artist_change.bind(FOCUS[0], lambda event: (remove_text(artist_change)))

title_change = tk.Entry(top_2_0, width=15)
title_change.insert(0, TEXTS[3])
title_change.bind(FOCUS[0], lambda event: (remove_text(title_change)))

album_change = tk.Entry(top_3_0, width=15)
album_change.insert(0, TEXTS[3])
album_change.bind(FOCUS[0], lambda event: (remove_text(album_change)))


def disable_checkbutton(var, name):
    if var.get():
        name.config(state="disabled")
    elif not var.get():
        name.config(state="normal")


test = Commands()


check_artist_var = tk.IntVar()
check_title_var = tk.IntVar()
check_album_var = tk.IntVar()
clear_artist_var = tk.IntVar()
clear_title_var = tk.IntVar()
clear_album_var = tk.IntVar()

check_artist_CHB = tk.Checkbutton(top_1_1, text=TEXTS[4], variable=check_artist_var, onvalue=0, offvalue=1, command=lambda: (disable_checkbutton(check_artist_var, artist_entry)))
check_title_CHB = tk.Checkbutton(top_2_1, text=TEXTS[5], variable=check_title_var, onvalue=0, offvalue=1, command=lambda: (disable_checkbutton(check_title_var, title_entry)))
check_album_CHB = tk.Checkbutton(top_3_1, text=TEXTS[6], variable=check_album_var, onvalue=0, offvalue=1, command=lambda: (disable_checkbutton(check_album_var, album_entry)))
clear_artist_CHB = tk.Checkbutton(top_1_1, text=TEXTS[7], variable=clear_artist_var, onvalue=1, offvalue=0, command=lambda: (disable_checkbutton(clear_artist_var, artist_change)))
clear_title_CHB = tk.Checkbutton(top_2_1, text=TEXTS[7], variable=clear_title_var, onvalue=1, offvalue=0, command=lambda: (disable_checkbutton(clear_title_var, title_change)))
clear_album_CHB = tk.Checkbutton(top_3_1, text=TEXTS[7], variable=clear_album_var, onvalue=1, offvalue=0, command=lambda: (disable_checkbutton(clear_album_var, album_change)))


current_path = tk.Label(top_4, text=TEXTS[8]+TEXTS[9], borderwidth=2, relief='groove')
pick_path = tk.Button(top_4, text=TEXTS[10], command=test.choose_n_show_dir)
show_files = tk.Button(top_5, text=TEXTS[11], command=test.run_checks)
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
help_info.pack(pady=10)

top_5.pack(side='bottom', fill='x', expand=True)
top_5_0.pack()
top_5_1.pack()


top_4.pack(side='bottom', fill='x', expand=True)
top_4_right.pack()


artist_entry.pack(side='left', padx=30)
check_artist_CHB.pack(side='left', padx=30)

title_entry.pack(side='left', padx=30)
check_title_CHB.pack(side='left', padx=30)

album_entry.pack(side='left', padx=30)
check_album_CHB.pack(side='left', padx=30)


artist_change.pack(side='right', padx=[0, 50])
clear_artist_CHB.pack(side='right', padx=[0, 50])

title_change.pack(side='right', padx=[0, 50])
clear_title_CHB.pack(side='right', padx=[0, 50])

album_change.pack(side='right', padx=[0, 50])
clear_album_CHB.pack(side='right', padx=[0, 50])

current_path.pack(side='left', padx=30)
pick_path.pack(side='right', padx=[0, 50])
show_files.pack(side='left', padx=30, pady=[0, 20])
change_metadata.pack(side='right', padx=[0, 50], pady=[0, 20])



if __name__ == '__main__':
    window.mainloop()
