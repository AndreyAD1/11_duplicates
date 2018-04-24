import argparse
import os


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='enter a directory path')
    args = parser.parse_args()
    return args


def get_file_info_dict(file_features, path, file_dict):
    if file_features in file_dict:
        file_dict[file_features].append(path)
        return file_dict
    file_dict[file_features] = [path]
    return file_dict


def get_all_files_in_directory(path):
    file_info_dict = {}
    for path, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            file_path = os.path.join(path, file_name)
            file_size = os.path.getsize(file_path)
            file_name_and_size = (file_name, file_size)
            file_info_dict = get_file_info_dict(
                file_name_and_size,
                file_path,
                file_info_dict
            )
    return file_info_dict


def get_duplicate_file_names_and_paths(path):
    all_files_info = get_all_files_in_directory(path)
    all_duplicates = {}
    for file_name_and_size, file_path_list in all_files_info.items():
        if len(file_path_list)>1:
            file_name = file_name_and_size[0]
            all_duplicates[file_name] = file_path_list
    return all_duplicates


def print_duplicates(duplicate_dict):
    if not duplicate_dict:
        print('The directory does not contain duplicate files.')
    if duplicate_dict:
        print('The directory contains these duplicate files:')
        for file_name in duplicate_dict:
            print(file_name)
            all_paths = duplicate_dict[file_name]
            for path in all_paths:
                print('\t', path)


if __name__ == '__main__':
    console_arguments = get_console_arguments()
    user_path = console_arguments.path
    if not os.path.exists(user_path):
        exit('Can not find the directory.')
    if not os.path.isdir(user_path):
        exit('The entered path is not a directory path.')
    duplicates = get_duplicate_file_names_and_paths(user_path)
    print_duplicates(duplicates)
