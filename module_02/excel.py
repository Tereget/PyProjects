import xlrd
import jpype
jpype.startJVM()
import os
import pandas as pd
import openpyxl
import funcs_for_excel
from asposecells.api import Workbook


def xls_converting(path_file_name):
    """
    Конвертация в читаемый формат.
    """

    workbook = Workbook(path_file_name)
    workbook.save("work_file.xls")



class TableProcessing:
    def __init__(self, file_name, path_name='src/'):
        path_file_name = path_name + file_name

        # Получаем данные из файла.
        try:
            wb = xlrd.open_workbook(path_file_name)
        except Exception:
            try:
                xls_converting(path_file_name)
                wb = xlrd.open_workbook('work_file.xls')
                os.remove('work_file.xls')
            except Exception:
                raise Exception('Файл не найден')
        self.wb = wb


    def salary_calculation(self):
        sh = self.wb.sheet_by_index(0)
        return funcs_for_excel.salary_calculation(sh)


    def nutritious_food(self):
        sh = self.wb.sheet_by_index(0)
        return funcs_for_excel.nutritious_food(sh)


    def food_energic(self):
        sh_1 = self.wb.sheet_by_name('Справочник')
        sh_2 = self.wb.sheet_by_name('Раскладка')
        return funcs_for_excel.food_energic(sh_1, sh_2)


    def food_energic_all_days(self):
        sh_1 = self.wb.sheet_by_name('Справочник')
        sh_2 = self.wb.sheet_by_name('Раскладка')
        return funcs_for_excel.food_energic_all_days(sh_1, sh_2)



def salary_calculation_using_tables(dir_name, path_name='src/'):
    """
    Функция для заполнения общей ведомости по имеющимся расчётным листкам.
    """

    dir_name = path_name + dir_name
    # - 1: Создаём пустой список и заполняем значениями "ФИО, Начислено".
    sp_out = []

    # - 1.1: Читаем файлы с ЗП сотрудников.
    for file in os.listdir(dir_name):
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

    # - 3: Создаём папку для результатов (если таковой нет).
    try:
        os.mkdir('result')
    except FileExistsError:
        ()

    # - 4: Записываем результат в блокнот.
    with open('result/sallaries_in_the_roga.txt', 'w', encoding="UTF-8") as ouf:
        for els in sp_out:
            for el in els:
                ouf.write(el)
            ouf.write('\n')
