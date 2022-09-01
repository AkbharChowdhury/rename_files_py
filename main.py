# https://www.youtube.com/watch?v=jVN2vXkXdsE
import os
from os import path


def rename_folder(root_dir):
    if not path.exists(root_dir):
        raise FileNotFoundError

    substring = '-main'
    folders = os.listdir(root_dir)

    if substring not in "~".join(folders):
        print('no folder names were updated')
        return

    for folder in folders:
        directory = os.path.join(root_dir, folder)
        # check if parent folder is root directory
        if os.path.isdir(directory) and substring in folder:
            renamed_folder = folder.split(substring)[0]
            os.chdir(root_dir)
            os.rename(folder, renamed_folder)
            print(f'Folder {folder} has been renamed to {renamed_folder}')


if __name__ == '__main__':
    rename_folder(root_dir='/Users/akbhar/Documents/Github_projects')
