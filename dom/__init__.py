from selectolax.parser import Node as sNode
from selectolax.parser import HTMLParser


__version__ = '0.0.3'

html_tags = [
    "figcaption",
    "blockquote",
    "textarea",
    "progress",
    "optgroup",
    "noscript",
    "fieldset",
    "datalist",
    "colgroup",
    "summary",
    "section",
    "details",
    "command",
    "caption",
    "article",
    "address",
    "submit",
    "strong",
    "source",
    "select",
    "script",
    "output",
    "option",
    "legend",
    "keygen",
    "iframe",
    "hgroup",
    "header",
    "footer",
    "figure",
    "canvas",
    "button",
    "video",
    "track",
    "title",
    "thead",
    "tfoot",
    "tbody",
    "table",
    "style",
    "small",
    "param",
    "meter",
    "label",
    "input",
    "audio",
    "aside",
    "applet",
    "object",
    "basefont",
    "center",
    "embed",
    "isindex",
    "listing",
    "menuitem",
    "plaintext",
    "strike",
    "template",
    "picture",
    "dialog",
    "time",
    "span",
    "samp",
    "ruby",
    "meta",
    "menu",
    "mark",
    "link",
    "html",
    "head",
    "form",
    "font",
    "code",
    "cite",
    "body",
    "base",
    "area",
    "abbr",
    "main",
    "dir",
    "wbr",
    "var",
    "sup",
    "sub",
    "nav",
    "map",
    "kbd",
    "ins",
    "img",
    "div",
    "dfn",
    "del",
    "col",
    "bdo",
    "bdi",
    "pre",
    "xmp",
    "ul",
    "tr",
    "th",
    "td",
    "rt",
    "rp",
    "ol",
    "li",
    "hr",
    "h6",
    "h5",
    "h4",
    "h3",
    "h2",
    "h1",
    "em",
    "dt",
    "dl",
    "dd",
    "br",
    "u",
    "s",
    "q",
    "p",
    "i",
    "b",
    "a",
]
# big, blink, bold, tt, var, frameset

html_attributes = [
    "accept",
    "accesskey",
    "loading",
    "action",
    "align",
    "alt",
    "async",
    "autocomplete",
    "autofocus",
    "autoplay",
    "bgcolor",
    "border",
    "charset",
    "checked",
    "cite",
    "class",
    "color",
    "cols",
    "colspan",
    "content",
    "contenteditable",
    "controls",
    "coords",
    "data",
    "datetime",
    "default",
    "defer",
    "dir",
    "dirname",
    "disabled",
    "download",
    "draggable",
    "enctype",
    "for",
    "form",
    "formaction",
    "headers",
    "height",
    "hidden",
    "high",
    "href",
    "hreflang",
    "id",
    "ismap",
    "kind",
    "label",
    "lang",
    "list",
    "loop",
    "low",
    "max",
    "maxlength",
    "media",
    "method",
    "min",
    "multiple",
    "muted",
    "name",
    "novalidate",
    "onabort",
    "onafterprint",
    "onbeforeprint",
    "onbeforeunload",
    "onblur",
    "oncanplay",
    "oncanplaythrough",
    "onchange",
    "onclick",
    "oncontextmenu",
    "oncopy",
    "oncuechange",
    "oncut",
    "ondblclick",
    "ondrag",
    "ondragend",
    "ondragenter",
    "ondragleave",
    "ondragover",
    "ondragstart",
    "ondrop",
    "ondurationchange",
    "onemptied",
    "onended",
    "onerror",
    "onfocus",
    "onhashchange",
    "oninput",
    "oninvalid",
    "onkeydown",
    "onkeypress",
    "onkeyup",
    "onload",
    "onloadeddata",
    "onloadedmetadata",
    "onloadstart",
    "onmousedown",
    "onmousemove",
    "onmouseout",
    "onmouseover",
    "onmouseup",
    "onmousewheel",
    "onoffline",
    "ononline",
    "onpagehide",
    "onpageshow",
    "onpaste",
    "onpause",
    "onplay",
    "onplaying",
    "onpopstate",
    "onprogress",
    "onratechange",
    "onreset",
    "onresize",
    "onscroll",
    "onsearch",
    "onseeked",
    "onseeking",
    "onselect",
    "onstalled",
    "onstorage",
    "onsubmit",
    "onsuspend",
    "ontimeupdate",
    "ontoggle",
    "onunload",
    "onvolumechange",
    "onwaiting",
    "onwheel",
    "open",
    "optimum",
    "pattern",
    "placeholder",
    "poster",
    "preload",
    "readonly",
    "rel",
    "required",
    "reversed",
    "rows",
    "rowspan",
    "sandbox",
    "scope",
    "selected",
    "shape",
    "size",
    "sizes",
    "span",
    "spellcheck",
    "src",
    "srcdoc",
    "srclang",
    "srcset",
    "start",
    "step",
    "style",
    "tabindex",
    "target",
    "title",
    "translate",
    "type",
    "usemap",
    "value",
    "width",
    "wrap",
    "property",
    "integrity",
    "crossorigin",
    "nonce",
    "autocapitalize",
    "enterkeyhint",
    "inputmode",
    "is",
    "itemid",
    "itemprop",
    "itemref",
    "itemscope",
    "itemtype",
    "part",
    "slot",
    "spellcheck",
    "alink",
    "nowrap",
    "vlink",
    "vspace",
    "language",
    "clear",
    "hspace",
    "xmlns",
    "about",
    "allowtransparency",
    "datatype",
    "inlist",
    "prefix",
    "resource",
    "rev",
    "typeof",
    "vocab",  # rdfa
    "playsinline",
    "autopictureinpicture",
    "buffered",
    "controlslist",
    "disableremoteplayback",  # video
]


