import os


def mk_html():
    """
    Пустая HTML-страница.
    """

    start = '<html>\n<body>\n'
    finish = '</body>\n</html>'
    return start, finish

class MakeMT:
    def __init__(self):
        self.skelet = mk_html()

    def index_html(self):
        """
        Главная HTML-страница.
        """

        table_out = self.skelet[0]

        table_out += ('<form action="/cgi-bin/data_in.py">\n'
                      '<label for="name">Num by word</label>\n'
                      '<input type="text" name="INPUT_TEXT">\n'
                      '<input type="submit">\n</form>\n')

        table_out += ('<form action="/cgi-bin/data_in_with_error.py">\n'
                      '<label for="name">Several num by word</label>\n'
                      '<input type="text" name="INPUT_TEXT">\n'
                      '<input type="submit">\n</form>\n')

        table_out += self.skelet[1]

        return table_out

    def mt_text(self):
        """
        Таблица умножения в текстовом формате (HTML-страница).
        """

        table_out = f'{self.skelet[0]}<table>\n'
        o = 1
        for i in range(10):
            y = '<tr>\n'
            table_out += y
            z = 1
            for j in range(10):
                x = o
                x *= z
                y = f'<td>{x}</td>\n'
                table_out += y
                z += 1
            y = '</tr>\n'
            table_out += y
            o += 1
        table_out += f'</table>\n{self.skelet[1]}'

        return table_out