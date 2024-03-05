import re
import urllib.error
from urllib.request import urlopen
from collections import defaultdict

import requests
from bs4 import BeautifulSoup


def html_cleaning(html):

    s = html[html.index('<body'):]  # Сносим заголовок.

    y = r'<script'  # Сносим скрипты.
    z = re.findall(y, s)
    for script in z:
        s1 = s.index('<script')
        s2 = s.index('/script>') + 8
        s = s[:s1] + s[s2:]

    Python_re = r'(\<[^\<\>]*\>)'  # Сносим остальную системную инфу.
    z = re.findall(Python_re, s)
    for el in z:
        if el in s:
            s = s.replace(el, '*')

    return s                       # Очищенная версия.



class WordCounterOnTheSite:
    def __init__(self, url):
        # Получаем html-код страницы.
        if requests.get(url).status_code == 404:
            self.error = f'Сайт: {url} - не найден.'
        else:
            self.error = None
            self.html = urlopen(str(url), ).read().decode('utf-8')
            self.clear_html = html_cleaning(self.html)


    def total_score(self, word):
        """
        Количество всех вхождений слова, с учётом
        системной инфы (с учётом регистра).
        """
        if self.error:
            return self.error
        return f'Количество вхождений: {str(self.html.count(word))}'    # Ответ.



    def visible_on_the_site(self, word):
        """
        Количество вхождений слова, которые видно
        в браузере (с учётом регистра).
        """
        if self.error:
            return self.error
        return f'Количество вхождений: {str(self.clear_html.count(word))}'       # Ответ.



    def frequent_line_in_code_tag(self):
        """
        Нахождение максимально часто встречающихся строк между
        тегами <code> и </code> (вывод в алфавитном порядке).
        """
        if self.error:
            return self.error
        s = self.html                   # Короткий вид для переменной.

        # Находим все нужные строки по условию.
        y = r'\<code\>\w+<\/code\>'
        z = re.findall(y, s)

        # Если на сайте нет таких строк:
        if len(z) == 0:
            return 'Строки с тегами "code" не найдены.'

        # Считаем количество повторений для каждой строки.
        d = defaultdict(int)
        for code in z:
            d[code] += 1

        # Вытаскиваем максимально часто встречающиеся строки.
        max_value = max(d.values())
        d = {k: v for k, v in d.items() if v == max_value}
        j = []
        for key in d.keys():
            j.append(key)

        # Убираем теги и сортируем список.
        new_j = []
        for designs in j:               #
            designs = designs.removeprefix('<code>')
            designs = designs.removesuffix('</code>')
            new_j.append(designs)
        new_j.sort()
        str_out = ' '.join(new_j)
        return str_out                  # Ответ.



    def sum_of_cell_values(self):
        """
        Суммирование значений ячеек таблицы формата html.
        """
        if self.error:
            return self.error

        # Вытаскиваем ячейки с сайта.
        soup = BeautifulSoup(self.html, 'html.parser')
        z = soup.find_all('td')

        # Если на сайте нет ячеек таблицы:
        if len(z) == 0:
            return 'Ячейки таблицы не найдены.'

        # Суммируем значения ячеек.
        sum = 0
        unk_str = 0
        for cell in z:
            cell = str(cell.string)
            cell = cell.removeprefix(' ')
            cell = cell.removesuffix(' ')
            if cell.isnumeric():
                sum += int(cell)
            else:
                unk_str += 1
        return (f'Сумма значений всех ячеек: {str(sum)}\nКоличество ячеек, не являющихся числами: {str(unk_str)}')     # Ответ.
