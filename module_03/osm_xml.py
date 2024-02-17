import xmltodict


class FindingInformationInXML:
    def __init__(self, file_name):

        # Получаем данные из файла в текстовом виде.
        try:
            with open(file_name, 'r', encoding='utf8') as inf:
                xml = inf.read()
            self.parsedxml = xmltodict.parse(xml)
        except Exception:
            raise Exception('Файл не найден')



    """
    Количество точечных объектов с вложенным тэгом "tag"/без тэга.
    """
    def score_tag_in_node(self):
        score_plus = 0
        score_minus = 0
        for node in self.parsedxml['osm']['node']:
            if 'tag' in node:
                score_plus += 1
            else:
                score_minus += 1
        return str(score_plus) + ' ' + str(score_minus)



    """
    Количество заправок (точечные объекты).
    """
    def score_azs_on_node(self):
        score_azs = 0
        for node in self.parsedxml['osm']['node']:
            if 'tag' in node:
                score = 0
                if type(node['tag']) == dict:
                    node['tag'] = [node['tag']]
                for tag in node['tag']:
                    try:
                        if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                            score_azs += 1
                    except TypeError:
                        continue
        return score_azs



    """
    Количество заправок (общее количество).
    """
    def score_azs_all(self):
        score_azs = 0
        for point in self.parsedxml['osm']:
            for azs in self.parsedxml['osm'][point]:
                if 'tag' in azs:
                    score = 0
                    if type(azs['tag']) == dict:
                        azs['tag'] = [azs['tag']]
                    for tag in azs['tag']:
                        try:
                            if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                                score_azs += 1
                        except TypeError:
                            continue
        return score_azs





"""
Тестеры.
"""
# x = FindingInformationInXML('map2.osm')
# print(x.score_tag_in_node())              # map1.osm
# print(x.score_azs_on_node())              # map2.osm
# print(x.score_azs_all())                  # map2.osm