from prnm import renops

import argparse
import os


def main():
    print os.getcwd()

    parser = argparse.ArgumentParser(
        prog = 'picrename',
        description="Rename pictures with a date string and incrementing index"
        )

    parser.add_argument('-a', '--alpha_index', 
            action = 'store_true',
            default = False)

    args = parser.parse_args()

    renops.rename_all(".", 'A', '001')

