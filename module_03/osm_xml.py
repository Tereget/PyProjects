import xmltodict


class FindingInformationInXML:
    def __init__(self, file_name, path_name='module_03/src/'):

        # Получаем данные из файла в текстовом виде.
        try:
            with open(f'{path_name}{file_name}', 'r', encoding='utf8') as inf:
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
        return f'{str(score_plus)} {str(score_minus)}'



    def score_azs_on_node(self, tag='node'):
        """
        Количество заправок (точечные объекты).
        """

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

        score_azs = 0
        for point in self.parsedxml['osm']:
            score_azs += self.score_azs_on_node(point)

        return score_azs

