list = ['2021-2', '2021-1', '2021-3', '2021-11', '2021-11', '2021-12', '2021-9', '2021-13']

list_wi = []
for i in list:
    if '-' in i:
        list_wi.append(i.replace('-', ''))

print(list_wi.sort(key=int))
print(list_wi)