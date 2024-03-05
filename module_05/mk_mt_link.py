import re

from module_05.mk_mt_text import MakeMT


class MakeMTWithLink(MakeMT):

    def mt_link(self):
        table_out = self.mt_text()
        y = r'<td>[0-9]{1,3}</td>'
        for s in table_out.splitlines():
            z = re.search(y, table_out)
            if z:
                num = table_out[z.start()+4:z.end()-5]
                cfl = f'<td><a href="http://{num}.ru">{num}</a></td>'
                table_out = table_out.replace(z.group(), cfl)

        return table_out