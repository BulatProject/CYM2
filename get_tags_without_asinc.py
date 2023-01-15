import eyed3
import os
import subprocess

'критерии отбора не забыть'

MANUAL_CHECK = 'manual_check.txt'

BAN_LIST = ['official',
	'video',
	'/', '\\', ':', '*', '?', '<', '>', '|', '...', ' ...', ' - ',
	"'(' and ')' not in",
	'vevo',
	'mrSuicideSheep',
	'music',
	'alona chemerys',
	'aviencloud',
    'VK Virus Bot',
    '.net',
    '.ru',
    '.org',
    '.com'
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
class tagger:
    def __init__(self, *paths_list):
        self.paths = paths_list

    def get_base_tag(self, one_path):
        self.song_tag = eyed3.load(one_path).tag
        return self.song_tag

    def get_all_tags(self, id3_tag):
        self.all_tags = [id3_tag.artist, id3_tag.title, id3_tag.album]
        return self.all_tags

    def check_for_bad_metadata(self):
        open(MANUAL_CHECK, 'w').close()
        for song in self.paths:
            song_metadata = self.get_all_tags(self.get_base_tag(song))
            stop = False

            for every_tag in range(len(song_metadata)):
                if stop:
                    break;

                for banned_symbol in BAN_LIST:
                    if banned_symbol in song_metadata[every_tag]:
                        with open(MANUAL_CHECK, 'a') as file:
                            file.write(f'{song}\nArtist: {song_metadata[0]}\nTitle: {song_metadata[1]}\nAlbum: {song_metadata[2]}\n\n')
                        stop = True
                        break;
        subprocess.call(MANUAL_CHECK, shell = True)

# Сделан вывод вариантов в файл для просмотра.
# Не сделаны условия для автоматической правки и не сделана функция по изменению данных.

def checkbox(self, a=True):
    if a:
        check_for_bad_metadata()
    else:
        change_metadata()

