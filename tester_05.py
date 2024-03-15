import os

from module_05.mk_html import run
from module_05.mk_html import MakeMT
from module_05.mk_html import MakeMTWithLink


"""
1). При запуске тестера запускается сервак, доступный по адресу: http://localhost:8000/
2). Ссылка ведёт в корневой каталог проекта.
3). Результирующие странички находятся в module_05/result/ (их можно открыть, как по старинке, 
    так и через сервак (рекомендуется). 
4). Если откроешь страничку "mt_link.html", надо обязательно перейти по ссылке "21".
5). Работу функции index_html() корректно проверять через сервак 
    по пути: module_05/result/num_by_word/ (такого условие задачи).
"""


def write(dir, res, name):
    with open(f'{dir}{name}', 'w') as ouf:
        ouf.write(res)


rdir = os.path.join('module_05', 'result', '')
nbw = os.path.join(rdir, 'num_by_word', '')

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)
    os.makedirs(nbw, exist_ok=True)

    x1 = MakeMT()
    x2 = MakeMTWithLink()

    res1 = x1.mt_text()
    res2 = x1.index_html()
    res3 = x2.mt_link()

    write(rdir, res1, 'mt_text.html')
    write(nbw, res2, 'index.html')
    write(rdir, res3, 'mt_link.html')

    run()