import os, time, errno, pickle, stdiomask, getpass, sys
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
from urllib.request import urlopen
import json
import csv
import yaml

def linux_webdriver():
    CHROME_PATH = '/usr/bin/google-chrome'
    CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
    WINDOW_SIZE = "1440,2560"

    sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

    driver = webdriver.Chrome(
        executable_path="/usr/lib/chromium-browser/chromedriver",
        chrome_options=chrome_options
    )
    return driver

def windows_webdriver():
    driver = webdriver.Chrome("C:\\Windows\webdriver\chromedriver.exe")
    return driver

def running_os():
    os_type = str(input('What OS are you running in? \n insert 1 for Linux \n insert 2 for Windows \n Input: '))
    print('true OS = ',sys.platform)

    if os_type == "1":
        driver = linux_webdriver()
    elif os_type == "2":
        driver = windows_webdriver()
    else:
        print("please pick one or the other")
        running_os()
    return driver

driver = running_os()

filename = 'followers.csv'
with open(filename) as csvfile:
    reader = csv.reader(csvfile)

    usernames=[]
    for row in reader:
        username = row[0]
        usernames.append(username)

    usernames1 = []
    for user in usernames:
        username = user.split(',')
        username = username[2]
        usernames1.append(username)

login_id = input('Your IG Account Username: ')
password = getpass.getpass('Your IG Account Password: ')

def login_instagram():
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        username_bar = driver.find_element_by_name("username")
        username_bar.send_keys(login_id)

        password_bar = driver.find_element_by_name("password")
        password_bar.send_keys(password)
        time.sleep(2)

        login_button = driver.find_element_by_class_name("L3NKy")
        login_button.click()
    except:
        print("log in failed")
        pass

    time.sleep(5)

    user_profile_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a'
    try:
        check_logged_in = driver.find_element_by_xpath(user_profile_xpath)
        if check_logged_in:
            print(" ")
            print("LOG IN SUCCESS")
    except:
        print(" ")
        print("LOG IN FAILED")

login_instagram()

def followerButton():
    try:
        follButtonXpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        follower_button = driver.find_element_by_xpath(follButtonXpath)
        print("button found")
        print(follower_button.text)
        follower_button.click()
        print("button clicked")
        printfoll = (follower_button.text)
        follValue = printfoll.split()
        print(follValue[0])
        follvalue = follValue[0]
        return follvalue
    except:
        pass

# fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
# scroll = 0
# while scroll < xint:
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
#     time.sleep(0.1)
#     scroll += 1
#     if scroll == xint/2:
#         print("break")
#         break
#     else:
#         pass

def follGet(n):
    try:
        str_n = str(n)
        follXpath = '/html/body/div[4]/div/div[2]/ul/div/li[' + str_n + ']/div/div[1]/div[2]/div[1]/a'
        follower_name = driver.find_element_by_xpath(follXpath)
        time.sleep(0.2)
        follvalue = (follower_name.text)
        return follvalue
    except:
        pass
counter = 0
def URL():
    max = 100  #maximal userID to take (to avoid account block by Instagram)
    while counter <= max:
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.instagram.com/"+zstr+"/?__a=1")
        time.sleep(0.3)
        userID=driver.find_element_by_xpath('/html/body/pre')
        user=userID.get_attribute('innerHTML')
        s=user
        y=yaml.load(s, Loader=yaml.FullLoader)
        l=(y.get("logging_page_id"))
        IGid=(l.split('_'))
        IGidVal = IGid[1]
        driver.switch_to.window(driver.window_handles[0])
        if counter >= max:
            print("ID Limit exceded")
            break
        return IGidVal

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[0])

time.sleep(3)

usernamecounter = 0
for i in range(1, 100):
    usernames2 = str(usernames1[usernamecounter])
    print(usernames2)
    driver.get("https://www.instagram.com/"+ usernames2 +"/")
    follvalue=followerButton()
    folllist=[]
    xint = int(follvalue)
    fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
    scroll = 0
    while scroll < xint:
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        time.sleep(0.1)
        scroll += 1
        if scroll == xint/2:
            print("break")
            break
        else:
            pass
    
    zstr = str(follGet(i))
    print(str(i)+zstr)

    IDstr = str(URL())
    counter += 1
    if IDstr == "None":
        IDstr = "ID limit exceded"
    else:
        pass
    print(IDstr)

    usernamecounter += 1
    time.sleep(0.5)
    folllist.append(zstr + ", " + IDstr)

print(folllist)
time.sleep(3)
with open("followers" + "_user" + ".csv", 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for follower in folllist:
        wr.writerow([follower])

print(folllist)
time.sleep(5)
driver.close
