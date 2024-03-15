import os

import xlrd
import jpype
jpype.startJVM()
import pandas as pd

from module_02 import funcs_for_excel
from module_02.funcs_for_excel import dekor


class TableProcessing:
    def __init__(self, path_file_name):
        # Получаем данные из файла.
        if os.path.isfile(path_file_name):
            try:
                wb = xlrd.open_workbook(path_file_name)
            except xlrd.biffh.XLRDError:
                funcs_for_excel.xls_converting(path_file_name)
                wb = xlrd.open_workbook('work_file.xls')
                os.remove('work_file.xls')
            self.wb = wb


    @dekor
    def salary_calculation(self):
        sh = self.wb.sheet_by_index(0)
        return funcs_for_excel.salary_calculation(sh)


    @dekor
    def nutritious_food(self):
        sh = self.wb.sheet_by_index(0)
        return funcs_for_excel.nutritious_food(sh)


    @dekor
    def food_energic(self, l_one='Справочник', l_two='Раскладка'):
        sh_1 = self.wb.sheet_by_name(l_one)
        sh_2 = self.wb.sheet_by_name(l_two)
        return funcs_for_excel.food_energic(sh_1, sh_2)


    @dekor
    def food_energic_all_days(self, l_one='Справочник', l_two='Раскладка'):
        sh_1 = self.wb.sheet_by_name(l_one)
        sh_2 = self.wb.sheet_by_name(l_two)
        return funcs_for_excel.food_energic_all_days(sh_1, sh_2)


def salary_calculation_using_tables(dir_name):
    """
    Функция для заполнения общей ведомости по имеющимся расчётным листкам.
    """
    file_list = funcs_for_excel.finding_tables(dir_name)
    if isinstance(file_list, str):
        return file_list

    # - 1: Создаём пустой список и заполняем значениями "ФИО, Начислено".
    sp_name = []
    sp_money = []

    # - 2: Читаем файлы с ЗП сотрудников.
    for file in file_list:
        filename = os.path.join(f'{dir_name}/{file}')
        df = pd.read_excel(filename, engine='openpyxl')

        # - 2.1: Достаём нужные значения.
        name = df.values[0][1]
        money = df.values[0][3]

        # - 2.2: Добавляем значения в списки.
        sp_name.append(name)
        sp_money.append(int(money))

    # - 3: Создаём и сортируем датафрейм.
    df = pd.DataFrame({"ФИО": sp_name, "Начислено": sp_money})
    df = df.sort_values(by='ФИО')

    return df