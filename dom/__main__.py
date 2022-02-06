"""
    come CLI
    ====================================
    - some useful cli commands
"""

import argparse
import os
import sys

import httpx
from selectolax.parser import HTMLParser

from dom import __version__


def parse_args():
    parser = argparse.ArgumentParser(add_help=False,
                                     prog="come",
                                     usage="%(prog)s [options]",
                                     description="A domonic-like wrapper around selectolax")

    parser.add_argument('-v', '--version', action='store_true')
    parser.add_argument(
    "-q",
    "--querySelectorAll",
    help="pass a url and a css query",
    type=str,
    nargs="*",
    default=None,
    )

    args = parser.parse_args()
    return args


def do_things(arguments):

    if arguments.version is True:
        print(__version__)
        return __version__

    if arguments.querySelectorAll is not None:
        url, query = arguments.querySelectorAll
        if 'http' not in url:
            url = 'https://' + url
        r = httpx.get(url)
        doc = HTMLParser(r.text)
        result = doc.css(query)
        for n in result:
            print(str(n.html))

def run():
    """[Entry point required by setup.py console_scripts.]
    """
    args = parse_args()
    do_things(args)


if __name__ == "__main__":
    run()
