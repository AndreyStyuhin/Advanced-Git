from src.processing import filter_by_state, sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по статусу EXECUTED
executed = filter_by_state(data)  # по умолчанию 'EXECUTED'
print(executed)
# Ожидаем:
# [
#   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
# ]

# Фильтрация по статусу CANCELED
canceled = filter_by_state(data, 'CANCELED')
print(canceled)
# Ожидаем:
# [
#   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]

# Сортировка по убыванию (descending=True)
sorted_desc = sort_by_date(data)  # по умолчанию True
print(sorted_desc)
# Ожидаем:
# [
#   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
# ]

# Сортировка по возрастанию (descending=False)
sorted_asc = sort_by_date(data, descending=False)
print(sorted_asc)
# Ожидаем:
# [
#   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
# ]