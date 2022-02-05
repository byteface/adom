from selectolax.parser import Node
from selectolax.parser import HTMLParser

# def render(inp, outp=''):
#     print( inp )
#     return str(inp)

__version__ = '0.0.2'


class tag():

    def __init__(self, *args, **kwargs):
        self.content = ''.join([each.__str__() for each in args])
        self.__attributes = ''.join([ ''' %s="%s"''' % (key.split('_')[1], value) for key, value in kwargs.items()])
        # super().__init__()
        self._node = HTMLParser(f"<{self.name}{self.__attributes}>{self.content}</{self.name}>")#.root
        # In [2]: tree.css_first('h1#title').text()
        # print(dir(self._node))
        # self.__cls__ = self._node.__dir__
        # self.__dict__.update(self._node)

    def __str__(self):
        # return f"<{self.name}{self.__attributes}>{self.content}</{self.name}>"
        return self._node.html


html = type('html', (tag,), {'name':'html'})
body = type('body', (tag,), {'name':'body'})
head = type('head', (tag,), {'name':'head'})
script = type('script', (tag,), {'name':'script'})
style = type('style', (tag,), {'name':'style'})
h1 = type('h1', (tag,), {'name':'h1'})
h2 = type('h2', (tag,), {'name':'h2'})
h3 = type('h3', (tag,), {'name':'h3'})
h4 = type('h4', (tag,), {'name':'h4'})
h5 = type('h5', (tag,), {'name':'h5'})
h6 = type('h6', (tag,), {'name':'h6'})
p = type('p', (tag,), {'name':'p'})
i = type('i', (tag,), {'name':'i'})
b = type('b', (tag,), {'name':'b'})
a = type('a', (tag,), {'name':'a'})
ul = type('ul', (tag,), {'name':'ul'})
ol = type('ol', (tag,), {'name':'ol'})
li = type('li', (tag,), {'name':'li'})
hr = type('hr', (tag,), {'name':'hr'})
img = type('img', (tag,), {'name':'img'})
div = type('div', (tag,), {'name':'div'})
span = type('span', (tag,), {'name':'span'})
strong = type('strong', (tag,), {'name':'strong'})
blockquote = type('blockquote', (tag,), {'name':'blockquote'})
table = type('table', (tag,), {'name':'table'})
tr = type('tr', (tag,), {'name':'tr'})
td = type('td', (tag,), {'name':'td'})
title = type('title', (tag,), {'name':'title'})
meta = type('meta', (tag,), {'name':'meta'})
