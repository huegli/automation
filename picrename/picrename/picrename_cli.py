#! /usr/bin/env python

from prnm import renops
import os

def run():
    print os.getcwd()
    renops.rename_all(".", 'A', '001')

if __name__ == "__main__":
    run()
