import os
from pathlib import Path

path1 = '/mnt/i/RKB-Dataset/Coding Mom (Backup) - 4 May 2020/Coding Mom/Novi/HASIL AKHIR DATA SET/APRIL'
path2 = '/mnt/j/Instagram_Indonesia_RAW'

list1 = os.listdir(path1)
list2 = os.listdir(path2)

list2 = list(dict.fromkeys(list2))
print(list2[::-1])

# for names in list1:
#     if names in list2:
#         print(names)