import xmltodict


class FindingInformationInXML:
    def __init__(self, file_name, path_name='module_03/cgi-bin/'):

        # Получаем данные из файла в текстовом виде.
        try:
            with open(path_name + file_name, 'r', encoding='utf8') as inf:
                xml = inf.read()
            self.parsedxml = xmltodict.parse(xml)
        except:
            raise Exception('Файл не найден')



    def score_tag_in_node(self):
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
        return str(score_plus) + ' ' + str(score_minus)



    def score_azs_on_node(self):
        """
        Количество заправок (точечные объекты).
        """

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



    def score_azs_all(self):
        """
        Количество заправок (общее количество).
        """

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

