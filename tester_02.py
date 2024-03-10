import os
import zipfile

from module_02.excel import TableProcessing
from module_02.excel import salary_calculation_using_tables


rdir = os.path.join('module_02/result/')
sdir = os.path.join('module_02/src/')
file_01 = f'{sdir}salaries.xlsx'
file_02 = f'{sdir}trekking1.xlsx'
file_03 = f'{sdir}trekking2.xlsx'
file_04 = f'{sdir}trekking3.xlsx'
dir_01 = f'{sdir}roga'

if dir_01 not in os.listdir():
    with zipfile.ZipFile(f'{sdir}rogaikopyta.zip', 'r') as zip_ref:
        zip_ref.extractall(f'{dir_01}')

if __name__ == "__main__":
    print("Hello, World!")

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

        ouf.write(f'Salary calculation:\n')
        if type(res_01) == str:
            ouf.write(f'{res_01}')
        else:
            for value in res_01:
                ouf.write(f'{value}\n')
        ouf.write('\n\n\n')

        ouf.write(f'Nutricious food:\n')
        if type(res_02) == str:
            ouf.write(f'{res_02}')
        else:
            for value in res_02:
                ouf.write(f'{value}\n')
        ouf.write('\n\n\n')

        ouf.write(f'Food energic:\n')
        if type(res_03) == str:
            ouf.write(f'{res_03}')
        else:
            for value in res_03:
                ouf.write(f'{value}\n')
        ouf.write('\n\n\n')

        ouf.write(f'Food energic all days:\n')
        if type(res_04) == str:
            ouf.write(f'{res_04}')
        else:
            for value in res_04:
                ouf.write(f'{value}\n')
        ouf.write('\n\n\n')

        res_05.to_excel(f'{rdir}result.xlsx', index=0)