class Node():
    ELEMENT_NODE: int = 1
    TEXT_NODE: int = 3
    CDATA_SECTION_NODE: int = 4
    PROCESSING_INSTRUCTION_NODE: int = 7
    COMMENT_NODE: int = 8
    DOCUMENT_NODE: int = 9
    DOCUMENT_TYPE_NODE: int = 10
    DOCUMENT_FRAGMENT_NODE: int = 11

    '''
    def __format__(self, format_spec):
        # return f"<{self.name}{self.__attributes}>{self.content}</{self.name}>"
        # http://tidy.sourceforge.net/docs/quickref.html

        BASE_OPTIONS = {
            # "indent": 1,           # Pretty; not too much of a performance hit
            # "tidy-mark": 0,        # No tidy meta tag in output
            # "wrap": 0,             # No wrapping
            # "alt-text": "",        # Help ensure validation
            # "doctype": 'strict',   # Little sense in transitional for tool-generated markup...
            # "force-output": 1,     # May not get what you expect but you will get something

            # HTML, XHTML, XML Options Reference
            # 'anchor-as-name': 0,  #?,
            'doctype': 'auto',
            'drop-empty-paras': 0,
            'fix-backslash': 0,
            'fix-bad-comments': 0,
            'fix-uri':0,
            'hide-endtags': 1,   #?,
            'input-xml': 1,     #?,
            'join-styles': 0,
            'literal-attributes': 1,
            'lower-literals': 0,
            'merge-divs': 0,
            # 'merge-spans': 0,
            'output-html': 1,
            # 'preserve-entities': 1,
            'quote-ampersand': 0,
            'quote-nbsp': 0,
            # 'show-body-only': 'auto',

            # Diagnostics Options Reference
            'show-errors': 0,
            'show-warnings': 0,

            # Pretty Print Options Reference
            'break-before-br': 1,
            'indent': 1,
            'indent-attributes': 0,   #default,
            'indent-spaces': 4,
            'tab-size': 4,
            'wrap': 132,
            'wrap-asp': 0,
            'wrap-jste': 0,
            'wrap-php': 0,
            'wrap-sections': 0,

            # Character Encoding Options Reference
            'char-encoding': 'utf8',

            # Miscellaneous Options Reference
            'force-output': 1,
            'quiet': 1,
            'tidy-mark': 0,

        }

        # from tidylib import tidy_document
        # import tidylib
        # tidylib.BASE_OPTIONS = BASE_OPTIONS
        # tidylib.BASE_OPTIONS = {}
        # print('BEFORE::', self._node.html)
        # document, errors = tidy_document(self._node.html,
                                        #  options=BASE_OPTIONS)
        # print document
        # print errors


        # https://github.com/nijel/utidylib
        import tidy
        doc = tidy.parseString(
            self._node.html,
            output_html=1,
            # output_xhtml=1,
            # add_xml_decl=1,
            indent=1,
            tidy_mark=0,
            doctype="auto",  #'html5' - fails?
        )

        # https://github.com/Kijewski/pytidyhtml5/blob/master/basic-sanity-test.py

        return str(doc)
        '''

    def __str__(self):
        # return f"<{self.name}{self.__attributes}>{self.content}</{self.name}>"
        # return self._node.html
        return self._node.html


    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs

        if getattr(self, 'name', None) is None:
            self.name = ''

        # if user doesn't put underscore (dont advertise this as still has issues.)
        new_kwargs = {}
        for k, v in kwargs.items():
            if k[0] != "_":
                new_kwargs[f"_{k}"] = v
            else:
                new_kwargs[k] = v
        self.kwargs = new_kwargs

        try:
            self.content = ''.join([each.__str__() for each in args])
            self.__attributes__ = ''.join([''' %s="%s"''' % (key.split('_', 1)[1], value) for key, value in self.kwargs.items()])
        except IndexError as e:
            # from domonic.html import TemplateError
            # raise TemplateError(e)
            print('template error!')
            raise Exception(e)

        self._doc = HTMLParser(f"<{self.name}{self.__attributes__}>{self.content}</{self.name}>")#.root
        if self.name == 'html':
            self._node = self._doc
        # elif self.name == 'head':
        #     self._node = self._doc
        else:
            self._node = self._doc.tags(self.name)[0]
            # if self._doc.body.child is not None:
            #     self._node = self._doc.body.child

        # print(dir(self._node))
        # super().__init__(*args, **kwargs)


