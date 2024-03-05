import os

import xmltodict


class FindingInformationInXML:
    def __init__(self, file_name):
        # Получаем данные из файла в текстовом виде.
        if os.path.isfile(file_name):
            with open(file_name, 'r', encoding='utf8') as inf:
                xml = inf.read()
            self.parsedxml = xmltodict.parse(xml)
        else:
            self.parsedxml = None


    def score_tag_in_node(self):
        """
        Количество точечных объектов с вложенным тэгом "tag"/без тэга.
        """

        if self.parsedxml == None:
            return 'Файл не идентифицирован'

        score_plus = 0
        score_minus = 0
        for node in self.parsedxml['osm']['node']:
            if 'tag' in node:
                score_plus += 1
            else:
                score_minus += 1
        return f'{str(score_plus)} {str(score_minus)}'



    def score_azs_on_node(self, tag='node'):
        """
        Количество заправок (точечные объекты).
        """

        if self.parsedxml == None:
            return 'Файл не идентифицирован'

        score_azs = 0
        for node in self.parsedxml['osm'][tag]:
            if 'tag' in node:
                nt = node['tag']
                if isinstance(nt, dict):
                    if nt['@k'] == 'amenity' and nt['@v'] == 'fuel':
                        score_azs += 1
                else:
                    for tag in nt:
                        if tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                            score_azs += 1

        return score_azs



    def score_azs_all(self):
        """
        Количество заправок (общее количество).
        """

        if self.parsedxml == None:
            return 'Файл не идентифицирован'

        score_azs = 0
        for point in self.parsedxml['osm']:
            score_azs += self.score_azs_on_node(point)

        return score_azs

