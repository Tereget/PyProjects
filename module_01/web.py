import re
from urllib.request import urlopen
from collections import defaultdict

import numpy as np
import requests
from bs4 import BeautifulSoup


def dekor(func):
    def wrapper(self, *args):
        if self.error:
            return self.error
        return func(self, *args)

    return wrapper


def html_cleaning(html):
    """
    HTML-страница без системных тэгов.
    """

    s = html[html.index('<body'):]  # Сносим заголовок.

    y = r'<script'  # Сносим скрипты.
    z = re.findall(y, s)
    for script in z:
        s1 = s.index('<script')
        s2 = s.index('/script>') + 8
        s = s[:s1] + s[s2:]

    python_re = r'(\<[^\<\>]*\>)'  # Сносим остальную системную инфу.
    z = re.findall(python_re, s)
    for el in z:
        if el in s:
            s = s.replace(el, '*')

    return s


class WordCounterOnTheSite:
    def __init__(self, url):
        # Получаем html-код страницы.
        if requests.get(url).status_code == 404:
            self.error = f'Сайт: {url} - не найден.'
        else:
            self.error = None
            self.html = urlopen(url).read().decode('utf-8')
            self.clear_html = html_cleaning(self.html)




    @dekor
    def total_score(self, word='@52%$#', *_):
        """
        Количество всех вхождений слова, с учётом
        системной инфы (с учётом регистра).
        """
        return f'Количество вхождений: {self.html.count(word)}'


    @dekor
    def visible_on_the_site(self, word='@52%$#', *_):
        """
        Количество вхождений слова, которые видно
        в браузере (с учётом регистра).
        """
        return f'Количество вхождений: {self.clear_html.count(word)}'


    @dekor
    def frequent_line_in_code_tag(self, tag='code', *_):
        """
        Нахождение максимально часто встречающихся строк между
        тегами <...> и </...> (вывод в алфавитном порядке).
        Тэг по умолчанию: "code".
        """
        s = self.html

        # Находим все нужные строки по условию.
        y = rf'\<{tag}\>\w+<\/{tag}\>'
        z = re.findall(y, s)

        # Если на сайте нет таких строк:
        if not z:
            return f'Строки с тегами "{tag}" не найдены.'

        """
        str_out = ''
        npu = np.unique(z, return_counts=True)
        for el in np.where(npu[1] == npu[1].max(), npu[0], ''):
            if el:
                str_out += str(el).removeprefix(f'<{tag}>').removesuffix(f'</{tag}>') + ' '
        return str_out
        """

        # Считаем количество повторений для каждой строки.
        d = defaultdict(int)
        for code in z:
            d[code.removeprefix(f'<{tag}>').removesuffix(f'</{tag}>')] += 1

        # Вытаскиваем максимально часто встречающиеся строки.
        max_value = max(d.values())
        d = {k: v for k, v in d.items() if v == max_value}
        j = list(d.keys())
        j.sort()
        str_out = ' '.join(j)

        return str_out


    @dekor
    def sum_of_cell_values(self, *_):
        """
        Суммирование значений ячеек таблицы формата html.
        """

        # Вытаскиваем ячейки с сайта.
        soup = BeautifulSoup(self.html, 'html.parser')
        z = soup.find_all('td')

        # Если на сайте нет ячеек таблицы:
        if not z:
            return 'Ячейки таблицы не найдены.'

        # Суммируем значения ячеек.
        sum = 0
        unk_str = 0
        for cell in z:
            cell = str(cell.string).strip(' ')
            if cell.isnumeric():
                sum += int(cell)
            else:
                unk_str += 1
        return f'Сумма значений всех ячеек: {sum}\nКоличество ячеек, не являющихся числами: {unk_str}'