# class closed_tag(Node):
#     def __str__(self):
#         return f"<{self.name}{self.__attributes__}/>"


class Element(Node):
    # __slots__ = ('_id')

    def __init__(self, *args, **kwargs):
        # self.content = None
        # self.attributes = None
        # if self.hasAttribute('id'):
        #     self.id = self.id  # ''#None

        # self.lang = None
        # self.tabIndex = None

        # if self.hasAttribute('title'):
        #     self.title = self.title

        # if self.hasAttribute('class'):
        #     self.className = self.className
        #     self.classList = self.classList

        # self.tagName
        self.style = None  # Style(self)  # = #'test'#Style()
        # self.shadowRoot = None
        # self.dir = None
        super().__init__(*args, **kwargs)


class Document(Element,):
    URL = None

    def __init__(self, *args, **kwargs):
        """ Constructor for Document objects """
        self.args = args
        self.kwargs = kwargs
        # self.documentURI = uri
        # self.documentElement = self
        self.stylesheets = None
        self.doctype = None
        super().__init__(*args, **kwargs)
        # try:
            # global document
            # document = self
        # except Exception as e:
            # print('failed to set document', e)

# document can be set manually but will get set each time a new Document is created.
# global document
# document = Document()


class HTMLElement(Element):  # TODO - check
    name = ''


