from dom import *

page = html(
    head(
        style(),
        script(),
    ),
    body(
        div("hello world"),
        a("this is a link", _href="http://www.somesite.com", _style="font-size:10px;"),
        ol(''.join([f'{li()}' for thing in range(5)])),
        h1("test", _class="test"),
    )
)
print(page)
print('======')

from window import *
window.location = "https://en.wikipedia.org/wiki/2022_United_States_House_of_Representatives_elections"
print(window.document.css('a'))
