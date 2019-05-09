train_sched = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

def find_dict(list, key, value):
    for dict in list:
        if dict[key] == value:
            return dict

train111 = find_dict(train_sched, 'train', "111" )  

train111_dir = train111['direction']

train80B = find_dict(train_sched, 'train', '80B')

train80B_freq = train80B['frequency_in_minutes']

train610 = find_dict(train_sched, 'train', '610')

train610_dir = train610['direction']

# def find_north_trains(list, value):
#     north_trains = []
#     for dict in list:
#         if dict['direction'] == 'north':
#             north_trains.append(dict['train'])
#     print(north_trains)

# find_trains(train_sched, 'north')

def find_trains(list, value):
    trains_list = []
    for dict in list:
        if dict['direction'] == value:
            trains_list.append(dict['train'])
    print(f"{value} bound trains: {trains_list}")

find_trains(train_sched, 'north')

find_trains(train_sched, 'east')

train111.update({'first_departure_time' : 6})


def re_sort_trains():
    trains_by_frequency = {}

    for train in train_sched:
        freq = train['frequency_in_minutes']
        name = train['train']
        if freq in trains_by_frequency:
            trains_by_frequency[freq].append(name)
        else:
            trains_by_frequency[freq] = [name]
            
    print(trains_by_frequency)

re_sort_trains()