class HTMLAnchorElement(HTMLElement):  # TODO - check
    name = 'a'
    # def __init__(self, *args, **kwargs):
        # self.url = urllib.parse.urlsplit(url)
        # self.href = url  # self.url.geturl()
        # self.protocol = self.url.scheme
        # self.hostname = self.url.hostname
        # self.port = self.url.port
        # self.host = self.url.hostname
        # self.pathname = self.url.path
        # self.hash = ''
        # self.search = self.url.query
        # self._searchParams = URLSearchParams(self.url.query)
        # super().__init__(*args, **kwargs)


class HTMLAreaElement(HTMLElement):  # TODO - check
    name = 'area'


class HTMLAudioElement(HTMLElement):
    name = 'audio'


class HTMLBRElement(HTMLElement):
    name = 'br'


class HTMLBaseElement(HTMLElement):
    name = 'base'


class HTMLBaseFontElement(HTMLElement):  # TODO - check
    name = 'basefont'


class HTMLBodyElement(HTMLElement):
    name = 'body'


class HTMLButtonElement(HTMLElement):
    name = 'button'


class HTMLCanvasElement(HTMLElement):
    name = 'canvas'


class HTMLContentElement(HTMLElement):  # TODO - check
    name = 'content'


class HTMLDListElement(HTMLElement):
    name = 'dl'


class HTMLDataElement(HTMLElement):
    name = 'data'


class HTMLDataListElement(HTMLElement):
    name = 'datalist'


class HTMLDialogElement(HTMLElement):
    name = 'dialog'


class HTMLDivElement(HTMLElement):
    name = 'div'


class HTMLDocument(Document):
    name = 'html'


class HTMLEmbedElement(HTMLElement):
    name = 'embed'


class HTMLFieldSetElement(HTMLElement):  # TODO - check
    name = 'fieldset'


class HTMLFormControlsCollection(HTMLElement):  # TODO - check
    name = 'formcontrols'


class HTMLFormElement(HTMLElement):
    name = 'form'


class HTMLFrameSetElement(HTMLElement):  # TODO - check
    name = 'frameset'


class HTMLHRElement(HTMLElement):
    name = 'hr'


class HTMLHeadElement(HTMLElement):
    name = 'head'


class HTMLHeadingElement(HTMLElement):
    name = 'h1'


class HTMLIFrameElement(HTMLElement):
    name = 'iframe'


class HTMLImageElement(HTMLElement):
    name = 'img'


class HTMLInputElement(HTMLElement):
    name = 'input'


class HTMLIsIndexElement(HTMLElement):  # TODO - check
    name = ''


class HTMLKeygenElement(HTMLElement):
    name = 'keygen'


class HTMLLIElement(HTMLElement):
    name = 'li'


class HTMLLabelElement(HTMLElement):
    name = 'label'


class HTMLLegendElement(HTMLElement):
    name = 'legend'


class HTMLLinkElement(HTMLElement):
    name = 'link'


class HTMLMapElement(HTMLElement):  # TODO - check
    name = 'map'


class HTMLMediaElement(HTMLElement):  # TODO - check
    name = 'media'


class HTMLMetaElement(HTMLElement):
    name = 'meta'


class HTMLMeterElement(HTMLElement):
    name = 'meter'


class HTMLModElement(HTMLElement):  # TODO - check
    name = 'mod'


class HTMLOListElement(HTMLElement):
    name = 'ol'


class HTMLObjectElement(HTMLElement):
    name = 'object'


class HTMLOptGroupElement(HTMLElement):
    name = 'optgroup'


class HTMLOptionElement(HTMLElement):
    name = 'option'


# class HTMLOptionsCollection(HTMLElement):   # TODO - check
#     name = 'options'


class HTMLOutputElement(HTMLElement):
    name = 'output'


class HTMLParagraphElement(HTMLElement):
    name = 'p'


class HTMLParamElement(HTMLElement):  # TODO - check
    name = 'param'


class HTMLPictureElement(HTMLElement):
    name = 'picture'


class HTMLPreElement(HTMLElement):
    name = 'pre'


class HTMLProgressElement(HTMLElement):
    name = 'progress'


