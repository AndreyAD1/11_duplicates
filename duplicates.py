import argparse
import os
import pathlib
from collections import Counter


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='enter a directory path')
    args = parser.parse_args()
    return args


def get_file_name_and_size(file_path):
    file_name = file_path.name
    file_size = file_path.stat().st_size
    return file_name, file_size


def get_all_files_in_directory(path):
    file_info_dict = {}
    for path, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            file_path = os.path.join(path, file_name)
            file_size = os.path.getsize(file_path)
            file_info_dict[file_path] = (file_name, file_size)
    return file_info_dict


def get_paths_of_duplicate_file(duplicate_name_and_size, all_files_info):
    duplicate_path_list = [
        file_path
        for file_path, file_name_and_size in all_files_info
        if file_name_and_size == duplicate_name_and_size
    ]
    return duplicate_path_list


def get_all_duplicate_files(duplicate_items):
    duplicate_list = [
        file_name_and_size
        for file_name_and_size, file_repeats_number in duplicate_items
        if file_repeats_number > 1
    ]
    return duplicate_list


def get_name_and_path_of_duplicates(duplicate_counter_items, all_files_items):
    duplicates_dict = {}
    duplicate_file_list = get_all_duplicate_files(duplicate_counter_items)
    for file_name_and_size in duplicate_file_list:
        duplicate_file_paths = get_paths_of_duplicate_file(file_name_and_size, all_files_items)
        file_name = file_name_and_size[0]
        duplicates_dict[file_name] = duplicate_file_paths
    return duplicates_dict


def get_duplicate_file_names_and_paths(path):
    all_files_info = get_all_files_in_directory(path)
    duplicate_counter = Counter(all_files_info.values())
    all_duplicates = get_name_and_path_of_duplicates(
        duplicate_counter.items(),
        all_files_info.items()
    )
    return all_duplicates


def print_duplicates(duplicate_dict):
    print('The directory contains these duplicate files:')
    for file in duplicate_dict:
        print(file)
        all_paths = duplicate_dict[file]
        for path in all_paths:
            print('       {}'.format(path))


if __name__ == '__main__':
    console_arguments = get_console_arguments()
    user_path = console_arguments.path
    directory_existing = os.path.exists(user_path)
    # if not directory_existing:
    #     exit('Can not find the directory.')
    # user_path = pathlib.Path(user_path)
    # if not user_path.is_dir():
    #     exit('The entered path is not a directory path.')
    duplicates = get_duplicate_file_names_and_paths(
        user_path
    )
    print_duplicates(duplicates)
