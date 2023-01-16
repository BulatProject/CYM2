import eyed3
import os
import subprocess

'критерии отбора не забыть .lower()'

MANUAL_CHECK = 'manual_check.txt'
ALL_INFO_TO_SHOW = '{}\nArtist: {}\nTitle: {}\nAlbum: {}\n\n'
ARTIST_TO_SHOW = '{}\nArtist: {}\n\n'
TITLE_TO_SHOW = '{}\nTitle: {}\n\n'
ALBUM_TO_SHOW = '{}\nAlbum: {}\n\n'

BAN_LIST = ['official',
	'video',
	'/', '\\', ':', '*', '?', '<', '>', '|', '...', ' ...', ' - ',
	#"'(' and ')' not in",
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
    'mp3'
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
    def __init__(self, paths_list):
        self.paths = paths_list
        self.get_base_tag()
        self.get_all_tags()
# Now dictionaries are created as you create an object.
# And they are ready to be used.
# Надо будет удалять экземпляр класса после его создания в функции, отвечающей за изменение метаданных.

    def get_base_tag(self):
        self.paths_and_tags = {one_path: eyed3.load(one_path).tag for one_path in self.paths}
        self.tags_and_paths = {self.song_tags.get(path): path for path in self.paths_and_tags}

    def get_all_tags(self):
        self.all_tags = {tags: [tags.artist, tags.title, tags.album] for tags in self.tags_and_paths}

    def check_for_any_bad_metadata(self):
        self.songs_for_change = set()
        for metadata in self.all_tags:
            metadata_list = self.all_tags.get(metadata)
            stop = False

            for every_tag in metadata_list:
                if stop:
                    break;
                if every_tag is None:
                    continue;
                for banned_symbol in BAN_LIST:
                    if banned_symbol in every_tag.lower():
                        self.songs_for_change.add(ALL_INFO_TO_SHOW.format(self.tags_and_paths.get(metadata), 
                                                        metadata_list[0], 
                                                        metadata_list[1], 
                                                        metadata_list[2]))
                    stop = True
                    break;
        self.open_file_with_problems()

    def open_file_with_problems(self):
        with open(MANUAL_CHECK, 'w') as file:
            file.write(self.songs_for_change)
        subprocess.call(MANUAL_CHECK, shell = True)

    def check_artist(self):
        self.songs_to_change = set()
        open(MANUAL_CHECK, 'w').close()
        for song in self.paths:
            artist = self.get_base_tag(song).artist
            if artist is None:
                continue;
            for banned_symbol in BAN_LIST:
                if banned_symbol in artist.lower():
                    with open(MANUAL_CHECK, 'a') as file:
                        file.write(ARTIST_TO_SHOW.format(song, artist))
        subprocess.call(MANUAL_CHECK, shell = True)

    def check_title(self):
        self.songs_to_change = set()
        open(MANUAL_CHECK, 'w').close()
        for song in self.paths:
            title = self.get_base_tag(song).title
            if title is None:
                continue;
            for banned_symbol in BAN_LIST:
                if banned_symbol in title.lower():
                    self.songs_to_change.add(song)
                    with open(MANUAL_CHECK, 'a') as file:
                        file.write(ARTIST_TO_SHOW.format(song, title))
        subprocess.call(MANUAL_CHECK, shell = True)

    def check_album(self):
        self.songs_to_change = set()
        open(MANUAL_CHECK, 'w').close()
        for song in self.paths:
            album = self.get_base_tag(song).album
            if album is None:
                continue;
            for banned_symbol in BAN_LIST:
                if banned_symbol in album.lower():
                    self.songs_to_change.add(song)
                    with open(MANUAL_CHECK, 'a') as file:
                        file.write(ARTIST_TO_SHOW.format(song, album))
        subprocess.call(MANUAL_CHECK, shell = True)


a = Tagger('D:/Python/tests')
a.check_for_any_bad_metadata()

# Сделан вывод вариантов в файл для просмотра.
# Не сделаны условия для автоматической правки и не сделана функция по изменению данных.

def checkbox(self, a=True):
    if a:
        check_for_any_bad_metadata()
    else:
        change_metadata()

