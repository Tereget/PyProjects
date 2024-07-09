import os

from args_from_file import arg_pars
from module_03.osm_xml import FindingInformationInXML


rdir = os.path.join('module_03', 'result', '')
sdir = os.path.join('module_03', 'src', '')
map_01 = f'{sdir}map1.osm'
map_02 = f'{sdir}map2.osm'

if __name__ == "__main__":
    print("Hello, World!")

    rdir = os.path.join('module_03', 'result', '')
    sdir = os.path.join('module_03', 'src', '')
    arg_dict = arg_pars('--config_path')
    map_01 = f'{sdir}{arg_dict["map_01"]}'
    map_02 = f'{sdir}{arg_dict["map_02"]}'

    os.makedirs(rdir, exist_ok=True)

    x1 = FindingInformationInXML(map_01)
    x2 = FindingInformationInXML(map_02)

    res_01 = x1.score_tag_in_node()
    res_02 = x2.score_azs_on_node()
    res_03 = x2.score_azs_all()

    with open(f'{rdir}results.txt', 'w') as ouf:
        ouf.write(f'Score tag in node:\n{res_01}\n\n\nScore azs on node:\n'
                  f'{res_02}\n\n\nScore azs all:\n{res_03}')

