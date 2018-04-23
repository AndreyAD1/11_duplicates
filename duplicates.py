import argparse
import os
import pathlib
from collections import Counter


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='enter a directory path')
    args = parser.parse_args()
    return args


def get_file_name_and_size(file_path):
    file_name = file_path.name
    file_size = file_path.stat().st_size
    return file_name, file_size


def get_all_files_in_directory(path, file_info):
    for file_system_object in path.iterdir():
        if file_system_object.is_dir():
            file_info = get_all_files_in_directory(
                file_system_object,
                file_info
            )
        if file_system_object.is_file():
            file_name_and_size = get_file_name_and_size(file_system_object)
            file_info[file_system_object] = file_name_and_size
    return file_info


def get_paths_of_duplicate_file(duplicate_name_and_size, file_info_list):
    duplicate_path_list = []
    for file_path, file_name_and_size in file_info_list:
        if file_name_and_size == duplicate_name_and_size:
            duplicate_path = file_path
            duplicate_path_list.append(duplicate_path)
    return duplicate_path_list


def get_all_duplicate_files(duplicate_items):
    duplicate_list = [
        file_name_and_size
        for file_name_and_size, file_repeats_number in duplicate_items
        if file_repeats_number>1
    ]
    return duplicate_list



def get_name_and_path_of_duplicates(duplicate_items, all_files_items):
    duplicates_dict = {}
    duplicate_files = get_all_duplicate_files(duplicate_items)
    for file_name_and_size in duplicate_files:
        duplicate_file_paths = get_paths_of_duplicate_file(file_name_and_size, all_files_items)
        file_name = file_name_and_size[0]
        duplicates_dict[file_name] = duplicate_file_paths
    return duplicates_dict


def get_duplicates(path):
    file_information = {}
    all_files_info = get_all_files_in_directory(path, file_information)
    duplicate_counter = Counter(all_files_info.values())
    all_duplicates = get_name_and_path_of_duplicates(
        duplicate_counter.items(),
        all_files_info.items()
    )
    return all_duplicates


def print_duplicates(files):
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
    duplicates = get_duplicates(user_path)
    print(duplicates)
    # if duplicates:
    #     print('The directory contains the duplicate files.')
    # else:
    #     print('The directory does not contain duplicate files.')
