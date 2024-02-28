import os

import xlrd
import jpype
jpype.startJVM()
import pandas as pd

from module_02 import funcs_for_excel


class TableProcessing:
    def __init__(self, file_name, path_name='module_02/cgi-bin/'):
        path_file_name = path_name + file_name

        # Получаем данные из файла.
        try:
            wb = xlrd.open_workbook(path_file_name)
        except:
            try:
                funcs_for_excel.xls_converting(path_file_name)
                wb = xlrd.open_workbook('work_file.xls')
                os.remove('work_file.xls')
            except:
                raise Exception('Файл не найден')
        self.wb = wb


    def salary_calculation(self):
        try:
            sh = self.wb.sheet_by_index(0)
            return funcs_for_excel.salary_calculation(sh)
        except:
            return 'Некорректные данные в файле'


    def nutritious_food(self):
        try:
            sh = self.wb.sheet_by_index(0)
            return funcs_for_excel.nutritious_food(sh)
        except:
            return 'Некорректные данные в файле'


    def food_energic(self):
        try:
            sh_1 = self.wb.sheet_by_name('Справочник')
            sh_2 = self.wb.sheet_by_name('Раскладка')
            return funcs_for_excel.food_energic(sh_1, sh_2)
        except:
            return 'Некорректные данные в файле'


    def food_energic_all_days(self):
        try:
            sh_1 = self.wb.sheet_by_name('Справочник')
            sh_2 = self.wb.sheet_by_name('Раскладка')
            return funcs_for_excel.food_energic_all_days(sh_1, sh_2)
        except:
            return 'Некорректные данные в файле'



def salary_calculation_using_tables(dir_name, path_name='module_02/cgi-bin/'):
    """
    Функция для заполнения общей ведомости по имеющимся расчётным листкам.
    """

    dir_name = path_name + dir_name
    try:
        file_list = os.listdir(dir_name)
    except:
        return 'Некорректный путь к файлам'
    # - 1: Создаём пустой список и заполняем значениями "ФИО, Начислено".
    sp_out = []

    # - 1.1: Читаем файлы с ЗП сотрудников.
    for file in file_list:
        filename = dir_name + '/' + file
        df = pd.read_excel(filename, engine='openpyxl')

        # - 1.2: Достаём нужные значения.
        for value in df.values:
            i = 0
            while i < len(value):
                if value[i] == 'ФИО':
                    name = value[i+1]
                elif value[i] == 'Начислено':
                    money = value[i+1]
                i += 1

        # - 1.3: Добавляем значения в список.
        sp_out.append((name, ' ', str(int(money))))

    # - 2: Сортируем спсиок по алфавиту.
    sp_out.sort()

    # - 3: Возвращаем ответ.
    return sp_out