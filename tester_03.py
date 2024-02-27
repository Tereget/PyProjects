import os

from module_03.osm_xml import FindingInformationInXML


rdir = 'module_03/result/'
sdir = 'module_03/src/'

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)

    x = FindingInformationInXML('map2.osm', sdir)

    # map1.osm
    res = str(x.score_tag_in_node())
    rfile = rdir + 'score_tag_in_node.txt'
    with open(rfile, 'w') as ouf:
        ouf.write(res)

    # map2.osm
    res = str(x.score_azs_on_node())
    rfile = rdir + 'score_azs_on_node.txt'
    with open(rfile, 'w') as ouf:
        ouf.write(res)

    # map2.osm
    res = str(x.score_azs_all())
    rfile = rdir + 'score_azs_all.txt'
    with open(rfile, 'w') as ouf:
        ouf.write(res)