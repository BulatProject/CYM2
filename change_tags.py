import eyed3

class ReTagger:
    def start_changes(self, songs_to_change, texts):
        functions_to_run = {'artist': self.change_artist, 
                            'title': self.change_title, 
                            'album': self.change_album}

        for song in songs_to_change:
            for keys in texts:
                functions_to_run[keys](song, texts[keys])

    def change_artist(self, single_path, text_new):
        base_tag = eyed3.load(single_path).tag
        artist = base_tag.artist
        if text_new:
            base_tag.artist = text_new
            base_tag.save()
            return artist, text_new
        else:
            base_tag.artist = ''
            base_tag.save()
            return artist, 'Deleted'

    def change_title(self, single_path, text_new):
        base_tag = eyed3.load(single_path).tag
        title = base_tag.title
        if text_new:
            base_tag.title = text_new
            base_tag.save()
            return title, text_new
        else:
            base_tag.title = ''
            base_tag.save()
            return title, 'Deleted'

    def change_album(self, single_path, text_new):
        base_tag = eyed3.load(single_path).tag
        album = base_tag.album
        if text_new:
            base_tag.album = text_new
            base_tag.save()
            return album, text_new
        else:
            base_tag.album = ''
            base_tag.save()
            return album, 'Deleted'
