# coding: utf-8

import os
import pathlib
import zipfile


def all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

if __name__ == '__main__':
    s = input("Dir: ")
    root_dir = s.strip('\"')

    print("Processing...")
    print()

    for i in all_files(root_dir):
        print(i)
        folder, ext = os.path.splitext(i)
        os.mkdir(folder)
        filepath = folder + "/" + ext
        with zipfile.ZipFile(i) as zip_f:
            zip_f.extractall(pathlib.Path(filepath).parent)

    print("Done!")
    os.system("pause > nul")