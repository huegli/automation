from prnm import renops

import argparse


def main():

    parser = argparse.ArgumentParser(
        prog = 'picrename',
        description =
            "Rename pictures with a date string and incrementing index",
        formatter_class=argparse.RawTextHelpFormatter

        )

    parser.add_argument('-a', '--alpha_index', 
            help = """
Alphabet character to use for part of the new
picture name (e.g. -a 'A')
            """,
            action = 'store',
            default = 'A')

    parser.add_argument('-n', '--num_index',
            help = """
Numerical index at which to start numbering
(e.g. -n '001')
            """,
            action = 'store',
            default = '001')

    parser.add_argument('-v', '--verbose', type=int, default = 1,
            help = """
 0  - No ouput
 1  - Warnings on files that are not pictures with EXIF
 >1 - Print the new names of the picture files
            """)

    parser.add_argument('-d', '--debug_only',
            help = """
Just print the new names without actually renaming 
the picture files
            """,
            action = 'store_true')

    parser.add_argument('dirname',
            help = "Directory name in which to rename the pictures")

    args = parser.parse_args()

    renops.rename_all(args.dirname, args.alpha_index , args.num_index, 
            args.verbose)

