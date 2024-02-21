import os

class MakeMT:

    def mt_text(self):
        try:
            os.mkdir('result')
        except FileExistsError:
            ()

        self.pathname = 'result/' + input() + '.html'
        with open(self.pathname, 'w', encoding='utf-8') as ouf:
            o = 1
            ouf.write('<html>\n')
            ouf.write('<body>\n')
            ouf.write('<table>\n')
            for i in range(10):
                y = '<tr>\n'
                ouf.write(y)
                z = 1
                for j in range(10):
                    x = o
                    x *= z
                    y = '<td>' + str(x) + '</td>\n'
                    ouf.write(y)
                    z += 1
                y = '</tr>\n'
                ouf.write(y)
                o += 1
            ouf.write('</table>\n')
            ouf.write('</body>\n')
            ouf.write('</html>\n')

        return self.pathname


# x = MakeMT()
# x.mt_text()
