import os

from module_02 import excel

rdir = 'module_02/result/'
sdir = 'module_02/src/'

if __name__ == "__main__":
    print("Hello, World!")

    os.makedirs(rdir, exist_ok=True)

    x = excel.TableProcessing('trekking3.xlsx', sdir)

    # salaries.xlsx (in class)
    res = x.salary_calculation()
    rfile = rdir + 'salary_calculation.txt'
    with open(rfile, 'w') as ouf:
        ouf.write(res)

    # trekking1.xlsx (in class)
    res = x.nutritious_food()
    rfile = rdir + 'nutritious_food.txt'
    with open(rfile, 'w') as ouf:
        if res == 'Некорректные данные в файле':
            ouf.write(res)
        else:
            for food in res:
                ouf.write(food)
                ouf.write('\n')

    # trekking2.xlsx (in class)
    res = x.food_energic()
    rfile = rdir + 'food_energic.txt'
    with open(rfile, 'w') as ouf:
        ouf.write(res)

    # trekking3.xlsx (in class)
    res = x.food_energic_all_days()
    rfile = rdir + 'food_energic_all_days.txt'
    with open(rfile, 'w') as ouf:
        if res == 'Некорректные данные в файле':
            ouf.write(res)
        else:
            for k in res:
                ouf.write(k)
                ouf.write('\n')

    # roga (in def)
    res = excel.salary_calculation_using_tables('roga', sdir)
    rfile = rdir + 'sallaries_in_the_roga.txt'
    with open(rfile, 'w') as ouf:
        if res == 'Некорректный путь к файлам':
            ouf.write(res)
        else:
            for els in res:
                for el in els:
                    ouf.write(el)
                ouf.write('\n')