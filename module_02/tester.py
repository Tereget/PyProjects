import os
import excel

if __name__ == "__main__":
    print("Hello, World!")

    try:
        os.mkdir('result')
    except FileExistsError:
        ()

    x = excel.TableProcessing('trekking3.xlsx')

    """
    # salaries.xlsx
    with open('result/salary_calculation.txt', 'w') as ouf:
        ouf.write(x.salary_calculation())
    """

    """
    # trekking1.xlsx
    x.nutritious_food()
    """

    """
    # trekking2.xlsx
    with open('result/food_energic.txt', 'w') as ouf:
        ouf.write(x.food_energic())
    """

    """
    # trekking3.xlsx
    x.food_energic_all_days()
    """

    """
    excel.salary_calculation_using_tables('roga')
    """
