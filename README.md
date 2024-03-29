# Парсинг файлов:

#### Описание модулей:
- Модуль №1: Анализ файлов html: поиск слов; поиск строк с конкретным тегом (на примере тега \<code\>); подсчёт суммы значений ячеек таблицы (если таковые имеются).
- Модуль №2: Анализ таблиц excel: подсчёт значений по одному листу/по нескольким листам/по нескольким файлам; конвертация файлов в универсальный формат xls.
- Модуль №3: Анализ файлов xml: подсчёт объектов на фрагменте карты (точечных, а также - общего количества).
- Модуль №4: Анализ и обработка графиков: изменение разрешения/локации легенды.
- Модуль №5: Запуск сервера и генерация html.


#### Установка интерпретатора (python v.3.9):
```commandline

OS Linux:
	sudo apt update
	sudo apt install software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt install python3.9
	
OS Windows:
	https://bangbangeducation.ru/point/razrabotka/kak-ustanovit-python/#2
	
OS MacOS:
	$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	$ brew install python[version]
```

#### Установка окружения (python v.3.9):
```commandline

C помощью vrtualenv:
	pip3.9 install virtualenv
	virtualenv kitty
	source kitty/bin/activate
	pip3.9 install -r ./requirements.txt
	
C помощью venv:
	sudo apt install python3-venv
	python3.9 -m venv kitty
	source kitty/bin/activate
	pip3.9 install -r ./requirements.txt
	
С помощью conda:
	wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
	bash Anaconda3-2024.02-1-Linux-x86_64.sh
	source ~/.bashrc
	rm Anaconda3-2024.02-1-Linux-x86_64.sh 
	conda env create -n kitty -f environment.yml  
	conda activate kitty
```


#### Тестирование:
```commandline
	python3.9 tester_01.py
	python3.9 tester_02.py
	python3.9 tester_03.py
	python3.9 tester_04.py
	python3.9 tester_05.py
```


# CODE REVIEW:

## TASK_01	[+]

### 1. Main / Master [+]
- Должна быть одна главная ветка: master или main. Сейчас одну надо удалить. 
- В след раз чтобы не было раздвоения нужно создать пустой удаленный репозиторий. Там будет ветка main. После этого в локальной папке необходимо выполнить следующий код:

```
git init
git remote add origin <URL>
git pull origin main
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main

```

### 2. .gitignore [+]
- Папка .idea должна быть в гитигноре. Удалить ее из репозитория


### 3. Repository: description [+]
- Когда создается репозиторий, нужно добавить очень краткое описание в графе about. Она отображается справа сверху на сайте. Сейчас она пустая.
- В текущем файле README в отдельной графе создать краткое описание проекта: что делает каждый модуль. 


### 4. Tree structure [+]
- название папки не должно начинаться с цифры: 1_module -> module_1
- при нумерации надо добавлять ведущие нули: module_1 -> module_01
- module_02:
	- не понятно, где исходные файлы, а где результирующие -> src - для файлов исходников; result - для полученных файлов 
- module_03:
	- аналогично


### 5. requirements.txt [+]
- надо добавить 


## TASK_02 [+]

### 1. Code	[+]
- Сначала импорты всех модулей. потом импорты частей:
```
import os
import re
...
from holodilnik import Putin
...
```

