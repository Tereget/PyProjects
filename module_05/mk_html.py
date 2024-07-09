import re
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler


def run():
    """
    Запуск локального сервера.
    """

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()


def mk_html():
    """
    Пустая HTML-страница.
    """

    start = '<html>\n<body>\n'
    finish = '</body>\n</html>'
    return start, finish


class MakeMT:
    def __init__(self):
        self.start, self.finish = mk_html()

    def index_html(self):
        """
        Главная HTML-страница.
        """

        table_out = self.start

        table_out += ('<form action="/cgi-bin/data_in.py">\n'
                      '<label for="name">Num by word</label>\n'
                      '<input type="text" name="INPUT_TEXT">\n'
                      '<input type="submit">\n</form>\n')

        table_out += ('<form action="/cgi-bin/data_in_with_error.py">\n'
                      '<label for="name">Several num by word</label>\n'
                      '<input type="text" name="INPUT_TEXT">\n'
                      '<input type="submit">\n</form>\n')

        table_out += self.finish

        return table_out

    def mt_text(self):
        """
        Таблица умножения в текстовом формате (HTML-страница).
        """

        table_out = f'{self.start}<table>\n'
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
        table_out += f'</table>\n{self.finish}'

        return table_out


class MakeMTWithLink(MakeMT):
    def mt_link(self):
        """
        Таблица умножения со ссылками (HTML-страница).
        """

        table_out = self.mt_text()
        y = r'<td>[0-9]{1,3}</td>'
        for s in table_out.splitlines():
            z = re.search(y, table_out)
            if z:
                num = table_out[z.start() + 4:z.end() - 5]
                cfl = f'<td><a href="http://{num}.ru">{num}</a></td>'
                table_out = table_out.replace(z.group(), cfl)

        return table_out