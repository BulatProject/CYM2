import eyed3, os, subprocess


MANUAL_CHECK = 'manual_check.txt'
ALL_INFO_TO_SHOW = '{}\nArtist: {}\nTitle: {}\nAlbum: {}\nWhat was found: {}\nWhere: {}\n\n'

TAGS_TO_SHOW = '{}\n{}\n\n'
ARTIST_TO_SHOW = '{}: {}'

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
    '  и  '
]

class Tagger:

    def __init__(self, paths_list):
        self.paths = paths_list

    def run_check(self, text_from_user=None, open=True):
        if text_from_user is None:
            songs_to_change, songs_with_problems = self.divide_full_check()       
        else:
            songs_to_change, songs_with_problems = self.divide_partial_check(text_from_user)

        if open:
            self.open_file_with_problems(songs_with_problems)

        return songs_to_change

    def divide_full_check(self):
        songs_to_change = []
        songs_with_problems = set()
        for song_path in self.paths:
            path_and_tags = self.check_one_path_for_any_bad_metadata(song_path)
            if path_and_tags:
                songs_to_change.append(song_path)
                songs_with_problems.add(path_and_tags)        
        return songs_to_change, songs_with_problems

    def divide_partial_check(self, text_from_user):
        functions_to_run = {'Artist': self.check_artist, 
                            'Title': self.check_title, 
                            'Album': self.check_album}
        songs_to_change = []
        songs_with_problems = set()
        for song_path in self.paths:
            tags = []
            for key in text_from_user:
                bad_tag = functions_to_run[key](song_path, text_from_user[key])
                if bad_tag:
                    tags.append(ARTIST_TO_SHOW.format(key, bad_tag))
            if len(tags):
                songs_to_change.append(song_path)
                songs_with_problems.add(TAGS_TO_SHOW.format(song_path, '\n'.join(tags)))

        return songs_to_change, songs_with_problems


    def check_one_path_for_any_bad_metadata(self, path_to_check):
        self.path_to_check = path_to_check
        base_tag = eyed3.load(path_to_check).tag
        self.metadata_list = {base_tag.artist: 'Artist', base_tag.title: 'Title', base_tag.album: 'Album'}

        def wrap_metadata(place, banned_element):
            path_and_tags = ALL_INFO_TO_SHOW.format(
                                    self.path_to_check, 
                                    base_tag.artist, 
                                    base_tag.title, 
                                    base_tag.album,
                                    banned_element,
                                    place
)
            return path_and_tags

        if not self.check_brackets(os.path.basename(self.path_to_check)) or '...' in os.path.basename(self.path_to_check):
            return wrap_metadata('File name', 'Unclosed bracket or "..."')

        for every_tag in self.metadata_list:
            if every_tag is None:
                continue
            if not self.check_brackets(every_tag):
                return wrap_metadata(self.metadata_list[every_tag], 'Unclosed bracket')

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


    def check_artist(self, path_to_check, text_from_user):
        base_tag = eyed3.load(path_to_check).tag
        artist = base_tag.artist

        if artist is None:
            return False

        if text_from_user.lower() in artist.lower():
            return artist
        return False


    def check_title(self, path_to_check, text_from_user):
        base_tag = eyed3.load(path_to_check).tag
        title = base_tag.title

        if title is None:
            return False

        if text_from_user.lower() in title.lower():
            return title
        return False


    def check_album(self, path_to_check, text_from_user):
        base_tag = eyed3.load(path_to_check).tag
        album = base_tag.album

        if album is None:
            return False

        if text_from_user.lower() in album.lower():
            return album
        return False

