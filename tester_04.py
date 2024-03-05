import os

from module_04.graphs_with_pyplot import sinus
from module_04.graphs_with_pyplot import sinus_shifted
from module_04.graphs_with_pyplot import osm_points


rdir = os.path.join('module_04/result/')

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)

    res = sinus()
    rfile = f'{rdir}sinus.png'
    res.savefig(rfile)

    res = sinus_shifted()
    rfile = f'{rdir}sinus_shifted.png'
    res.savefig(rfile)

    res = osm_points()
    rfile = f'{rdir}osm_points.png'
    res.savefig(rfile)