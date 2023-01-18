import eyed3, os, subprocess

MANUAL_CHECK = 'manual_check.txt'
ALL_INFO_TO_SHOW = '{}\nArtist: {}\nTitle: {}\nAlbum: {}\nWhat was found: {}\nWhere {}\n\n'
ARTIST_TO_SHOW = '{}\nArtist: {}\n\n'
TITLE_TO_SHOW = '{}\nTitle: {}\n\n'
ALBUM_TO_SHOW = '{}\nAlbum: {}\n\n'

BAN_LIST = ['official',
	'video',
	'/', '\\', ':', '*', '?', '<', '>', '|', '...', ' ...', ' - ', # Был опыт, когда троеточие не находилось, если перед ним стоял пробел.
	'vevo',
	'mrsuicidesheep',
	'music',
	'alona chemerys',
	'aviencloud',
    'vk virus bot',
    '.net',
    '.ru',
    '.org',
    '.com',
    'bot',
    'mp3',
    ' и'
]


'''
Автоматическая замена?
if " - " in tag.title and str(os.basename(path))[:-4] == tag.title:
    title_new = tag.title.split(' - ')
    if tag.autor != title_new[0]:
        tag.autor = title_new[0]
        tag.save()
    tag.title = title_new[1]
    tag.save()

'''
class Tagger:
# Now dictionaries are created as you create an object.
# And they are ready to be used.
# Надо будет удалять экземпляр класса после его создания в функции, отвечающей за изменение метаданных.
    def __init__(self, paths_list):
        self.paths = paths_list
#        self.put_base_tags_in_dict()
#        self.put_all_tags_in_dict()

#    def put_base_tags_in_dict(self):
#        self.paths_and_tags = {one_path: eyed3.load(one_path).tag for one_path in self.paths}
#        self.tags_and_paths = {self.paths_and_tags.get(path): path for path in self.paths_and_tags}

#    def put_all_tags_in_dict(self):
#        self.all_tags = {tags: [tags.artist, tags.title, tags.album] for tags in self.tags_and_paths}


    def run_full_check(self, function, text_from_user=None):
        songs_to_change = []
        songs_with_problems = set()

        if function.__name__ == 'check_one_path_for_any_bad_metadata':
            for song_path in self.paths:
                path_and_tags = function(song_path)
                if path_and_tags:
                    songs_to_change.append(song_path)
                    songs_with_problems.add(path_and_tags)           
        else:
            for song_path in self.paths:
                path_and_tags = function(song_path, text_from_user)
                if path_and_tags:
                    songs_to_change.append(song_path)
                    songs_with_problems.add(path_and_tags)

        self.open_file_with_problems(songs_with_problems)

        return songs_to_change # Таким образом результат работы этой функции можно будет отправить на исправление.


    def check_one_path_for_any_bad_metadata(self, path_to_check):
        if path_to_check is None:
            print('В глобальную проверку передаётся пустое значение')#Не забыть удалить проверочный принт!
            return False

        self.path_to_check = path_to_check
        base_tag = eyed3.load(path_to_check).tag
        self.metadata_list = {base_tag.artist: 'artist', base_tag.title: 'title', base_tag.album: 'album'}

        def wrap_metadata(place, banned_element):
            path_and_tags = ALL_INFO_TO_SHOW.format(
                                    self.path_to_check, 
                                    self.metadata_list[0], 
                                    self.metadata_list[1], 
                                    self.metadata_list[2],
                                    banned_element,
                                    place
)
            return path_and_tags

        if not self.check_brackets(os.path.basename(self.path_to_check)) or '...' in os.path.basename(self.path_to_check):
            return wrap_metadata('file name', 'unclosed bracket or "..."')

        for every_tag in self.metadata_list:
            if every_tag is None:
                continue;
            if not self.check_brackets(every_tag):
                return wrap_metadata(self.metadata_list[every_tag], 'unclosed bracket')

            for banned_element in BAN_LIST:
                if banned_element in every_tag.lower():
                    return wrap_metadata(self.metadata_list[every_tag], banned_element)
        return False

# Sometines original metadata or even a name of the file could be cut, leaving an unclosed bracked.
# So we are trying to identify traces of those cuts.
    def check_brackets(self, text_to_check):
        return text_to_check.count('(') is text_to_check.count(')')


    def open_file_with_problems(self, data_to_write):
        with open(MANUAL_CHECK, 'w', encoding="utf-8") as file:
            for element in data_to_write:
                file.write(element)
        subprocess.call(MANUAL_CHECK, shell = True)

#Перепроверить.
    def check_artist(self, path_to_check, text_from_user):
        if path_to_check is None or text_from_user is None:
            print('В артиста передаётся пустое значение')#Не забыть удалить проверочный принт!
            return False

        base_tag = eyed3.load(path_to_check).tag
        artist = base_tag.artist

        if artist is None:
            return False

        if text_from_user.lower() in artist.lower():
            path_and_tags = ARTIST_TO_SHOW.format(path_to_check, artist)
            return path_and_tags
        return False


    def check_title(self, path_to_check, text_from_user):
        if path_to_check is None or text_from_user is None:
            print('В название передаётся пустое значение')#Не забыть удалить проверочный принт!
            return False

        base_tag = eyed3.load(path_to_check).tag
        title = base_tag.title

        if title is None:
            return False

        if text_from_user.lower() in title.lower():
            path_and_tags = ARTIST_TO_SHOW.format(path_to_check, title)
            return path_and_tags
        return False


    def check_album(self, path_to_check, text_from_user):
        if path_to_check is None or text_from_user is None:
            print('В название передаётся пустое значение')#Не забыть удалить проверочный принт!
            return False

        base_tag = eyed3.load(path_to_check).tag
        album = base_tag.album

        if album is None:
            return False

        if text_from_user.lower() in album.lower():
            path_and_tags = ARTIST_TO_SHOW.format(path_to_check, album)
            return path_and_tags
        return False


a = Tagger('D:/Python/tests')
a.check_one_path_for_any_bad_metadata()



# Сделан вывод вариантов в файл для просмотра.
# Не сделаны условия для автоматической правки и не сделана функция по изменению данных.

def checkbox(self, a=True):
    if a:
        check_one_path_for_any_bad_metadata()
    else:
        change_metadata()

