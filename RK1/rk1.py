# используется для сортировки
from operator import itemgetter


class CD:
    """CD-диск"""

    def __init__(self, id, title, price, lib_id):
        self.id = id
        self.title = title
        self.price = price
        self.lib_id = lib_id


class CDLibrary:
    """Библиотека CD-дисков"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class CDInLibrary:
    """
    'Диски библиотеки' для реализации
    связи многие-ко-многим
    """

    def __init__(self, lib_id, cd_id):
        self.lib_id = lib_id
        self.cd_id = cd_id


# Библиотеки CD-дисков
libraries = [
    CDLibrary(1, 'Городская библиотека CD-дисков'),
    CDLibrary(2, 'Фонотека университета'),
    CDLibrary(3, 'Библиотека музыкальных записей'),
    CDLibrary(4, 'Домашняя библиотека коллекционера'),
]

# CD-диски
cds = [
    CD(1, 'Ария. Герой асфальта', 650, 1),
    CD(2, 'Кино. Группа крови', 725, 1),
    CD(3, 'Аквариум. Радио Африка', 590, 2),
    CD(4, 'ДДТ. Актриса весна', 480, 1),
    CD(5, 'Алиса. Энергия', 515, 3),
]

# Диски библиотек (связь многие-ко-многим)
cds_libraries = [
    CDInLibrary(1, 1),
    CDInLibrary(1, 2),
    CDInLibrary(1, 4),
    CDInLibrary(2, 3),
    CDInLibrary(3, 5),

    CDInLibrary(2, 1),
    CDInLibrary(4, 3),
    CDInLibrary(4, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(cd.title, cd.price, lib.name)
                   for lib in libraries
                   for cd in cds
                   if cd.lib_id == lib.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(lib.name, link.lib_id, link.cd_id)
                         for lib in libraries
                         for link in cds_libraries
                         if lib.id == link.lib_id]

    many_to_many = [(cd.title, cd.price, lib_name)
                    for lib_name, lib_id, cd_id in many_to_many_temp
                    for cd in cds if cd.id == cd_id]

    print('Задание Е1')
    # ключ - библиотека, значение - список названий дисков
    res_1 = {lib.name: [title for title, _, _ in
                        filter(lambda i: i[2] == lib.name, one_to_many)]
             for lib in libraries
             if 'библиотека' in lib.name.lower()}
    print(res_1)

    print('\nЗадание Е2')
    res_2_unsorted = []
    # Перебираем все библиотеки
    for lib in libraries:
        # Цены дисков библиотеки
        lib_prices = [price for _, price, _ in
                      filter(lambda i: i[2] == lib.name, one_to_many)]
        # Если библиотека не пустая
        if len(lib_prices) > 0:
            # Средняя цена дисков библиотеки
            lib_avg = round(sum(lib_prices) / len(lib_prices), 2)
            res_2_unsorted.append((lib.name, lib_avg))

    # Сортировка по средней цене
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание Е3')
    # ключ - название диска, значение - список библиотек
    # 'А' здесь - кириллическая буква
    res_3 = {cd.title: [lib_name for _, _, lib_name in
                        filter(lambda i: i[0] == cd.title, many_to_many)]
             for cd in cds
             if cd.title.startswith('А')}
    print(res_3)


if __name__ == '__main__':
    main()
