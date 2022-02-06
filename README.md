# adom

A [domonic-like](https://github.com/byteface/domonic) wrapper around [selectolax](https://github.com/rushter/selectolax)

```python
from dom import *
print(html(body(h1('Hello, World!'))))
# <html><body><h1>Hello, World!</h1></body></html>
```

```python
from window import *
window.location = "https://www.google.com"
print( window.document.css('a') )
# [<Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>, <Node a>]
```

### install

```bash
python3 -m pip install adom
```

### CLI

To see the version:

```bash
domonic -v
```

To use css selectors on a website...

```bash
adom -q https://google.com a
```