class HTMLQuoteElement(HTMLElement):  # TODO - check
    name = 'q'


class HTMLScriptElement(HTMLElement):
    name = 'script'


class HTMLSelectElement(HTMLElement):
    name = 'select'


class HTMLShadowElement(HTMLElement):  # TODO - check
    name = 'shadow'


class HTMLSourceElement(HTMLElement):  # TODO - check
    name = 'source'


class HTMLSpanElement(HTMLElement):
    name = 'span'


class HTMLStyleElement(HTMLElement):
    name = 'style'


class HTMLTableCaptionElement(HTMLElement):  # TODO - check
    name = 'caption'


class HTMLTableCellElement(HTMLElement):  # TODO - check
    name = 'td'


class HTMLTableColElement(HTMLElement):
    name = 'col'


class HTMLTableDataCellElement(HTMLElement):  # TODO - check
    name = 'td'


class HTMLTableElement(HTMLElement):
    name = 'table'


class HTMLTableHeaderCellElement(HTMLElement):
    name = 'th'


class HTMLTableRowElement(HTMLElement):
    name = 'tr'


class HTMLTableSectionElement(HTMLElement):
    name = 'tbody'


class HTMLTemplateElement(HTMLElement):  # TODO - check
    name = 'template'


class HTMLTextAreaElement(HTMLElement):
    name = 'textarea'


class HTMLTimeElement(HTMLElement):
    name = 'time'


class HTMLTitleElement(HTMLElement):
    name = 'title'


class HTMLTrackElement(HTMLElement):
    name = 'track'


class HTMLUListElement(HTMLElement):
    name = 'ul'


class HTMLUnknownElement(HTMLElement):
    name = 'unknown'


class HTMLVideoElement(HTMLElement):
    name = 'video'


html = type('html', (Document,), {'name': 'html'})
body = type('body', (Element,), {'name': 'body'})
head = type('head', (Element,), {'name': 'head'})
script = type('script', (Element,), {'name': 'script'})
style = type('style', (Element,), {'name': 'style'})
h1 = type('h1', (Element,), {'name': 'h1'})
h2 = type('h2', (Element,), {'name': 'h2'})
h3 = type('h3', (Element,), {'name': 'h3'})
h4 = type('h4', (Element,), {'name': 'h4'})
h5 = type('h5', (Element,), {'name': 'h5'})
h6 = type('h6', (Element,), {'name': 'h6'})
p = type('p', (Element,), {'name': 'p'})
i = type('i', (Element,), {'name': 'i'})
b = type('b', (Element,), {'name': 'b'})
a = type('a', (HTMLAnchorElement,), {'name': 'a'})
ul = type('ul', (Element,), {'name': 'ul'})
ol = type('ol', (Element,), {'name': 'ol'})
li = type('li', (Element,), {'name': 'li'})
hr = type('hr', (Element,), {'name': 'hr'})
img = type('img', (Element,), {'name': 'img'})
div = type('div', (Element,), {'name': 'div'})
span = type('span', (Element,), {'name': 'span'})
strong = type('strong', (Element,), {'name': 'strong'})
blockquote = type('blockquote', (Element,), {'name': 'blockquote'})
table = type('table', (Element,), {'name': 'table'})
tr = type('tr', (Element,), {'name': 'tr'})
td = type('td', (Element,), {'name': 'td'})
title = type('title', (Element,), {'name': 'title'})
# meta = type('meta', (Element,), {'name': 'meta'})

form = type('form', (Element,), {'name': 'form'})
label = type("label", (Element,), {"name": "label"})

