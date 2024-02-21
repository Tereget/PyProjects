import os
from osm_xml import FindingInformationInXML

if __name__ == "__main__":
    print("Hello, World!")

    try:
        os.mkdir('result')
    except FileExistsError:
        ()

    x = FindingInformationInXML('map1.osm')

    """
    # map1.osm
    with open('result/score_tag_in_node.txt', 'w') as ouf:               
        ouf.write(str(x.score_tag_in_node()))
    """

    """
    # map2.osm
    with open('result/score_azs_on_node.txt', 'w') as ouf:
        ouf.write(str(x.score_azs_on_node()))
    """

    """
    # map2.osm
    with open('result/score_azs_all.txt', 'w') as ouf:
        ouf.write(str(x.score_azs_all()))
    """
