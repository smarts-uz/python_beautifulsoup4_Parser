from datetime import datetime
list = ['2021-9-12', '2021-9-11', '2021-3', '2021-11-1', '2021-11-3', '2021-12-4', '2021-9-6', '2021-10-6']

def del_character(some_list):
    new_list = []
    for i in some_list:
        if '-' in i:
            new_list.append(i.replace('-', ''))
    return new_list

def sort_by_int(some_list):
    return some_list.sort(key=int)

try:
    sorted_list = sorted(list, key=lambda t: datetime.strptime(t, '%Y-%m-%d'))
except:
    sorted_list = sorted(list, key=lambda t: datetime.strptime(t, '%Y-%m'))

print(sorted_list)