submit = type("submit", (Element,), {"name": "submit"})
# title = type("title", (Element,), {"name": "title"})
noscript = type("noscript", (Element,), {"name": "noscript"})
section = type("section", (Element,), {"name": "section"})
nav = type("nav", (Element,), {"name": "nav"})
article = type("article", (Element,), {"name": "article"})
aside = type("aside", (Element,), {"name": "aside"})
hgroup = type("hgroup", (Element,), {"name": "hgroup"})
address = type("address", (Element,), {"name": "address"})
pre = type("pre", (Element,), {"name": "pre"})
dl = type("dl", (Element,), {"name": "dl"})
dt = type("dt", (Element,), {"name": "dt"})
dd = type("dd", (Element,), {"name": "dd"})
figure = type("figure", (Element,), {"name": "figure"})
figcaption = type("figcaption", (Element,), {"name": "figcaption"})
em = type("em", (Element,), {"name": "em"})
small = type("small", (Element,), {"name": "small"})
s = type("s", (Element,), {"name": "s"})
cite = type("cite", (Element,), {"name": "cite"})
q = type("q", (Element,), {"name": "q"})
dfn = type("dfn", (Element,), {"name": "dfn"})
abbr = type("abbr", (Element,), {"name": "abbr"})
code = type("code", (Element,), {"name": "code"})
var = type("var", (Element,), {"name": "var"})
samp = type("samp", (Element,), {"name": "samp"})
kbd = type("kbd", (Element,), {"name": "kbd"})
sub = type("sub", (Element,), {"name": "sub"})
sup = type("sup", (Element,), {"name": "sup"})
u = type("u", (Element,), {"name": "u"})
mark = type("mark", (Element,), {"name": "mark"})
ruby = type("ruby", (Element,), {"name": "ruby"})
rt = type("rt", (Element,), {"name": "rt"})
rp = type("rp", (Element,), {"name": "rp"})
bdi = type("bdi", (Element,), {"name": "bdi"})
bdo = type("bdo", (Element,), {"name": "bdo"})
span = type("span", (Element,), {"name": "span"})
ins = type("ins", (Element,), {"name": "ins"})
iframe = type("iframe", (Element,), {"name": "iframe"})
video = type("video", (Element,), {"name": "video"})
audio = type("audio", (Element,), {"name": "audio"})
canvas = type("canvas", (Element,), {"name": "canvas"})
caption = type("caption", (Element,), {"name": "caption"})
colgroup = type("colgroup", (Element,), {"name": "colgroup"})
tbody = type("tbody", (Element,), {"name": "tbody"})
thead = type("thead", (Element,), {"name": "thead"})
tfoot = type("tfoot", (Element,), {"name": "tfoot"})
th = type("th", (Element,), {"name": "th"})
fieldset = type("fieldset", (Element,), {"name": "fieldset"})
legend = type("legend", (Element,), {"name": "legend"})
button = type("button", (Element,), {"name": "button"})
select = type("select", (Element,), {"name": "select"})
datalist = type("datalist", (Element,), {"name": "datalist"})
optgroup = type("optgroup", (Element,), {"name": "optgroup"})
option = type("option", (Element,), {"name": "option"})
textarea = type("textarea", (Element,), {"name": "textarea"})
output = type("output", (Element,), {"name": "output"})
progress = type("progress", (Element,), {"name": "progress"})
meter = type("meter", (Element,), {"name": "meter"})
details = type("details", (Element,), {"name": "details"})
summary = type("summary", (Element,), {"name": "summary"})
menu = type("menu", (Element,), {"name": "menu"})
menuitem = type("menuitem", (Element,), {"name": "menuitem"})  # dead but may be used
font = type("font", (Element,), {"name": "font"})
header = type("header", (Element,), {"name": "header"})
footer = type("footer", (Element,), {"name": "footer"})

# CLOSED TAGS
base = type("base", (Element,), {"name": "base"})
link = type("link", (Element,), {"name": "link"})  # HTMLLinkElement TODO - closed tags
meta = type("meta", (Element,), {"name": "meta"})  # HTMLMetaElement TODO - closed tags
hr = type("hr", (Element,), {"name": "hr"})
br = type("br", (Element,), {"name": "br"})
wbr = type("wbr", (Element,), {"name": "wbr"})
img = type("img", (Element,), {"name": "img"})  # HTMLImageElement TODO - closed tags
param = type("param", (Element,), {"name": "param"})
source = type("source", (Element,), {"name": "source"})
track = type("track", (Element,), {"name": "track"})
area = type("area", (Element,), {"name": "area"})
col = type("col", (Element,), {"name": "col"})
input = type("input", (Element,), {"name": "input"})
keygen = type("keygen", (Element,), {"name": "keygen"})
command = type("command", (Element,), {"name": "command"})

