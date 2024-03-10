from asposecells.api import Workbook
from collections import defaultdict


def xls_converting(path_file_name):
    """
    Конвертация в читаемый формат.
    """

    workbook = Workbook(path_file_name)
    workbook.save("work_file.xls")


def salary_calculation(sh):
    """
    Вычисление региона с самой высокой медианной з/п;
    Вычисление самой высокооплачиваемой профессии.
    (файл с одним листом).
    """

    # - 1: Вводим переменные (словари, данные из файла).
    d_region = {}
    d_prof = {}
    vals = [sh.row_values(rownum) for rownum in range(sh.nrows)]

    # - 1.1: Создаём словарь для текущего листа; вносим туда все виды профессий.
    for profs in vals[0][1:]:
        d_prof[profs] = 0

    # - 1.2: Вносим в словарь с медианой названия регионов; заполняем значения обоих словарей.
    for j in vals[1:]:
        numbers = j[1:]
        if numbers:
            try:
                z = 0
                for key, value in d_prof.items():
                    d_prof[key] += numbers[z]
                    z += 1
                numbers.sort()
                central_numb = float(numbers[len(numbers) // 2])
                central_numb_2 = float(numbers[len(numbers) // 2 - 1])
                if len(numbers) % 2 != 0:
                    d_region[j[0]] = central_numb
                else:
                    d_region[j[0]] = (central_numb + central_numb_2) / 2
            except ValueError:
                continue

    # - 2: Узнаём название региона с самой высокой медианой.
    p = 0
    region_output = ''
    for key, value in d_region.items():
        if value > p:
            region_output = key
            p = value
        elif value == p:
            region_output += ', ' + key

    # - 3: Узнаём название профессии с самой высокой оплатой по регионам.
    p = 0
    prof_output = ''
    for key, value in d_prof.items():
        if value > p:
            prof_output = key
            p = value
        elif value == p:
            prof_output += f', {key}'
    out = f'{region_output} {prof_output}'

    return out


def nutritious_food(sh):
    """
    Список самых каллорийных продуктов (сразу выводит результат по вызову функции)
    (файл с одним листом).
    """

    # - 1: Вводим переменные (словари, списки, данные из файла).
    d = defaultdict(str)
    sp = []
    sp_new = []
    vals = [sh.row_values(rownum) for rownum in range(sh.nrows)]

    # - 1.1: Заполняем словарь необходимыми значениями.
    for j in vals:
        if len(j) > 1:
            try:
                d[float(j[1])] += f'{j[0]}*'
            except ValueError:
                continue

    # - 2: Переносим значения в список и сортируем по коллориям.
    for key, value in d.items():
        sp.append(f'{key}*{value}')
    sp.sort()
    sp.reverse()

    # - 3: Сортируем лексикографически блюда с одинаковой каллорийностью.
    for el in sp:
        sp_el = el.split('*')
        sp_el.sort()
        for name in sp_el[2:]:
            sp_new.append(name)

    return sp_new


def food_energic(sh_1, sh_2):
    """
    Подсчёт энергетической ценности для имеющейся еды
    (файл с двумя листами: Справочник и Раскладка).
    """

    # - 1: Вводим переменные (словари, списки, данные из файла).
    d = {}
    vals_energic = [sh_1.row_values(rownum) for rownum in range(sh_1.nrows)]
    vals_food = [sh_2.row_values(rownum) for rownum in range(sh_2.nrows)]

    # - 1.1: Заполняем словарь значениями (вес/ккал/Б/Ж/У).
    for j in vals_food[1:]:
        if len(j) > 1:
            try:
                if j[0] not in d:
                    d[j[0]] = str(j[1])
                else:
                    d[j[0]] = str(float(d[j[0]]) + float(j[1]))
            except ValueError:
                continue
    for j in vals_energic[1:]:
        if len(j) > 4:
            if j[0] in d:
                try:
                    for score in j[1:5]:
                        if score == '':
                            score = 0
                        d[j[0]] += f'/{float(score) / 100}'
                except ValueError:
                    continue

    # - 2: Считаем суммарное количество Кккал/Б/Ж/У; округляем.
    sp_out = [0, 0, 0, 0]
    for value in d.values():
        energic = value.split('/')[1:5]
        weight = value.split('/')[0]
        i = 0
        while i < 4:
            sp_out[i] += float(energic[i]) * float(weight)
            i += 1
    str_out = ''
    for result in sp_out:
        str_out += f'{int(result)} '

    return str_out


def food_energic_all_days(sh_1, sh_2):
    """
    Подсчёт энергетической ценности для имеющейся еды на каждый день похода.
    (файл с двумя листами: Справочник и Раскладка).
    """

    # - 1: Вводим переменные (словари, списки, данные из файла).
    day_lst = []
    d_out = {}
    vals_energic = [sh_1.row_values(rownum) for rownum in range(sh_1.nrows)]
    vals_food = [sh_2.row_values(rownum) for rownum in range(sh_2.nrows)]

    # - 1.1: Создаём список дней.
    for j in vals_food[1:]:
        if j[0] not in day_lst:
            day_lst.append(int(j[0]))
    day_lst.sort()

    # - 2: Считаем суммарное количество Кккал/Б/Ж/У; округляем (для каждого дня).
    for h in day_lst:

        # - 2.1: Заполняем словарь значениями (вес/ккал/Б/Ж/У), (для текущего дня).
        d = {}
        for j in vals_food[1:]:
            if j[0] == h:
                if len(j) > 2:
                    try:
                        if j[1] not in d:
                            d[j[1]] = str(j[2])
                        else:
                            d[j[1]] = str(float(d[j[1]]) + float(j[2]))
                    except ValueError:
                        continue
        for j in vals_energic[1:]:
            if len(j) > 4:
                if j[0] in d:
                    try:
                        for score in j[1:5]:
                            if score == '':
                                score = 0
                            d[j[0]] += f'/{float(score) / 100}'
                    except ValueError:
                        continue

        # - 2.2: Считаем суммарное количество Кккал/Б/Ж/У; округляем (для текущего дня).
        sp_out = [0, 0, 0, 0]
        for value in d.values():
            energic = value.split('/')[1:5]
            weight = value.split('/')[0]
            i = 0
            while i < 4:
                sp_out[i] += float(energic[i]) * float(weight)
                i += 1
        str_out = ''
        for result in sp_out:
            str_out += f'{int(result)} '
        str_out = str_out.rstrip(' ')
        d_out[h] = str_out

    day_lst_out = []
    for k in day_lst:
        day_lst_out.append(d_out[k])
    return day_lst_out