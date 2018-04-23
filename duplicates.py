import argparse
import os
import pathlib


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='enter a directory path')
    args = parser.parse_args()
    return args


def get_all_files_in_directory(path, file_paths):
    for file_system_object in path.iterdir():
        if file_system_object.is_dir():
            file_paths = get_all_files_in_directory(
                file_system_object,
                file_paths
            )
        if file_system_object.is_file():
            file_paths.append(file_system_object)
    return file_paths


def get_dublicates(path):
    all_file_paths = []
    all_file_paths = get_all_files_in_directory(path, all_file_paths)
    print(all_file_paths)


def print_dublicates(files):
    pass


if __name__ == '__main__':
    console_arguments = get_console_arguments()
    user_path = console_arguments.directory
    directory_existing = os.path.exists(user_path)
    if not directory_existing:
        exit('Can not find the directory.')
    user_path = pathlib.Path(user_path)
    if not user_path.is_dir():
        exit('The entered path is not a directory path.')
    dublicates = get_dublicates(user_path)
    print_dublicates(dublicates)
