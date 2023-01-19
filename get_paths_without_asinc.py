import os

TEST_PATH = r"D:\Python\tests"

class walker:
    def __init__(self, path):
        self.walking_directory = os.walk(path)
        self.trace_record = []
        
    def get_names_n_directories(self):
        for root, dirs, files in self.walking_directory:
            for name in files:
                if name[-4:] == '.mp3':
                    self.trace_record.append(os.path.join(root, name))

    def get_readable_paths(self):
        return self.trace_record

def get_path(path):
    file_paths = walker(path)
    file_paths.get_names_n_directories()
    return file_paths.get_readable_paths()

