import re
from mk_mt_text import MakeMT

class MakeMTWithLink(MakeMT):

    def mt_link(self):
        self.pathname = self.mt_text()
        with open(self.pathname, 'r') as inf:
            n = inf.read()
        y = r'<td>[0-9]{1,3}</td>'
        for s in n.splitlines():
            z = re.search(y, n)
            try:
                num = n[z.start()+4:z.end()-5]
                cfl = '<td><a href="http://'+num+'.ru">'+num+'</a></td>'
                n = n.replace(z.group(), cfl)
            except AttributeError:
                continue

        with open(self.pathname, 'w', encoding='utf-8') as ouf:
            ouf.write(n)


# x = MakeMTWithLink()
# x.mt_link()

