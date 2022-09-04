import os
from os import path


class FolderHandler:

    def rename_folder(self, root_dir):

        if not path.exists(root_dir):
            print('Error: the specified directory cannot be found')
            return

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