import argparse
import os
from collections import defaultdict


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='enter a directory path')
    args = parser.parse_args()
    return args


def get_all_files_in_directory(path):
    file_info_dict = defaultdict(list)
    for path, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            file_path = os.path.join(path, file_name)
            file_size = os.path.getsize(file_path)
            file_name_and_size = (file_name, file_size)
            file_info_dict[file_name_and_size].append(file_path)
    return file_info_dict


def get_duplicate_file_names_and_paths(all_files_info):
    all_duplicates = {}
    for (file_name, file_size), path_list in all_files_info.items():
        if len(path_list) > 1:
            all_duplicates[file_name] = path_list
    return all_duplicates


def print_duplicates(duplicate_dict):
    if not duplicate_dict:
        print('The directory does not contain duplicate files.')
    if duplicate_dict:
        print('The directory contains these duplicate files:')
        for file_name, file_paths in duplicate_dict.items():
            print(file_name)
            for path in file_paths:
                print('\t', path)


if __name__ == '__main__':
    console_arguments = get_console_arguments()
    user_path = console_arguments.path
    if not os.path.exists(user_path):
        exit('Can not find the directory.')
    if not os.path.isdir(user_path):
        exit('The entered path is not a directory path.')
    all_files_in_directory = get_all_files_in_directory(user_path)
    duplicates = get_duplicate_file_names_and_paths(all_files_in_directory)
    print_duplicates(duplicates)
