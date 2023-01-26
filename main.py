import tkinter as tk
from tkinter import filedialog as fd
from get_tags import *
from get_paths import *
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
        'Запустить исправитель',
        'Заполните или отключите поле!',
        'Заполните поле!']
HELP = '''Если снять все галочки c "искать в", то проверены будут все три тега и название.
Программа будет искать следующие паттерны:
"official", "video", "/", "\\", ":", "*", "?", "<", ">", "|", "...", " ...",
" - ", "vevo", "mrsuicidesheep", "music", "alona chemerys", "aviencloud",
"vk virus bot", ".net", ".ru", ".org", ".com", "bot", "mp3", "  и  ".
Также будет происходить проверка на наличие незакрытых скобок.
В таком режиме запустить исправитель нельзя.'''


class Commands:
    def __init__(self):
        self.entries = {artist_entry: 'Artist', title_entry: 'Title', album_entry: 'Album'}
        self.changers = {'Artist': [artist_change, clear_artist_var], 'Title': [title_change, clear_title_var], 'Album': [album_change, clear_album_var]}
        self.check = None

    def choose_n_show_dir(self):
        directory = fd.askdirectory()
        current_path.config(text=TEXTS[8]+directory, wraplength=250)
        self.check = Tagger(get_path(directory))

    def check_all(self):
        self.check.run_check()

    def which_check(self):
        tags_to_check = {}
        if self.check is None:
            current_path.config(text='Сначала выберите папку!\n')
        elif check_artist_var.get() == check_title_var.get() == check_album_var.get() == 1:
            return self.check_all
        else:
            for each in self.entries:
                text = each.get()
                if str(each['state']) == 'disabled':
                    continue
                elif all((len(text), text != TEXTS[0], text != TEXTS[1], text != TEXTS[2], text != TEXTS[13])):
                    tags_to_check[self.entries[each]] = text
                else:
                    each.delete(0, "end")
                    each.insert(0, TEXTS[13])
                    tags_to_check.clear()
        if len(tags_to_check):
            return tags_to_check

    def run_checks(self):
        tags_or_func = self.which_check()
        if type(tags_or_func).__name__ == 'method':
            tags_or_func()
        elif type(tags_or_func) is dict:
            self.check.run_check(tags_or_func)

    def which_change(self, tags_from_check):
        tags_to_change = {}
        for tag in tags_from_check:
            entry = self.changers[tag][0]
            text = entry.get()
            if self.changers[tag][1].get():
                tags_to_change[tag] = False
            elif all((text != '', text != TEXTS[3], text != TEXTS[14])):
                tags_to_change[tag] = entry.get()
            else:
                entry.delete(0, "end")
                entry.insert(0, TEXTS[14])
                tags_to_change.clear()
        if len(tags_to_change):
            return tags_to_change

    def run_change(self):
        tags_to_check = self.which_check()
        texts = {}
        if type(tags_to_check) is dict:
            tags_to_change = [key for key in tags_to_check]
            to_clear = self.which_change(tags_to_change)
            if type(to_clear) is dict:
                for keys in tags_to_check:
                    texts[keys] = [tags_to_check[keys], to_clear[keys]]
                change = ReTagger()
                songs_to_change = self.check.run_check(tags_to_check, False)
                change.start_changes(songs_to_change, texts)


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
    entry.delete(0, "end")


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


def disable_checkbutton(commands_list):
# Checking state of checkbutton.
    if commands_list[0].get():
# Disabling main entry widget.
        commands_list[1].config(state="disabled")
# If our checkbutton is from the first group, then we disable all related widgets.
        if len(commands_list) != 2:
            commands_list[2].config(state="disabled")
            commands_list[3].config(state="disabled")
    else:
        commands_list[1].config(state="normal")
        if len(commands_list) != 2:
            commands_list[2].config(state="normal")
# If related checkbutton is on, we won't enable related entry widget. 
            if not commands_list[4].get():
                commands_list[3].config(state="normal")


check_artist_var = tk.IntVar()
check_title_var = tk.IntVar()
check_album_var = tk.IntVar()
clear_artist_var = tk.IntVar()
clear_title_var = tk.IntVar()
clear_album_var = tk.IntVar()

check_artist_CHB = tk.Checkbutton(top_1_1, text=TEXTS[4], variable=check_artist_var, onvalue=0, offvalue=1, command=lambda: (disable_checkbutton(ch_art_cb)))
check_title_CHB = tk.Checkbutton(top_2_1, text=TEXTS[5], variable=check_title_var, onvalue=0, offvalue=1, command=lambda: (disable_checkbutton(ch_ti_cb)))
check_album_CHB = tk.Checkbutton(top_3_1, text=TEXTS[6], variable=check_album_var, onvalue=0, offvalue=1, command=lambda: (disable_checkbutton(ch_alb_cb)))
clear_artist_CHB = tk.Checkbutton(top_1_1, text=TEXTS[7], variable=clear_artist_var, onvalue=1, offvalue=0, command=lambda: (disable_checkbutton([clear_artist_var, artist_change])))
clear_title_CHB = tk.Checkbutton(top_2_1, text=TEXTS[7], variable=clear_title_var, onvalue=1, offvalue=0, command=lambda: (disable_checkbutton([clear_title_var, title_change])))
clear_album_CHB = tk.Checkbutton(top_3_1, text=TEXTS[7], variable=clear_album_var, onvalue=1, offvalue=0, command=lambda: (disable_checkbutton([clear_album_var, album_change])))
# Number of operands was too big. Had to form a list.
ch_art_cb = [check_artist_var, artist_entry, clear_artist_CHB, artist_change, clear_artist_var]
ch_ti_cb = [check_title_var, title_entry, clear_title_CHB, title_change, clear_title_var]
ch_alb_cb = [check_album_var, album_entry, clear_album_CHB, album_change, clear_album_var]

test = Commands()

current_path = tk.Label(top_4, text=TEXTS[8]+TEXTS[9], borderwidth=2, relief='groove')
pick_path = tk.Button(top_4, text=TEXTS[10], command=test.choose_n_show_dir)
show_files = tk.Button(top_5, text=TEXTS[11], command=test.run_checks)
change_metadata = tk.Button(top_5, text=TEXTS[12], width=20, command=test.run_change)


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