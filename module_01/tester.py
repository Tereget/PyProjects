import os
from web import WordCounterOnTheSite

if __name__ == "__main__":
    print("Hello, World!")

    try:
        os.mkdir('result')
    except FileExistsError:
        ()

    x = WordCounterOnTheSite('https://ru.wikipedia.org/wiki/Python')

    """
    # https://stepik.org/media/attachments/lesson/209717/1.html
    with open('result/total_score.txt', 'w') as ouf:                    
        ouf.write(x.total_score('Python'))
    """

    """
    # https://ru.wikipedia.org/wiki/Python
    with open('result/visible_on_the_site.txt', 'w') as ouf:            
        ouf.write(x.visible_on_the_site('Python'))
    """

    """
    # https://stepik.org/media/attachments/lesson/209719/2.html
    with open('result/frequent_line_in_code_tag.txt', 'w') as ouf:      
        ouf.write(x.frequent_line_in_code_tag())
    """

    """
    # https://stepik.org/media/attachments/lesson/209723/4.html
    with open('result/sum_of_cell_values.txt', 'w') as ouf:             
        ouf.write(x.sum_of_cell_values())
    """
