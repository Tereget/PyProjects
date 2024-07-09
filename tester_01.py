import os

from args_from_file import arg_pars
from module_01.web import WordCounterOnTheSite


if __name__ == "__main__":
    print("Hello, World!")

    rdir = os.path.join('module_01', 'result', '')
    arg_dict = arg_pars('--config_path')
    site_01 = arg_dict['site_01']
    site_02 = arg_dict['site_02']
    site_03 = arg_dict['site_03']
    site_04 = arg_dict['site_04']
    word = arg_dict['word']
    tag = arg_dict['tag']

    os.makedirs(rdir, exist_ok=True)

    x1 = WordCounterOnTheSite(site_01)
    x2 = WordCounterOnTheSite(site_02)
    x3 = WordCounterOnTheSite(site_03)
    x4 = WordCounterOnTheSite(site_04)

    res_01 = x1.total_score(word)
    res_02 = x2.visible_on_the_site(word)
    res_03 = x3.frequent_line_in_code_tag(tag)
    res_04 = x4.sum_of_cell_values()

    with open(f'{rdir}results.txt', 'w') as ouf:
        ouf.write(f'Total score:\n{res_01}\n\n\nVisible on the site:\n{res_02}\n\n\n'
                  f'Frequent line in code tag:\n{res_03}\n\n\n'
                  f'Sum of cell values:\n{res_04}')