main = type("main", (Element,), {"name": "main"})

# obsolete
applet = type("applet", (Element,), {"name": "applet"})
# object = type('object', (Element,), {'name': 'object'})
basefont = type("basefont", (Element,), {"name": "basefont"})
center = type("center", (Element,), {"name": "center"})
# dir = type('dir', (Element,), {'name': 'dir'})
embed = type("embed", (Element,), {"name": "embed"})
isindex = type("isindex", (Element,), {"name": "isindex"})
listing = type("listing", (Element,), {"name": "listing"})
plaintext = type("plaintext", (Element,), {"name": "plaintext"})
s = type("s", (Element,), {"name": "s"})
u = type("u", (Element,), {"name": "u"})
strike = type("strike", (Element,), {"name": "strike"})
xmp = type("xmp", (Element,), {"name": "xmp"})
template = type("template", (Element,), {"name": "template"})
picture = type("picture", (Element,), {"name": "picture"})
dialog = type("dialog", (Element,), {"name": "dialog"})


class Comment(Node):

    nodeType: int = Node.COMMENT_NODE
    __slots__ = ('data')

    def __init__(self, data) -> None:
        self.data = data
        super().__init__()

    def toString(self) -> str:
        return f'<!--{self.data}-->'
    __str__ = toString


class CDATASection(Node):

    nodeType: int = Node.CDATA_SECTION_NODE
    __slots__ = ('data')

    def __init__(self, data) -> None:
        self.data = data

    def toString(self) -> str:
        return f'<![CDATA[{self.data}]]>'
    __str__ = toString


class DocumentType(Node):

    nodeType = Node.DOCUMENT_TYPE_NODE
    __slots__ = ('name', 'publicId', 'systemId')

    def __init__(self, name: str = "html", publicId: str = "", systemId: str = "") -> None:
        self.name: str = name  # A DOMString, eg "html" for <!DOCTYPE HTML>.
        self.publicId: str = publicId  # eg "-//W3C//DTD HTML 4.01//EN", empty string for HTML5.
        self.systemId: str = systemId  # eg "http://www.w3.org/TR/html4/strict.dtd", empty string for HTML5.
        super().__init__()

    def internalSubset(self):
        ''' A DOMString of the internal subset, or None. Eg "<!ELEMENT foo (bar)>".'''
        if self.systemId:
            return self.systemId
        else:
            return None

    # def notations(self) -> NamedNodeMap:
    #     """ A NamedNodeMap with notations declared in the DTD. """
    #     nnm = NamedNodeMap()
    #     for item in self.ownerDocument.args:
    #         if item.nodeType == Node.NOTATION_NODE:
    #             nnm.append(item)
    #     return nnm

    # @property
    # def nodeType(self):
    #     return Node.DOCUMENT_TYPE_NODE

    def __str__(self) -> str:
        return f"<!DOCTYPE {self.name} {self.publicId} {self.systemId}>"


doctype = DocumentType
comment = Comment


def create_element(name="custom_tag", *args, **kwargs):
    """
    A method for creating custom tags

    tag name needs to be set due to custom tags with hyphens can't be classnames.
    i.e. hypenated tags <some-custom-tag></some-custom-tag>
    """
    # checks if already exists
    if name in html_tags:
        return globals()[name](*args, **kwargs)

    custom_tag = type("custom_tag", (Element,), {"name": name})
    new_tag = custom_tag(*args, **kwargs)
    new_tag.name = name
    return new_tag