- Описание функций дается внутри тела функции:
```
def body():
	"""
	Dead body of the former Russian President
	"""
```
- Разбить каждую задачу на 2 файла:
	- функции, которые выполняют задачу
	- файл-тестер, который импортирует функции из соседнего файла и запускает их на входных данных
	- результат работы тестера выводить не принтом в консоль, а сохранять в файл в папку result!
	- путь до входных файлов в тестере выделить в глобальный аргумент
	- в тестере добавить конструкцию `if __name__ == "__main__":`: [StackOverflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
- module_02: слишком длинные функции внутри класса. Заменить так:
```
def salary_calculation(self):
	sheet = self.wb.sheet_by_index(0)
	return salary_calculation(seet)
```
где `salary_calculation` определена вне класса так:
```
def salary_calculation(sh):

        # - 1: Вводим переменные (словари, данные из файла).
        d_region = {}
        d_prof = {}
        vals = [sh.row_values(rownum) for rownum in range(sh.nrows)]

        # - 1.1: Создаём словарь для текущего листа; вносим туда все виды профессий.
        for profs in vals[0][1:]:
            d_prof[profs] = 0

        # - 1.2: Вносим в словарь с медианой названия регионов; заполняем значения обоих словарей.
        for j in vals[1:]:
            numbers = j[1:]
            if len(numbers) > 0:
                try:
                    z = 0
                    for key, value in d_prof.items():
                            d_prof[key] += numbers[z]
                            z += 1
                    numbers.sort()
                    central_numb = float(numbers[len(numbers) // 2])
                    central_numb_2 = float(numbers[len(numbers) // 2 - 1])
                    if len(numbers) % 2 != 0:
                        d_region[j[0]] = central_numb
                    else:
                        d_region[j[0]] = (central_numb + central_numb_2) / 2
                except ValueError:
                    continue

        # - 2: Узнаём название региона с самой высокой медианой.
        p = 0
        region_output = ''
        for key, value in d_region.items():
            if value > p:
                region_output = key
                p = value
            elif value == p:
                region_output += ', ' + key

        # - 3: Узнаём название профессии с самой высокой оплатой по регионам.
        p = 0
        prof_output = ''
        for key, value in d_prof.items():
            if value > p:
                prof_output = key
                p = value
            elif value == p:
                prof_output += ', ' + key
        out = region_output + ' ' + prof_output

        # - 4: Получаем ответ.
        return out
```


### 2. README [+]
- Описание модулей сделать списком
- Добавить блок кода с командой по установке окружения из requirements.txt: [MarkDownCodeBlock](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code-and-syntax-highlighting)



## TASK_03 [+]

### 1. Code [+]

- кажется, что есть неиспользуемые импорты в некоторых файлах. PyCharm должен выделять неиспользуемые импорты
- импорты из локальных файлов делаются в самом конце [Pep8](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html#section-8)
- `Try except Exception` - бессмысленно. Либо `try except` либо `try except Exception as e`, чтобы потом иметь возможность обращаться к `e`. `Try except` это всегда плохо. Можно только использовать как временный костыль, но потом всегда надо избавляться от него.
- module_02: непонятно, почему `def xls_converting(path_file_name)` не ушла в отдельный файл
- файлы-тестеры:
	- закомментировано применение методов и сохранение результатов. Код должен быть полностью воспроизводимым, поэтому надо вернуть эти строки.
	- результат исполнения методов лучше сначала сохранять в переменную, а потом эту переменную записывать в файл.
	- не все результаты применения методов записываются в файл -- исправить.
	- Если не хочешь, чтобы папка перезаписывалась, используй `os.makedirs(exists_ok=False)` без `try except`: [Stackoverflow](https://stackoverflow.com/questions/13819496/what-is-the-difference-between-makedirs-and-mkdir-of-os).
	- пути до файлов src и result все еще не выделены в отдельные аргументы. Я хочу, чтобы ты столбиком записал их в начале файла -- они потом нам понадобятся.
	- файлы-тестеры запускаются снаружи питона через командную строку. Для этого пишется `python <название_файла>.py`. Поэтому все тестеры обычно лежат в корневой папке, чтобы не бегать через cd каждый раз. Перенести все тестеры в корень. После этого импорты локальных файлов пойдут по пизде, надо будет их исправить. Более того, пойдут по пизде все пути сохранения -- нужно будет дописывать префикс пути. Можно выделить префикс в отдельную переменную, чтобы потом плюсовать ее к названию каждого файла.


### 2. README [+]
- после заголовка проекта добавить подзаголовок "Описание модулей" перед описанием модулей. (Подзаголовок того же ранга, что "Установка окружения") 
- установка окружения:
	- указать версию питона до строки pip install
	- при выполнении pip install пакеты установятся в текущее окружения. Добавить команду, позволяющую сначала создать пустое окружение с требуемоей версией питона (venv, pip или conda)
- добавить заголовок "Тестирование". В этом разделе для каждого модуля записать команду запуска тестовых файлов: `python <название_файла>.py`



## TASK_04 [+]

### 1. README [+]

- Установка окружения:
	- папка создается, если еще нет проекта. У нас уже есть проект, поэтому строчки mkdir и cd надо убрать.
	- название окружения надо поменять: venv можно спутать с библиотекой.
	- надо подписать, что это вариант создания окружения с помощью virtualenv
	- добавить аналогичную инструкцию по созданию окружения, но с использованием venv вместо virtualenv
	- в отличии от conda, venv и virtualenv создают окружение на базе текущего интерпретатора. Ты здесь подразумеваешь, что у человека стоит python 3.9. Нужно перед установкой окружения добавить команду по установке python3.9


### 2. Code [+]

- общие замечания: [+]
	- используй f-string вместо str1 + str2 + str3... [docs](https://docs.python.org/3/tutorial/inputoutput.html)
	- надо выебнуться и сделать код кроссплатформенным. На винде ебучий слеш в путях пишется в обратную сторону, код поднимет ошибку. Используй это: [StackOverflow](https://stackoverflow.com/questions/10918682/platform-independent-path-concatenation-using)
	- `if len(numbers) > 0:` - достаточно писать `if numbers:`

- module_01: [+]
	- tester: [+]
		- 'https://stepik.org/media/attachments/lesson/209723/4.html' в глобальный аргумент	
		- 'Python' в глобальный аргумент
		- что означают закомментированные веб-сайты ?
	- web: [+]
		- [1](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_01/web.py#L72-L78) используй defaultdict из collections 
		- [2](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_01/web.py#L80-L89) я не понимаю, что здесь происходит, но мне кажется, что ты пытаешься взять те ключи словаря, значение которых равняется максимуму из всех значений словаря. Ты можешь отсортировать словарь по значению ключа [StackOverflow](https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value)
		- [3](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_01/web.py#L98-L100) используй `" ".join(list)`
		- [4](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_01/web.py#L125-L129) тебе нужен `isnumeric` [StackOverflow](https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth)
		- [5](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_01/web.py#L29) Логичнее в ините в качестве второго атрибута сохранить очищенную версию html. А внутри этого метода просто дергать count у этого атрибута.
		- Давай не будем спамить результирующие файлы. Применим все методы, соберем результат в переменные. А потом все это сохраним в один файл-отчет, где будет расписано, какая функция выполнялась, что она делала, и вхождение какого слова она искала.

- module_02: [+]
	- tester: [+]
		- 'trekking3.xlsx' в глобальный аргумент
		- импорты отдельно: salary_calculation_using_tables и TableProcessing
		- `if res == 'Некорректные данные в файле':` - пусть просто будет res = False, если там некорректно что-то 
	- excel: [+]
		- откуда взялись файлы src? Если это был архив, надо добавить этап разархивирования в код. Гугли, как это делается в ПИТУХОНЕ.
		- нет никакого смысла подавать раздельно путь до папки и название файла, а потом склеивать (Россию). Подавай сразу весь путь до файла.
		- try except внутри try except. Совсем ебнулся. Убирай все это. Если сама функция бросает ошибку, добавь в except конкретное исключение.
		- [1](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_02/excel.py#L70) добавить условие на расширение файлов
		- [2](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_02/excel.py#L72) пути сначала проверяются с помощью os.path.isdir, os.path.ispath, чтобы не использовать try except. По такой же логике можно какой-нибудь функцией сначала проверять корректность веб-адреса, а потом подавать его в парсеры. Погугли, что для этого использовать. 
		- [3](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_02/excel.py#L82-L89) кажется, что в файлах есть некий паттерн и можно сразу обращаться к номеру ячейки ?
		- [4](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_02/excel.py#L92) добавляй имя и зп в два разных листа. После цикла создай датафрейм: `df = pd.DataFrame({"name": names, "salary": salaries}`. Дальше, это можно отсортировать и сохранить как сsv или excel. Погугли как.
	- funcs_for_excel:
		- соберусь с силами и проедусь катком в следующих коммитах.

- module_03: [+]
	- tester: [+]
		- 'map2.osm' - в глобальный аргумент
		- собираем вывод в одни файл с пояснением, что это за цифры. Как и в модуле 1
	- osm_xml: [+] (2 пункт: так должно быть? 3 пункт: я сделал даже лучше)
		- [1](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_03/osm_xml.py#L42) - `isinstance`
		- [2](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_03/osm_xml.py#L42-L44) - ??????
		- [3](https://github.com/Tereget/PyProjects/blob/608c8b52b37f6864247cfeb60167f8573365a04b/module_03/osm_xml.py#L60-L61) - если это словарь, может сразу перебирать ключ и значение ?

- module_04: [+]
	- graphs_with_pyplot.py: [+]
		- убрать класс, он тут вообще не нужен
		- назвать функции так, чтоб они лучше отражали суть: sinus, sinus_shifted, osm_points. Как-то так


## TASK_05 [+-?]

### 1. README [+?]

- дописать, что установка python3.9 написана для linux. [+]
- а на винде можно подобную хуйню провернуть ? [+?] - По винде - тупо ссылка. По маку - не проверенная хуйня.
- необязательная задача: разобраться и написать инструкцию по установке окружения с помощью conda. [YouTube](https://www.youtube.com/watch?v=wWw7PR-Cwuw), [Conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) [+] Есть подозрение, что env.yml устанавливает, кроме нужного - что-то ещё.


### 2. Code [+-?]

- общие замечания: [+?]
	- Внутри скобок в f-string может быть любой тип данных. Не нужно приводить его к str. Удалить. [+]
	- Удалить очевидные комментарии типо "ответ", "Короткий вид для переменной." [+?] Нет понимания "очевидности". node[tag] = [node[tag]] столь же очевидно, как и короткий вид, но без коммента ты не вдуплил.
	- Что за cgi-bin ? [+]
	- Ты уверен, что если подавать в os.path.join куски со слешами, он их заменит? Проверь на винде [+] Протестил: работает надёжно, как Василич.


- module_01: [+-?]
	- [1](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_01/web.py#L38) - зачем str ? если оставляешь, то делай еще до подачи в requests [+]
	- [2](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_01/web.py#L78) - альтернативно: `if not z` [+]
	- [3](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_01/web.py#L89-L91) - `j = [key for key in d.keys()]` или проще: `j = list(d.keys())` [+]
	- [4](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_01/web.py#L81-L91) - закомментировать это решение, чтобы не потерять, и попробовать это: [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html) с ключом return_counts. [+?] Оставил его закоментированным, так как считаю плохим: сэкономили несколько строк в обмен на трудозатратность. Долго вдуплял, как работают эти методы. После вдупления методы выглядеть проще не стали. В аналогичной ситуации я даже не вспомню про них.
	- [5](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_01/web.py#L94-L98) - норм. Еще можно так: `j = [line.removesuffix('<code>').removesuffix('</code>') for line in j]` [+]
	- [6](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_01/web.py#L131) - зачем возвращать кортеж, а не строку ? [+] Кортеж был до внедрения ф-стринг. Поправил.
	- [7](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_01/web.py#L47-L48) - чтобы не дублировать этот код в каждом методе, нужно вынести это в отдельный метод, и вызывать его в начале каждой функции. Аналогично в модуле 3. Желательно еще в ините оповещать принтом, что файл не найден. [+] (декоратор) Обсудили: решение с выносом функции выйдет ещё длиннее + не вижу смысла укорачивать короткоствол.
	- [8](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_01/web.py#L64) - в теории можно было бы еще в ключевой аргумент добавить 'code', и потом вставлять его в f-string везде, где он встречается. [+] Тут я тебя поправлю: не "в теории", а - "обязательно". Этот метод делает функцию универсальной.


- module_02: [+-]
	- [1](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/tester_02.py#L16-L18) - схуяли вне main? Зип файл! Винрары ваевале! [+]
	- [2](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/tester_02.py#L39) - isinstance [+] Нужна пояснительная бригада.
	- [3](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/tester_02.py#L38-L68) - ну это же пиздец. if else идентичен. это надо выносить в функцию. [+]
	- [4](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/tester_02.py#L70) - запись файла во время открытия другого файла. Вопрос: что нужно сделать с этой строкой ? [+] Спалил сам, когда сокращал полотно на предыдущем пункте)
	- [5](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/excel.py#L5C8-L6) - это где-то используется ? [+] В конвертации файла.
	- [6](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/excel.py#L16-L21) - модуль не принимает файлы с определенным расширением ? Надо проверить расширение до того, как подавать в модуль. [-] Не понял. Зачем проверять? И на что проверять? В данном сценарии я избавлен от этих вопросов. Код съедает, что может съесть, и трансформирует то, что - не может.
	- [7](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/funcs_for_excel.py#L5) - сделать 2 ключевых аргумента: read_path, save_path. передавать save_path тут: [8](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/excel.py#L19), предварительно вынеся его в аргумент. [-] Не понял совершенно.
	- [8](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/excel.py#L30) - а можно разделить эти ошибки ? [+] Не исключаю ситуаций, когда данное разделение сработает некорректно.
	- [9](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/excel.py#L43-L44) - справочник и раскладка вынести в ключевые аргументы [+]
	- [10](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/excel.py#L66) - нужен экранирующий \ перед первой точкой ? [+]
	- [11](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/excel.py#L65-L72) - вынести в отдельную функцию [+]
	- [12](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/excel.py#L93) - сортировать надо по имени колонки, которая есть в датафрейме. колонки 'name' нет. Кстати, можно сортировать по нескольким колонкам. для этого надо передать список с именами колонок. [+]
	- [13](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_02/excel.py#L89) - в чем смысл str(int()) ? [+] Инт - для округления. Стр - для записи без ф-стринг (убрал).
	- в папке src какой-то пиздец происходит. Надо удалить дубликаты папок. [+]
	- необязательная задача со звездочкой. Внутри функций salary_calculation, nutritious_food, food_energic, food_energic_all_days оставить только часть внутри try, убрать try except. Написать декоратор [Habr](https://habr.com/ru/companies/otus/articles/727590/), в котором будет try except, и принимаемая на вход функция будет вызываться внутри try. Навесить декоратор на перечисленные функции с помощью @. [+]


- module_03: [+]
	- [1](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/tester_03.py#L19-L21) - зачем str ? [+] Ебёт?
	- [2](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_03/osm_xml.py#L32) - ебучие str [+]
	- [3](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_03/osm_xml.py#L57C1-L59C1) - это пайчарм требует 3 строки пустых ? [+]
	- [4](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_03/osm_xml.py#L48-L54) - теперь я понял, что было. Меня смущало имено изменение словаря во время перебора словаря. Сейчас есть `nt = node['tag']`, поэтому после isinstance можно вернуть `nt = [nt]` [+]


- module_05: [+]
	- [1](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_05/mk_mt_text.py#L11) - лучше сделать self.start и self.finish [+]
	- [2](https://github.com/Tereget/PyProjects/blob/3bf42675d2a941414ddeb31ca56d50223a6166c3/module_05/mk_mt_text.py#L40) - str убрать [+]
	- может лучше объединить 3 py файла в один ? [+]


## TASK_06


- общие комментарии:
	
	- Задача 1: Установить в PyCharm одно из расширений по контролю стиля кода: flake8, pep8, pylint... [Хабр](https://habr.com/ru/articles/681370/). Проверить код с его помощью. Исправить основные ошибки. Обратить особое внимание на:
		- название переменных, функций и классов
		- try except
		- циклы
		- порядок импортов

Наиболее гнетущие исправления можно игнорировать, но обязательно ознакомиться и понять.


	- Задача 2: Задавать глобальные аргументы при вызове файлов-тестеров с помощью модуля argparse. C учетом изменений дополнить раздел "Тестирование" в README.

	Комментарий: сейчас глобальные аргументы определяются внутри тестеров (сайты, пути до файлов). Если я хочу запустить скрипт на другом сайте, мне нужно редактировать тестер. Я хочу динамически задавать глобальные аргументы при вызове `python3.9 tester_01.py` Для этого используется модуль argparse [Хабр](https://habr.com/ru/companies/ruvds/articles/440654/), но есть и аналоги (двойки).
	```
	import argparse

	if __name__ == "__main__":

	    parser = argparse.ArgumentParser()
	    parser.add_argument('--telo', type=str, help='original')
	    args = parser.parse_args()
	    telo = args.telo

	```

	```
	python3.9 tester_01.py --telo Vladimir Putin
	```

	Это работает окей, когда аргументов немного. Когда их много, их заносят в отдельный конфиг, а при вызове питона подают путь до файла с конфигом:

	```
	import argparse

	if __name__ == "__main__":

	    parser = argparse.ArgumentParser()
	    parser.add_argument('--config_path', type=str, help='file containing all arguments')
	    args = parser.parse_args()
	    config_path = args.config_path
	    config = load_config(args.config_path)
	    telo = config['telo']
	    vasilich = config['vasilich']
	    banketnyi = config['banketnyi']
	    udmurt = config['udmurt']
	    ...

	```

	```
	python3.9 tester_01.py -config_path configs/module_03.yml
	```

	В качестве конфига можно использовать обычный txt файл, но это неудобно. Обычно используются форматы с определенной разметкой. Например json или yaml:
	- [Хабр 1](https://habr.com/ru/companies/rambler_and_co/articles/525498/)
	- [Хабр 2](https://habr.com/ru/articles/485236/)
	Я использую hyperpyyaml:
		- [pip](https://pypi.org/project/HyperPyYAML/)
		- [docs](https://github.com/speechbrain/HyperPyYAML/tree/main)
	

- module_01: 
	- [1](https://github.com/Tereget/PyProjects/blob/0c1d7e4b07458706682ed584a2efab08368e38b5/module_01/web.py#L137) - `str(cell.string).strip()`
	- [2](https://github.com/Tereget/PyProjects/blob/0c1d7e4b07458706682ed584a2efab08368e38b5/module_01/web.py#L45-L57):
		- Надо избавиться от try except
		- Решение 1: [Раздел: Декорирование функций, принимающих аргументы](https://habr.com/ru/companies/otus/articles/727590/)
		- Решение 2: Мне вообще не нравится идея определения декоратора внутри класса. Я бы вынес его, а при навешивании на методы класса добавлял бы аргумент `@dekor(error=self.error)`: [тут](https://advpyneng.readthedocs.io/ru/latest/book/08_decorators/with_args.html)


- module_02:
	- 6 - модуль не принимает файлы с определенным расширением ? Надо проверить расширение до того, как подавать в модуль. [-] Не понял. Зачем проверять? И на что проверять? В данном сценарии я избавлен от этих вопросов. Код съедает, что может съесть, и трансформирует то, что - не может.
	```
	    try:
		wb = xlrd.open_workbook(path_file_name)
	    except xlrd.biffh.XLRDError:
		funcs_for_excel.xls_converting(path_file_name)
		wb = xlrd.open_workbook('work_file.xls')
		os.remove('work_file.xls')

		->

	    # примерно так:
            if not path_file_name.endswith('.xls'):
		funcs_for_excel.xls_converting(path_file_name)

            wb = xlrd.open_workbook('work_file.xls')
            os.remove('work_file.xls')
	```
	- 7 - сделать 2 ключевых аргумента: read_path, save_path. передавать save_path тут: 8, предварительно вынеся его в аргумент. [-] Не понял совершенно.
	```
	def xls_converting(read_path="morozilnik.dead", save_path="work_file.xls"):
	    """
	    Конвертация в читаемый формат.
	    """

	    workbook = Workbook(read_path)
	    workbook.save(save_path)


	class TableProcessing:
	...
		funcs_for_excel.xls_converting(pread_path=read_path, save_path=save_path)
	...
	```


- module_03:
	- [1](https://github.com/Tereget/PyProjects/blob/0c1d7e4b07458706682ed584a2efab08368e38b5/module_03/osm_xml.py#L18-L30) - аналогично модулю 1


- module_05:
	- [1](https://github.com/Tereget/PyProjects/blob/0c1d7e4b07458706682ed584a2efab08368e38b5/module_05/mk_html.py#L77-L92) - почему нельзя добавить метод mt_link в класс MakeMT ?






