#! /usr/bin/env python
import sys

print sys.path

from prnm import rename_all
import os

def run():
    print os.getcwd()
    rename_all(".", 'A', '001')

if __name__ == "__main__":
    run()
