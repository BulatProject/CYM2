import os
import eyed3
import asyncio
import pickle

TEST_PATH = r"D:\Python\tests"

class walker:
    def __init__(self, path):
        self.walking_directory = os.walk(path)
        self.trace_record = {}
        
    async def get_names_n_directories(self):
        for root, dirs, files in self.walking_directory:
            if self.trace_record.get(root) is None:
                self.trace_record[root] = []
            await asyncio.sleep(0)
            for name in files:
                self.trace_record[root].append(name[:-4])
                await asyncio.sleep(0)
    
    def get_dict(self):
        return self.trace_record

class logging:
    pass


a = walker(TEST_PATH)
ioloop = asyncio.get_event_loop().create_task(a.get_names_n_directories())

with open('dict_1.txt', 'w') as dict_1:
    dict_1.write(str(ioloop))
