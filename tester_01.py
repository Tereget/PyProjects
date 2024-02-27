import os

from module_01.web import WordCounterOnTheSite


rdir = 'module_01/result/'

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)

    x = WordCounterOnTheSite('https://stepik.org/media/attachments/lesson/209723/4.html')

    # https://stepik.org/media/attachments/lesson/209717/1.html
    res = x.total_score('Python')
    rfile = rdir + 'total_score.txt'
    with open(rfile, 'w') as ouf:
        ouf.write(res)

    # https://ru.wikipedia.org/wiki/Python
    res = x.visible_on_the_site('Python')
    rfile = rdir + 'visible_on_the_site.txt'
    with open(rfile, 'w') as ouf:
        ouf.write(res)

    # https://stepik.org/media/attachments/lesson/209719/2.html
    res = x.frequent_line_in_code_tag()
    rfile = rdir + 'frequent_line_in_code_tag.txt'
    with open(rfile, 'w') as ouf:
        ouf.write(res)

    # https://stepik.org/media/attachments/lesson/209723/4.html
    res = x.sum_of_cell_values()
    rfile = rdir + 'sum_of_cell_values.txt'
    with open(rfile, 'w') as ouf:
        ouf.write(res)