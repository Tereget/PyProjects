import os
from graphs_with_pyplot import VisualGraphs

if __name__ == "__main__":
    print("Hello, World!")

    try:
        os.mkdir('result')
    except FileExistsError:
        ()

    x = VisualGraphs()

    # x.original()
    # x.double()
    # x.tee()