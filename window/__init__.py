"""
    window
    ====================================

"""
import sys
import httpx

from selectolax.parser import HTMLParser

class Window():

    def __init__(self):
        self._document = None
        self._location = None

    @property
    def document(self):
        return self._document

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, url):
        if 'http' not in url:
            url = 'https://' + url
        r = httpx.get(url)
        # from datetime import datetime
        # print('requested', datetime.now())
        self._document = HTMLParser(r.text)
        # print('done!', datetime.now())
        self._location = url

# global window
window = Window()
