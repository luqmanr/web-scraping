import os, csv, shutil, errno

work_path = '/mnt/i/RKB-Dataset/Coding Mom - Copy/'
save_path = '/mnt/i/RKB-Dataset/Coding Mom (Unique)/'

def ifFolder(work_path):
    folders = []
    for path in os.listdir(work_path):
        if os.path.isdir(os.path.join(work_path, path)):
            folders.append(path)
    return folders

## IF YOU WANT TO COMPARE TWO FOLDERS
# folderIDsrc = ifFolder(work_path)
# folderIDdst = ifFolder(save_path)

## IF YOU WANT TO READ FROM CSV FILE
folderIDsrc = ifFolder(work_path)
folderIDdst = []
with open('./Malaysia.csv', 'r', newline='', encoding='mac_roman') as csv_file:
    name_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for names in name_reader:
        folderIDdst.append(names[0])
    print(folderIDdst)

def checkDuplicate(folderIDsrc, folderIDdst):
    for folderSrc in folderIDsrc:
        for folderDst in folderIDdst:
            if folderDst.lower() == folderSrc.lower():
                print(folderDst)

checkDuplicate(folderIDsrc,folderIDdst)

moms = ifFolder(work_path)
print(moms)
def copyDuplicates(work_path, save_path): ## USE THIS FUNCTION IF YOU WANT TO MOVE AND RENAME DUPLICATE IDs TO THEIR REAL NAME
    for mom in moms:
        org_path = os.path.join(work_path, mom)
        out_path = os.path.join(save_path, mom)

        duplicate_names_list = []
        duplicate_names_dict = {}
        to_rename_list = []

        with open('../Test.csv', 'r', newline='', encoding='mac_roman') as csv_file:
            username_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for index, names in enumerate(username_reader):
                # print(names[0])
                duplicate_names_list.append(names[0])
                duplicate_names_dict.update({names[0]:names[1]})

            for index, folders in enumerate(os.listdir(org_path)):
                # print(folders)
                for duplicate_names in duplicate_names_list:
                    if duplicate_names.lower() in folders.lower():
                        
                        src = os.path.join(org_path, folders)
                        dst = os.path.join(out_path, duplicate_names_dict[duplicate_names])

                        # print(folders)
                        # print(duplicate_names)
                        print('renamed',src,'to',dst)

                        try:
                            os.makedirs(out_path)
                            print('dir made')
                        except OSError as e:
                            if e.errno != errno.EEXIST:
                                raise
                        try:
                            # shutil.copytree(src, dst)
                            shutil.move(src, dst)
                        except:
                            pass

def moveUnique(work_path,save_path): ## USE THIS FUNCTION IF YOU WANT TO MOVE UNIQUE INSTAGRAM IDs TO A NEW FOLDER
    for mom in moms:
        org_path = os.path.join(work_path, mom)
        out_path = os.path.join(save_path, mom)

        duplicate_names_list = []
        duplicate_names_dict = {}
        to_rename_list = []

        with open('../Test.csv', 'r', newline='', encoding='mac_roman') as csv_file:
            username_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for index, names in enumerate(username_reader):
                # print(names[0])
                duplicate_names_list.append(names[0])
                duplicate_names_dict.update({names[0]:names[1]})

            for index, folders in enumerate(os.listdir(org_path)):
                # print(folders)
                for duplicate_names in duplicate_names_list:
                    if duplicate_names.lower() in folders.lower():
                        pass
                    else:    
                        src = os.path.join(org_path, folders)
                        dst = os.path.join(out_path, folders)

                        # print(folders)
                        # print(duplicate_names)
                        print('renamed',src,'to',dst)

                        try:
                            os.makedirs(out_path)
                            print('dir made')
                        except OSError as e:
                            if e.errno != errno.EEXIST:
                                raise
                        try:
                            # shutil.copytree(src, dst)
                            shutil.move(src, dst)
                        except:
                            pass

# copyDuplicates(work_path, save_path)
# moveUnique(work_path,save_path)