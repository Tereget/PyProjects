import os
import zipfile

from module_02.excel import TableProcessing
from module_02.excel import salary_calculation_using_tables


def writing(head, result):
    ouf.write(f'{head}:\n')
    if isinstance(result, str):
        ouf.write(f'{result}')
    else:
        for value in result:
            ouf.write(f'{value}\n')
    ouf.write('\n\n\n')


rdir = os.path.join('module_02/result/')
sdir = os.path.join('module_02/src/')
file_01 = f'{sdir}salaries.xlsx'
file_02 = f'{sdir}trekking1.xlsx'
file_03 = f'{sdir}trekking2.xlsx'
file_04 = f'{sdir}trekking3.xlsx'
dir_01 = f'{sdir}roga'

if __name__ == "__main__":
    print("Hello, World!")

    if dir_01 not in os.listdir():
        with zipfile.ZipFile(f'{sdir}rogaikopyta.zip', 'r') as zip_ref:
            zip_ref.extractall(f'{dir_01}')

    os.makedirs(rdir, exist_ok=True)

    x1 = TableProcessing(file_01)
    x2 = TableProcessing(file_02)
    x3 = TableProcessing(file_03)
    x4 = TableProcessing(file_04)

    res_01 = x1.salary_calculation()
    res_02 = x2.nutritious_food()
    res_03 = x3.food_energic()
    res_04 = x4.food_energic_all_days()
    res_05 = salary_calculation_using_tables(dir_01)

    with open(f'{rdir}results.txt', 'w') as ouf:
        writing('Salary calculation', res_01)
        writing('Nutricious food', res_02)
        writing('Food energic', res_03)
        writing('Food energic all days', res_04)

    res_05.to_excel(f'{rdir}result.xlsx', index=0)