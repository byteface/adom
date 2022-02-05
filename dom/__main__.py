"""
    come CLI
    ====================================
    - some useful cli commands
"""

import argparse
import os
import sys

from dom import __version__


def parse_args():
    parser = argparse.ArgumentParser(add_help=False,
                                     prog="come",
                                     usage="%(prog)s [options]",
                                     description="A domonic-like wrapper around selectolax")

    parser.add_argument('-v', '--version', action='store_true')
    args = parser.parse_args()
    return args


def do_things(arguments):

    if arguments.version is True:
        print(__version__)
        return __version__


def run():
    """[Entry point required by setup.py console_scripts.]
    """
    args = parse_args()
    do_things(args)


if __name__ == "__main__":
    run()
