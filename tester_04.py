import os

from module_04.graphs_with_pyplot import VisualGraphs


rdir = os.path.join('module_04/result/')

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)

    x = VisualGraphs()

    res = x.original()
    rfile = f'{rdir} original.png'
    res.savefig(rfile)

    res = x.double()
    rfile = f'{rdir} double.png'
    res.savefig(rfile)

    res = x.tee()
    rfile = f'{rdir} tee.png'
    res.savefig(rfile)