import csv, os

instagram_dict = {}
instagram_username_list = []
names_list = []
duplicate_names_dict = {}

with open('../Face Instagram Coding Mom.csv', 'r', newline='', encoding='mac_roman') as csv_file:
    username_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for index, username in enumerate(username_reader):
        if (index == 0) or (username[1] == ''):
            pass
        else:
            # print(username)
            # print(username[1], username[4])
            # list_value = (username[1]: username[4])
            instagram_name = username[1]
            real_name = username[4]
            instagram_dict.update({username[4].lower(): username[1].lower()})
            instagram_username_list.append(username[4])


with open('../Face Artis Indonesia.csv', 'r', newline='', encoding='mac_roman') as csv_file, open('../Test.csv', 'w') as writeFile:
    name_reader = csv.reader(csv_file, delimiter=',')
    writer = csv.writer(writeFile)
    line_count = 0
    for index, name in enumerate(name_reader):
        # if (index == 0) or (name[1] == ''):
            # pass
        # else:
        names_list.append(name)
        # print(name)
        # writer.writerow(name)

    # print(names_list)
    for index, names in enumerate(names_list):
        realname = names[1].lower()

        for keys in instagram_dict.keys():
            if realname in keys.lower():
                # print(realname)
                # print(instagram_dict)
                names[3] = instagram_dict[keys]
                names_list[index][3] = instagram_dict[keys]

                # duplicate_names_dict.update({names[1]: instagram_dict[realname]})
                duplicate_names_dict.update({instagram_dict[keys]: names[1]})
                # print(names_list[index])
            
    for duplicates in duplicate_names_dict:
        row = []
        row.append(duplicates)
        row.append(duplicate_names_dict[duplicates])
        # print(row)
        writer.writerow(row)

    # print(duplicate_names_dict)