import os

from module_05.mk_web_server import run
from module_05.mk_mt_text import MakeMT
from module_05.mk_mt_link import MakeMTWithLink


"""
1). При запуске тестера запускается сервак, доступный по адресу: http://localhost:8000/
2). Если перейти по ссылке, можно будет увидеть весь проект.
3). Результирующие странички находятся в module_05/result/ (их можно открыть, как по старинке, 
    так и через сервак (рекомендуется). 
4). Если откроешь страничку "mt_link.html", надо обязательно перейти по ссылке "21".
5). Работа функции index_html() корректно проверять через сервак 
    по пути: module_05/result/num_by_word/ (такого условие задачи).
"""


rdir = os.path.join('module_05/result/')
nbw = os.path.join(f'{rdir}num_by_word/')

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)
    os.makedirs(nbw, exist_ok=True)

    x1 = MakeMT()
    x2 = MakeMTWithLink()

    res1 = x1.mt_text()
    res2 = x1.index_html()
    res3 = x2.mt_link()

    with open(f'{rdir}mt_text.html', 'w') as ouf:
        ouf.write(res1)

    with open(f'{nbw}index.html', 'w') as ouf:
        ouf.write(res2)

    with open(f'{rdir}mt_link.html', 'w') as ouf:
        ouf.write(res3)

    run()