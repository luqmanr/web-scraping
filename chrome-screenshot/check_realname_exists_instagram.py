import csv, os

instagram_list = {}
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
            instagram_list.update({username[4].lower(): username[1].lower()})

names_list = []
with open('../Face Artis Indonesia.csv', 'r', newline='', encoding='mac_roman') as csv_file, open('../Test.csv', 'w') as writeFile:
    username_reader = csv.reader(csv_file, delimiter=',')
    writer = csv.writer(writeFile)
    line_count = 0
    for index, username in enumerate(username_reader):
        # if (index == 0) or (username[1] == ''):
            # pass
        # else:
        names_list.append(username)
        # print(username)
        # writer.writerow(username)

    # print(names_list)
    for index, names in enumerate(names_list):
        realname = names[1].lower()

        if realname in instagram_list:
            # print(realname)
            # print(instagram_list[realname])
            names[3] = instagram_list[realname]
            names_list[index][3] = instagram_list[realname]
            # print(names_list[index])
        
        writer.writerow(names)

    # print(names_list)