# Добавить название проекта:

Модуль №1: Анализ файлов html: поиск слов; поиск строк с конкретным тегом (на примере тега \<code\>); подсчёт суммы значений ячеек таблицы (если таковые имеются).
Модуль №2: Анализ таблиц excel: подсчёт значений по одному листу/по нескольким листам/по нескольким файлам; конвертация файлов в универсальный формат xls.
Модуль №3: Анализ файлов xml: подсчёт объектов на фрагменте карты (точечных, а также - общего количества).
Модуль №4: Анализ и обработка графиков: изменение разрешения/локации легенды.


# CODE REVIEW:

## TASK_01

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


## TASK_02

### 1. Code
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


### 2. README
- Описание модулей сделать списком
- Добавить блок кода с командой по установке окружения из requirements.txt: [MarkDownCodeBlock](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code-and-syntax-highlighting)
