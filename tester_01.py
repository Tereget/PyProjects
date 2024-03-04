import os

from module_01.web import WordCounterOnTheSite


rdir = os.path.join('module_01/result/')
site_01 = 'https://stepik.org/media/attachments/lesson/209717/1.html'
site_02 = 'https://ru.wikipedia.org/wiki/Python'
site_03 = 'https://stepik.org/media/attachments/lesson/209719/2.html'
site_04 = 'https://stepik.org/media/attachments/lesson/209723/4.html'
word = 'Python'

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)

    x = WordCounterOnTheSite(site_04)

    res_01 = x.total_score(word)
    res_02 = x.visible_on_the_site(word)
    res_03 = x.frequent_line_in_code_tag()
    res_04 = x.sum_of_cell_values()

    with open(f'{rdir}results.txt', 'w') as ouf:
        ouf.write(f'Total score:\n{res_01}\n\n\nVisible on the site:\n{res_02}\n\n\n'
                  f'Frequent line in code tag:\n{res_03}\n\n\n'
                  f'Sum of cell values:\n{res_04}')


