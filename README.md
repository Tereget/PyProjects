# Парсинг файлов:

#### Описание модулей:
- Модуль №1: Анализ файлов html: поиск слов; поиск строк с конкретным тегом (на примере тега \<code\>); подсчёт суммы значений ячеек таблицы (если таковые имеются).
- Модуль №2: Анализ таблиц excel: подсчёт значений по одному листу/по нескольким листам/по нескольким файлам; конвертация файлов в универсальный формат xls.
- Модуль №3: Анализ файлов xml: подсчёт объектов на фрагменте карты (точечных, а также - общего количества).
- Модуль №4: Анализ и обработка графиков: изменение разрешения/локации легенды.
- Модуль №5: Запуск сервера и генерация html.

Проект создан на основе задач из курса: https://stepik.org/course/4519/syllabus


#### Установка интерпретатора (python v.3.9):
```commandline

OS Linux:
	sudo apt update
	sudo apt install software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt install python3.9
	
OS Windows:
	https://bangbangeducation.ru/point/razrabotka/kak-ustanovit-python/
	
OS MacOS:
	$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	$ brew install python[version]
```

#### Установка окружения (python v.3.9):
```commandline

C помощью vrtualenv:
	pip3.9 install virtualenv
	python3.9 -m virtualenv .venv
	source .venv/bin/activate
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
	python3.9 tester_01.py --config_path configs/config_01.yml
	python3.9 tester_01.py --config_path configs/config_01.json
	python3.9 tester_01.py --config_path configs/config_01.txt
	
	python3.9 tester_02.py --config_path configs/config_02.yml
	python3.9 tester_02.py --config_path configs/config_02.json
	python3.9 tester_02.py --config_path configs/config_02.txt
	
	python3.9 tester_03.py --config_path configs/config_03.yml
	python3.9 tester_03.py --config_path configs/config_03.json
	python3.9 tester_03.py --config_path configs/config_03.txt
	
	python3.9 tester_04.py
	
	python3.9 tester_05.py

Результаты работы четырёх модулей сохраняются в соответствующие папки 'result'.
Пятый модуль запускает локальный сервер:
	1. При запуске тестера запускается сервер, доступный по адресу: http://localhost:8000/
	2. Ссылка ведёт в корневой каталог проекта.
	3. Результирующие странички находятся в module_05/result/ (их можно открыть, как по старинке, 
	так и через сервер (рекомендуется). 
	4. Работу функции index_html() корректно проверять через сервер 
		по пути: module_05/result/num_by_word/ (такого условие задачи).	
```
