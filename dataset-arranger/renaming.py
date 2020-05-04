import os, glob, datetime, time
from datetime import date
from datetime import datetime

path_img_dump = "/media/sf_H_DRIVE"
filename_mode = " Filipina"

today = date.today()
today = today.strftime("%b-%d-%Y")

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def rename_files():
    for folders in os.listdir(path_img_dump):

        folder_path = os.path.join(path_img_dump,folders)

        # files = glob.glob(folder_path + "/" + "*")
        filename_iterator = 0
        for filenames in files(folder_path):
            filename_iterator += 1
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            src = os.path.join(folder_path,filenames)
            dst = os.path.join(folder_path, filename_mode + '-' + str(filename_iterator) + '.jpg')
            # print(filenames_path)
            os.rename(src,dst)
            print('renamed',src,'to',dst)

def rename_folders():
    for index, folders in enumerate(os.listdir(path_img_dump)):
        # print(folders[-len(filename_mode):])

        def if_foldername():
            if folders[-len(filename_mode):] == filename_mode:
                src = os.path.join(path_img_dump, folders)
                dst = os.path.join(path_img_dump, folders[:-len(filename_mode)])

                os.rename(src, dst)
                print('renamed',src,'to',dst)

        def just_rename():
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            src = os.path.join(path_img_dump, folders)
            dst = os.path.join(path_img_dump, today + '-' +str(timestamp))

            os.rename(src, dst)
            print('renamed',src,'to',dst)

        if_foldername()
        # just_rename()

rename_folders()