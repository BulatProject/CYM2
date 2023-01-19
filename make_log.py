from datetime import datetime


def log_to_dic(func):
    def wraptor(self):
        self.func = func
        path, old_tag, new_tag = self.func(self)
        record = f"{str(datetime.now())[:-5]}, {self.func.__name__.replace('_', ' ')}, {path}, {old_tag}, {new_tag}\n"
        return logger.dose_the_log(record)
    return wraptor


class logger:
    def __init__(self):
        self.doser = set()

    def write_to_file(self, records):
        with open('actions_log.csv', 'a', encoding="utf-8") as actions:
            for line in records:
                actions.write(line)

    def dose_the_log(self, record):
        self.doser.add(record)
        if len(self.doser) >= 20:#ИСПРАВИТЬ
            self.write_to_file(self.doser)
            self.doser.clear()