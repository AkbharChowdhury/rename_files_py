# https://www.youtube.com/watch?v=jVN2vXkXdsE
import pathlib
import os
from os import path


def rename_folder(rootdir):
    if not path.exists(rootdir):
        raise FileNotFoundError

    for file in os.listdir(rootdir):
        directory = os.path.join(rootdir, file)
        substring = '-main'
        # check if parent folder is root directory
        if os.path.isdir(directory) and substring in file:
            renamed_file = file.split(substring)[0]
            os.chdir(rootdir)
            os.rename(file, renamed_file)


if __name__ == '__main__':
    root_directory = '/Users/akbhar/Documents/Github_projects'
    rename_folder(root_directory)
