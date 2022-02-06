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
adom -v
```

To use css selectors on a website...

```bash
adom -q https://google.com a
```

### Discord

There's a discord for domonic to talk about python/doms etc. It can be used for this as well.
I check there 2 or 3 times a week or post updates there.

https://discord.gg/a9pSZv4V5f
