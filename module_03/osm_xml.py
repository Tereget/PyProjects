import os

import xmltodict


def dekor(func):
    """
    Трай-эксепт, потому что у функций разное количество аргов. Если убирать трай-эксепт, то либо
    придётся дубликат декоратора делать, либо вносить фиктивные арги в функции для выравнивания.
    """

    def wrapper(self, *args):
        if self.parsedxml == None:
            return 'Файл не идентифицирован'
        return func(self, *args)

    return wrapper


class FindingInformationInXML:
    def __init__(self, file_name):
        # Получаем данные из файла в текстовом виде.
        if os.path.isfile(file_name):
            with open(file_name, 'r', encoding='utf8') as inf:
                xml = inf.read()
            self.parsedxml = xmltodict.parse(xml)
        else:
            self.parsedxml = None
            print('Файл не идентифицирован')


    @dekor
    def score_tag_in_node(self, *_):
        """
        Количество точечных объектов с вложенным тэгом "tag"/без тэга.
        """
        score_plus = 0
        score_minus = 0
        for node in self.parsedxml['osm']['node']:
            if 'tag' in node:
                score_plus += 1
            else:
                score_minus += 1
        return f'{score_plus} {score_minus}'

    @dekor
    def score_azs_on_node(self, tag='node', *_):
        """
        Количество заправок (точечные объекты).
        """
        score_azs = 0
        for node in self.parsedxml['osm'][tag]:
            if 'tag' in node:
                nt = node['tag']
                if isinstance(nt, dict):
                    nt = [nt]
                for tag in nt:
                    if tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                        score_azs += 1
        return score_azs

    @dekor
    def score_azs_all(self, *_):
        """
        Количество заправок (общее количество).
        """
        score_azs = 0
        for point in self.parsedxml['osm']:
            score_azs += self.score_azs_on_node(point)
        return score_azs
