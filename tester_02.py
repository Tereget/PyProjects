import os

from module_02.excel import TableProcessing
from module_02.excel import salary_calculation_using_tables


rdir = os.path.join('module_02/result/')
sdir = os.path.join('module_02/src/')
file_01 = 'salaries.xlsx'
file_02 = 'trekking1.xlsx'
file_03 = 'trekking2.xlsx'
file_04 = 'trekking3.xlsx'
dir_01 = 'roga'

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)

    x = TableProcessing(file_04, sdir)

    res_01 = x.salary_calculation()
    res_02 = x.nutritious_food()
    res_03 = x.food_energic()
    res_04 = x.food_energic_all_days()
    res_05 = salary_calculation_using_tables(dir_01, sdir)

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

        ouf.write(f'Salary calculation using tables:\n')
        if type(res_05) == str:
            ouf.write(f'{res_05}')
        else:
            for value in res_05:
                ouf.write(f'{value}\n')
        ouf.write('\n\n\n')