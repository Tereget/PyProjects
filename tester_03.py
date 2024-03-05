import os

from module_03.osm_xml import FindingInformationInXML


rdir = os.path.join('module_03/result/')
sdir = os.path.join('module_03/src/')
map_01 = 'map1.osm'
map_02 = 'map2.osm'

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)

    x1 = FindingInformationInXML(map_01, sdir)
    x2 = FindingInformationInXML(map_02, sdir)

    res_01 = str(x1.score_tag_in_node())
    res_02 = str(x2.score_azs_on_node())
    res_03 = str(x2.score_azs_all())

    with open(f'{rdir}results.txt', 'w') as ouf:
        ouf.write(f'Score tag in node:\n{res_01}\n\n\nScore azs on node:\n'
                  f'{res_02}\n\n\nScore azs all:\n{res_03}')

