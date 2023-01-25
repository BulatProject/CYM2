from datetime import datetime


def log_to_dic(func):
    def wraptor(*args):
        path, old_tag, new_tag = func(args[0], args[1], args[2])
        record = f"{str(datetime.now())[:-5]}, {path}, {func.__name__.replace('_', ' ')}, {old_tag}, {new_tag}\n"
        return write_to_file(record)
    return wraptor


def write_to_file(record):
    with open('actions_log.txt', 'a', encoding="utf-8") as actions:
        actions.write(record)