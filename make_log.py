from datetime import datetime

# Логгер должен проектироваться параллельно с функциями.

full_log = {}
        
def log_to_dic(func):
        
    def wraptor(self):
        self.func = func
        full_log[str(datetime.now())[:-5]] = self.func.__name__.replace('_', ' ')
        self.func(self)
    return wraptor

def write_and_dump():
    log_string = ', '.join([(f'{key}: {full_log[key]}\n') for key in full_log])
    with open('actions_log.txt', 'a') as actions:
        actions.write(log_string)
    full_log = {}

def get_all_info():
    log_values = full_log.values()

    all_info_dict = {}
    for element in log_values:
        if all_info_dict.get(element) is None:
            all_info_dict[element] = 1
        else:
            all_info_dict[element] += 1
        all_info = ', '.join([(f'{element}: {all_info_dict[element]}') for element in all_info_dict])
    return all_info