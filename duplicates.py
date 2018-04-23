import argparse
import os
import pathlib


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='enter a directory path')
    args = parser.parse_args()
    return args


def get_dublicates(path):
    # Path.samefile(otherpath)
    # p = Path('.')
    # [x for x in p.iterdir() if x.is_dir()]
    pass


def print_dublicates(files):
    pass


if __name__ == '__main__':
    console_arguments = get_console_arguments()
    directory_path = console_arguments.directory
    print(directory_path)
    directory_existing = os.path.exists(directory_path)
    if directory_existing:
        dublicates = get_dublicates(directory_path)
    if not directory_existing:
        exit('Can not find the directory.')
    print_dublicates(dublicates)
