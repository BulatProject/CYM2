import eyed3
from make_log import *


class ReTagger:
    def start_changes(self, songs_to_change, texts):
        functions_to_run = {'Artist': self.change_artist, 
                            'Title': self.change_title, 
                            'Album': self.change_album}

        for song in songs_to_change:
            for keys in texts:
                functions_to_run[keys](song, texts[keys])

    @log_to_dic
    def change_artist(self, single_path, text_new):
        base_tag = eyed3.load(single_path).tag
        artist = base_tag.artist
        if text_new[1]:
            base_tag.artist = base_tag.artist.replace(text_new[0], text_new[1])
            base_tag.save()
            return single_path, artist, base_tag.artist
        else:
            base_tag.artist = ''
            base_tag.save()
            return single_path, artist, 'Deleted'

    @log_to_dic
    def change_title(self, single_path, text_new):
        base_tag = eyed3.load(single_path).tag
        title = base_tag.title
        if text_new[1]:
            base_tag.title = base_tag.title.replace(text_new[0], text_new[1])
            base_tag.save()
            return single_path, title, base_tag.title
        else:
            base_tag.title = ''
            base_tag.save()
            return single_path, title, 'Deleted'

    @log_to_dic
    def change_album(self, single_path, text_new):
        base_tag = eyed3.load(single_path).tag
        album = base_tag.album
        if text_new[1]:
            base_tag.album = base_tag.album.replace(text_new[0], text_new[1])
            base_tag.save()
            return single_path, album, base_tag.album
        else:
            base_tag.album = ''
            base_tag.save()
            return single_path, album, 'Deleted'
