import datetime

datetime_strings = ["2023-10-18 10:30:00","2023-11-18 10:30:00", "2023-11-08 7:30:00", "2023-11-17 10:30:00", "2023-11-17 13:30:00", "2023-11-18 10:30:00"]

datetime_strings.sort(key=lambda date: datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))

# Group into sublists by day
groups = []
day = None
day_list = []
for date in datetime_strings:
    current = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()
    if day != current:
        if day_list:
            groups.append(day_list)
        day_list = [date]
        day = current
    else:
        day_list.append(date)
groups.append(day_list)

print(groups)